import datetime
from django.utils import timezone
from drf_spectacular.utils import extend_schema, OpenApiParameter
from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError
from rest_framework.pagination import PageNumberPagination
from django.db.models import Q

from project.models import *
from project.serializers import *


class SessaoPagination(PageNumberPagination):
    page_size = 6
    page_size_query_param = 'page_size'
    max_page_size = 100


@extend_schema(
    summary="Agenda do Tutor",
    description="Este endpoint permite gerenciar os horários disponíveis (slots). Usar  o parâmetro '?tutor=ID' na URL para filtra a agenda para a de um tutor específico.",
    request=AgendaSerializer,
    responses=AgendaSerializer,
    tags=['05. Solicitar Sessão'],
    parameters=[
        OpenApiParameter(
            name='tutor',
            description='ID do Tutor para buscar os horários disponíveis na agenda',
            required=False,
            type=int
        ),
    ]
)
class AgendaViewSet(viewsets.ModelViewSet):
    queryset = AgendaModel.objects.all()
    serializer_class = AgendaSerializer
    permission_classes = [IsAuthenticated]
    http_method_names = ['get', 'post', 'delete']

    def get_queryset(self):
        queryset = AgendaModel.objects.all().select_related('tutorId')

        tutor_id = self.request.query_params.get('tutor')

        if tutor_id is not None:
            queryset = queryset.filter(tutorId=tutor_id)

        return queryset

    def create(self, request, *args, **kwargs):

        try:
            tutor = TutorModel.objects.get(usuarioId=self.request.user)
        except TutorModel.DoesNotExist:
            raise ValidationError(
                {"mensagem": "Apenas tutores podem criar agendas."})

        data = request.data.copy()
        data['tutorId'] = tutor.id

        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)

        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


@extend_schema(
	summary="Dados de Solicitação",
	description=(
		"Este endpoint gerencia as solicitações de tutoria feitas por alunos. "
		"Permite filtrar por tipo de participação ('tutor' ou 'aprendiz'), ID da Área, "
		"ID da Especialidade, escolher a direção da ordenação por data ('desc' ou 'asc') e possui paginação."
	),
	request=SolicitacaoSerializer,
	responses=SolicitacaoSerializer,
	tags=['05. Solicitar Sessão'],
	parameters=[
		OpenApiParameter(name='tipo', description="Filtra pelo papel do usuário logado ('tutor' ou 'aprendiz')", required=False, type=str),
		OpenApiParameter(name='area', description="ID da Área para filtrar as solicitações", required=False, type=int),
		OpenApiParameter(name='especialidade', description="ID da Especialidade para filtrar as solicitações", required=False, type=int),
		OpenApiParameter(name='ordem', description="Direção da ordenação por data: 'desc' (mais recentes primeiro, padrão) ou 'asc' (mais antigas primeiro)", required=False, type=str),
		OpenApiParameter(name='page', description="Número da página que deseja buscar", required=False, type=int),
	]
)
class SolicitacaoViewSet(viewsets.ModelViewSet):
    serializer_class = SolicitacaoSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = SessaoPagination
    http_method_names = ['get', 'post', 'patch']

    def get_queryset(self):
        user = self.request.user

        tipo_filtro   = self.request.query_params.get('tipo', '').lower()
        area_id       = self.request.query_params.get('area')
        espec_id      = self.request.query_params.get('especialidade')
        ordem_filtro  = self.request.query_params.get('ordem', '').lower()

        queryset = SolicitacaoModel.objects.filter(
			Q(usuarioId=user) | Q(agendaId__tutorId__usuarioId=user)
		).select_related('usuarioId', 'agendaId__tutorId__usuarioId', 'areaId', 'especialidadeId')

        if tipo_filtro == 'tutor':
            queryset = queryset.filter(
				agendaId__tutorId__usuarioId=user,
				estado=SolicitacaoModel.EstadoSolicitacao.PENDENTE
			)
        elif tipo_filtro == 'aprendiz':
            queryset = queryset.filter(usuarioId=user)
        else:
            queryset = queryset.filter(estado=SolicitacaoModel.EstadoSolicitacao.PENDENTE)

        if area_id is not None:
            queryset = queryset.filter(areaId=area_id)

        if espec_id is not None:
            queryset = queryset.filter(especialidadeId=espec_id)

        if ordem_filtro == 'asc':
            queryset = queryset.order_by('dataPretendida', 'agendaId__horarioInicio')
        else:
            queryset = queryset.order_by('-dataPretendida', '-agendaId__horarioInicio')

        return queryset

    def perform_create(self, serializer):
        logged_user = self.request.user
		
        agenda = serializer.validated_data.get('agendaId')
        data_pretendida = serializer.validated_data.get('dataPretendida')
		
        fuso_local = timezone.get_current_timezone()
        hoje = timezone.localtime(timezone.now())

        def obter_proximo_dia_util(data_base):
            proximo_dia = data_base + datetime.timedelta(days=1)
            if proximo_dia.weekday() == 5:  
                return proximo_dia + datetime.timedelta(days=2)
            elif proximo_dia.weekday() == 6:  
                return proximo_dia + datetime.timedelta(days=1)
            return proximo_dia

        dia_util_seguinte = obter_proximo_dia_util(hoje)
        limite_fim_do_dia = dia_util_seguinte.replace(hour=23, minute=59, second=59, microsecond=0)
		
        momento_da_tutoria_naive = datetime.datetime.combine(data_pretendida, agenda.horarioInicio)
        momento_da_tutoria = timezone.make_aware(momento_da_tutoria_naive, fuso_local)
		
        if momento_da_tutoria < limite_fim_do_dia:
            data_validade = momento_da_tutoria
        else:
            data_validade = limite_fim_do_dia

        serializer.save(
			usuarioId=logged_user,
			validade=data_validade
		)


