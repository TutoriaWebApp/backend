import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.preprocessing import MultiLabelBinarizer

from rest_framework import viewsets, permissions, pagination
from rest_framework.response import Response
from drf_spectacular.utils import extend_schema, OpenApiParameter

from django.db.models import Q
from project.models import *
from project.serializers.SistemaRecomendacaoSerializer import SistemaRecomendacaoSerializer

class RecomendacaoPagination(pagination.PageNumberPagination):
    page_size = 15
    page_size_query_param = 'page_size'
    max_page_size = 60

class SistemaRecomendacaoViewSet(viewsets.ViewSet):
    """
    ViewSet para o Sistema de Recomendação Híbrido de Tutores.
    Utiliza Pandas para manipulação de dados e Scikit-learn para cálculos de similaridade.
    """
    permission_classes = [permissions.IsAuthenticated]
    pagination_class = RecomendacaoPagination

    @extend_schema(
        parameters=[
            OpenApiParameter(name='dia', description='Vetor de dias da semana (SEG, TER, etc)', type={'type': 'array', 'items': {'type': 'string'}}, many=True),
            OpenApiParameter(name='horarioInicio', description='Vetor de horários de início (HH:MM)', type={'type': 'array', 'items': {'type': 'string'}}, many=True),
            OpenApiParameter(name='horarioFim', description='Vetor de horários de fim (HH:MM)', type={'type': 'array', 'items': {'type': 'string'}}, many=True),
            OpenApiParameter(name='area', description='Id de área de pesquisa', type=int, required=False),
            OpenApiParameter(name='especialidade', description='Id de especialidade de pesquisa', type=int, required=False),
            OpenApiParameter(name='page', description='Número da página', type=int, required=False),
            OpenApiParameter(name='page_size', description='Quantidade de itens por página', type=int, required=False),
        ],
        responses={200: SistemaRecomendacaoSerializer(many=True)}
    )
    def list(self, request):
        user = request.user

        # 1. Coleta de Dados e Filtragem (ORM)
        tutors_qs = TutorModel.objects.exclude(usuarioId=user).select_related('usuarioId')

        # Parâmetros de Filtro (Suporte a Vetores)
        dias = request.query_params.getlist('dia') or request.query_params.getlist('dia[]')
        horarios_inicio = request.query_params.getlist('horarioInicio') or request.query_params.getlist('horarioInicio[]')
        horarios_fim = request.query_params.getlist('horarioFim') or request.query_params.getlist('horarioFim[]')
        
        area = request.query_params.get('area')

        if not area:
            return Response({"mensagem": "O parâmetro 'area' é obrigatório para a recomendação."}, status=400)

        especialidade = request.query_params.get('especialidade')

        # Filtro de Agenda (Lógica OR para múltiplos slots)
        if dias and horarios_inicio and horarios_fim:
            schedule_filter = Q()
            for d, hi, hf in zip(dias, horarios_inicio, horarios_fim):
                schedule_filter |= Q(
                    agendas__dia=d,
                    agendas__horarioInicio__lte=hi,
                    agendas__horarioFim__gte=hf
                )
            tutors_qs = tutors_qs.filter(schedule_filter).distinct()

        # Filtro de Especialidade (Prioridade sobre Área)
        if especialidade:
            tutors_qs = tutors_qs.filter(especialidades__id=especialidade)
        elif area:
            tutors_qs = tutors_qs.filter(especialidades__areaId=area).distinct()

        if not tutors_qs.exists():
            return Response([])

        # --- PREPARAÇÃO PANDAS ---

        # DataFrame de Tutores
        tutors_data = []
        all_contem = ContemModel.objects.filter(tutorId__in=tutors_qs).select_related('especialidadeId')
        tutor_specs_map = {}
        for item in all_contem:
            if item.tutorId_id not in tutor_specs_map:
                tutor_specs_map[item.tutorId_id] = []
            tutor_specs_map[item.tutorId_id].append(item.especialidadeId_id)

        for t in tutors_qs:
            tutors_data.append({
                'id': t.id,
                'cidade': t.usuarioId.cidade,
                'estado': t.usuarioId.estado,
                'pontuacao': t.usuarioId.pontuacao,
                'especialidades': tutor_specs_map.get(t.id, [])
            })

        df_tutors = pd.DataFrame(tutors_data)

        # 2. FILTRAGEM BASEADA EM CONTEÚDO (Scikit-learn)

        # One-Hot Encoding das Especialidades
        mlb = MultiLabelBinarizer()
        spec_matrix = mlb.fit_transform(df_tutors['especialidades'])

        # Vetor de Interesse do Usuário (baseado em sessões passadas + interesse atual)
        user_spec_vector = np.zeros((1, spec_matrix.shape[1]))

        # A. Adiciona interesse do contexto atual (Boost)
        if especialidade:
            try:
                spec_id_int = int(especialidade)
                if spec_id_int in mlb.classes_:
                    idx = np.where(mlb.classes_ == spec_id_int)[0][0]
                    user_spec_vector[0, idx] += 10.0 # Peso alto para interesse explícito
            except (ValueError, TypeError):
                pass
        elif area:
            try:
                area_id_int = int(area)
                area_specs = EspecialidadeModel.objects.filter(areaId=area_id_int).values_list('id', flat=True)
                for s_id in area_specs:
                    if s_id in mlb.classes_:
                        idx = np.where(mlb.classes_ == s_id)[0][0]
                        user_spec_vector[0, idx] += 2.0 # Boost moderado para área
            except (ValueError, TypeError):
                pass

        # B. Adiciona interesse histórico
        user_sessions = SessaoModel.objects.filter(usuarioId=user).values_list('especialidadeId', flat=True)
        if user_sessions.exists():
            session_counts = pd.Series(user_sessions).value_counts()
            for spec_id, count in session_counts.items():
                if spec_id in mlb.classes_:
                    idx = np.where(mlb.classes_ == spec_id)[0][0]
                    user_spec_vector[0, idx] += count

        # Similaridade de Cosseno (Especialidades)
        # Se o vetor for todo zero (raro com boost), cosine_similarity retorna 0.
        if np.any(user_spec_vector):
            content_scores = cosine_similarity(user_spec_vector, spec_matrix).flatten()
        else:
            content_scores = np.zeros(len(df_tutors))

        # Ajuste por Localização e Pontuação
        loc_scores = np.where(df_tutors['cidade'] == user.cidade, 3.0,
                             np.where(df_tutors['estado'] == user.estado, 1.0, 0.0))

        final_content_scores = (content_scores * 5.0) + loc_scores + (df_tutors['pontuacao'] / 500.0)

        # 3. FILTRAGEM COLABORATIVA (User-Item Matrix)

        # Pegar todas as avaliações relevantes
        ratings_qs = AvaliacaoTutorModel.objects.all().values('sessaoId__usuarioId', 'tutorId', 'nota')
        if ratings_qs.exists():
            df_ratings = pd.DataFrame(list(ratings_qs))
            df_ratings.columns = ['user_id', 'tutor_id', 'rating']

            # Matriz Usuário-Item
            user_item_matrix = df_ratings.pivot_table(index='user_id', columns='tutor_id', values='rating').fillna(0)

            if user.id in user_item_matrix.index:
                # Similaridade entre usuários
                user_sim = cosine_similarity(user_item_matrix)
                user_sim_df = pd.DataFrame(user_sim, index=user_item_matrix.index, columns=user_item_matrix.index)

                # Predição de notas (média ponderada pela similaridade)
                user_ratings = user_item_matrix.loc[user.id]
                sim_users = user_sim_df[user.id].sort_values(ascending=False)[1:11] # Top 10 similares

                # Cálculo simplificado de predição
                collab_scores_map = {}
                for t_id in df_tutors['id']:
                    if t_id in user_item_matrix.columns:
                        weights = sim_users
                        ratings = user_item_matrix.loc[sim_users.index, t_id]
                        if weights.sum() > 0:
                            pred = (ratings * weights).sum() / weights.sum()
                        else:
                            pred = df_ratings[df_ratings['tutor_id'] == t_id]['rating'].mean()
                        collab_scores_map[t_id] = pred
                    else:
                        collab_scores_map[t_id] = 3.5 # Default
            else:
                # Usuário novo: usa média global de cada tutor
                avg_ratings = df_ratings.groupby('tutor_id')['rating'].mean()
                collab_scores_map = {t_id: avg_ratings.get(t_id, 3.5) for t_id in df_tutors['id']}
        else:
            collab_scores_map = {t_id: 3.5 for t_id in df_tutors['id']}

        df_tutors['collab_score'] = df_tutors['id'].map(collab_scores_map)
        df_tutors['content_score'] = final_content_scores

        # 4. HIBRIDIZAÇÃO FINAL
        # Peso: 60% Colaborativa, 40% Conteúdo
        df_tutors['final_score'] = (df_tutors['collab_score'] * 2.0) + df_tutors['content_score']

        # 5. RETORNO E PAGINAÇÃO
        df_sorted = df_tutors.sort_values(by='final_score', ascending=False)

        # Re-mapeamento para instâncias do Django
        recommended_ids = df_sorted['id'].tolist()
        scores_map = dict(zip(df_sorted['id'], df_sorted['final_score']))

        # Recuperar os objetos do QuerySet original
        tutors_by_id = {t.id: t for t in tutors_qs if t.id in recommended_ids}

        # Montar lista completa ordenada para paginar
        all_recommended_tutors = []
        for t_id in recommended_ids:
            if t_id in tutors_by_id:
                tutor_obj = tutors_by_id[t_id]
                tutor_obj.score = scores_map[t_id]
                all_recommended_tutors.append(tutor_obj)

        # Paginar a lista
        paginator = self.pagination_class()
        page = paginator.paginate_queryset(all_recommended_tutors, request)

        if page is not None:
            serializer = SistemaRecomendacaoSerializer(page, many=True, context={'request': request})
            return paginator.get_paginated_response(serializer.data)

        # Caso a paginação falhe ou não seja solicitada (fallback)
        serializer = SistemaRecomendacaoSerializer(all_recommended_tutors, many=True, context={'request': request})
        return Response(serializer.data)