class AceitarSolicitacaoViewSet(viewsets.ModelViewSet):
    queryset = SolicitacaoModel.objects.all()
    serializer_class = SolicitacaoSerializer
    permission_classes = [IsAuthenticated]
    http_method_names = ['patch']

    def perform_update(self, serializer):
        solicitacao = self.get_object()
        user = self.request.user

        if solicitacao.agendaId.tutorId.usuarioId != user:
            raise ValidationError(
                {"mensagem": "Apenas o tutor responsável pode aceitar esta solicitação."})

        if solicitacao.estado == SolicitacaoModel.EstadoSolicitacao.RECORRENTE:
            solicitacao.recorrente = True
            solicitacao.estado = SolicitacaoModel.EstadoSolicitacao.ACEITO
            solicitacao.save()

            SessaoModel.objects.create(
                usuarioId=solicitacao.usuarioId,
                tutorId=solicitacao.agendaId.tutorId,
                areaId=solicitacao.areaId,
                especialidadeId=solicitacao.especialidadeId,
                dataSessao=solicitacao.dataPretendida,
                horarioInicio=solicitacao.agendaId.horarioInicio,
                horarioFim=solicitacao.agendaId.horarioFim
            )
            return

        if solicitacao.estado != SolicitacaoModel.EstadoSolicitacao.PENDENTE:

            raise ValidationError(
                {"mensagem": "Apenas solicitações pendentes podem ser aceitas."})
        solicitacao.estado = SolicitacaoModel.EstadoSolicitacao.ACEITO
        solicitacao.save()

        SessaoModel.objects.create(
            usuarioId=solicitacao.usuarioId,
            tutorId=solicitacao.agendaId.tutorId,
            areaId=solicitacao.areaId,
            especialidadeId=solicitacao.especialidadeId,
            dataSessao=solicitacao.dataPretendida,
            horarioInicio=solicitacao.agendaId.horarioInicio,
            horarioFim=solicitacao.agendaId.horarioFim
        )


class RecusarSolicitacaoViewSet(viewsets.ModelViewSet):
    queryset = SolicitacaoModel.objects.all()
    serializer_class = SolicitacaoSerializer
    permission_classes = [IsAuthenticated]
    http_method_names = ['patch']

    def perform_update(self, serializer):
        solicitacao = self.get_object()
        user = self.request.user

        if solicitacao.agendaId.tutorId.usuarioId != user:
            raise ValidationError(
                {"mensagem": "Apenas o tutor responsável pode recusar esta solicitação."})

        if solicitacao.estado not in [SolicitacaoModel.EstadoSolicitacao.PENDENTE, SolicitacaoModel.EstadoSolicitacao.RECORRENTE]:
            raise ValidationError(
                {"mensagem": "Apenas solicitações pendentes ou recorrentes podem ser recusadas."})

        solicitacao.estado = SolicitacaoModel.EstadoSolicitacao.RECUSADO
        solicitacao.save()


@extend_schema(
    summary="Sessão de Tutoria",
    description=(
        "Este endpoint gerencia as sessões de tutoria confirmadas. "
        "Permite filtrar por tipo de participação ('tutor' ou 'aprendiz'), ID da Área, "
        "ID da Especialidade, escolher a ordenação por data ('desc' ou 'asc') e possui paginação."
    ),
    request=SessaoSerializer,
    responses=SessaoSerializer,
    tags=['05. Solicitar Sessão'],
    parameters=[
        OpenApiParameter(
            name='tipo',
            description="Filtra as sessões pelo papel do usuário logado ('tutor' ou 'aprendiz')",
            required=False,
            type=str
        ),
        OpenApiParameter(
            name='area',
            description="Filtra as sessões por um ID de Área específico",
            required=False,
            type=int
        ),
        OpenApiParameter(
            name='especialidade',
            description="Filtra as sessões por um ID de Especialidade específico",
            required=False,
            type=int
        ),
        OpenApiParameter(
            name='ordem',
            description="Direção da ordenação por data: 'desc' (mais recentes primeiro, padrão) ou 'asc' (mais antigas primeiro)",
            required=False,
            type=str
        ),
        OpenApiParameter(
            name='page',
            description="Número da página que deseja buscar",
            required=False,
            type=int
        ),
    ]
)
class SessaoViewSet(viewsets.ModelViewSet):
    serializer_class = SessaoSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = SessaoPagination
    http_method_names = ['get']

    def get_queryset(self):
        user = self.request.user

        queryset = SessaoModel.objects.filter(
			Q(usuarioId=user) | Q(tutorId__usuarioId=user)
		).select_related(
            'usuarioId', 
            'tutorId__usuarioId', 
            'areaId', 
            'especialidadeId'
        )
        
        tipo_filtro   = self.request.query_params.get('tipo', '').lower()
        area_id       = self.request.query_params.get('area')
        espec_id      = self.request.query_params.get('especialidade')
        ordem_filtro  = self.request.query_params.get('ordem', '').lower()

        if tipo_filtro == 'tutor':
            queryset = queryset.filter(tutorId__usuarioId=user)
        elif tipo_filtro == 'aprendiz':
            queryset = queryset.filter(usuarioId=user)

        if area_id is not None:
            queryset = queryset.filter(areaId=area_id)

        if espec_id is not None:
            queryset = queryset.filter(especialidadeId=espec_id)

        if ordem_filtro == 'asc':
           return queryset.order_by('dataSessao', 'horarioInicio')

        return queryset.order_by('-dataSessao', '-horarioInicio')

@extend_schema(
    summary="Listar todas as sessões de um tutor (Sem Paginação)",
    description="Endpoint exclusivo para verificação. Retorna a lista completa de sessões de um tutor com base no seu ID passado na URL.",
    responses=SessaoSerializer(many=True),
    tags=['06. Sessões'],
    parameters=[
        OpenApiParameter(
            name='tutor_id',
            description="ID do Tutor para buscar todas as sessões associadas",
            required=True,
            type=int
        ),
    ]
)
class SessoesTutorVerificacaoViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = SessaoSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = None 
    http_method_names = ['get']

    def get_queryset(self):
        tutor_id = self.request.query_params.get('tutor_id')
        
        if not tutor_id:
            return SessaoModel.objects.none()
            
        return SessaoModel.objects.filter(tutorId=tutor_id).select_related(
            'usuarioId', 
            'tutorId__usuarioId', 
            'areaId', 
            'especialidadeId'
        ).order_by('-dataSessao', '-horarioInicio')