import datetime
from zoneinfo import ZoneInfo
from django.utils import timezone
from drf_spectacular.utils import extend_schema, OpenApiParameter
from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError
from rest_framework.pagination import PageNumberPagination
from django.db.models import Q, Count

from project.models import *
from project.serializers import *


class SessaoPagination(PageNumberPagination):
	page_size = 6
	page_size_query_param = 'page_size'
	max_page_size = 100

import datetime
from zoneinfo import ZoneInfo
from django.utils import timezone
from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError
from django.db.models import Q, Count

# ... demais imports ...

def calcular_validade_solicitacao(data_pretendida, horario_inicio_agenda):
    """
    Calcula o prazo de validade no fuso horário do Brasil:
    - Fim do próximo dia útil (23:59:59)
    - Ou o próprio horário de início da sessão, caso ocorra antes desse limite.
    """
    fuso_brasil = ZoneInfo("America/Sao_Paulo")
    agora_brasil = datetime.datetime.now(fuso_brasil)
    hoje_brasil = agora_brasil.date()

    def obter_proximo_dia_util(data_base):
        # 0=Seg, 1=Ter, 2=Qua, 3=Qui, 4=Sex, 5=Sab, 6=Dom
        dia_semana = data_base.weekday()
        if dia_semana == 4:     # Sexta -> Próxima segunda (+3 dias)
            return data_base + datetime.timedelta(days=3)
        elif dia_semana == 5:   # Sábado -> Próxima segunda (+2 dias)
            return data_base + datetime.timedelta(days=2)
        elif dia_semana == 6:   # Domingo -> Próxima segunda (+1 dia)
            return data_base + datetime.timedelta(days=1)
        else:                   # Seg a Qui -> Dia seguinte (+1 dia)
            return data_base + datetime.timedelta(days=1)

    dia_util_seguinte = obter_proximo_dia_util(hoje_brasil)
    
    # Limite padrão: Fim do próximo dia útil às 23:59:59 no horário de Brasília
    limite_fim_do_dia = datetime.datetime.combine(
        dia_util_seguinte,
        datetime.time(23, 59, 59)
    ).replace(tzinfo=fuso_brasil)

    # Horário exato em que a sessão acontecerá
    momento_tutoria = datetime.datetime.combine(
        data_pretendida,
        horario_inicio_agenda
    ).replace(tzinfo=fuso_brasil)

    # Se a sessão for antes do limite do fim do dia útil, o prazo é a própria sessão
    if momento_tutoria < limite_fim_do_dia:
        return momento_tutoria
    return limite_fim_do_dia


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
		).select_related(
            'usuarioId', 
            'agendaId__tutorId',
            'agendaId__tutorId__usuarioId', 
            'areaId', 
            'especialidadeId'
        ).annotate(
            qtd_avaliacoes_aprendiz=Count('usuarioId__avaliacoes_aprendiz', distinct=True),
            qtd_avaliacoes_tutor=Count('agendaId__tutorId__avaliacoes_tutor', distinct=True)
        )

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

		data_validade = calcular_validade_solicitacao(data_pretendida, agenda.horarioInicio)

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

        if solicitacao.estado not in [
            SolicitacaoModel.EstadoSolicitacao.PENDENTE, 
            SolicitacaoModel.EstadoSolicitacao.RECORRENTE
        ]:
            raise ValidationError(
                {"mensagem": "Apenas solicitações pendentes podem ser aceitas."})

        eh_recorrente = solicitacao.recorrente or (
            solicitacao.estado == SolicitacaoModel.EstadoSolicitacao.RECORRENTE
        )

        solicitacao.estado = SolicitacaoModel.EstadoSolicitacao.ACEITO
        solicitacao.save()

        # Cria a sessão atual confirmada
        SessaoModel.objects.create(
            usuarioId=solicitacao.usuarioId,
            tutorId=solicitacao.agendaId.tutorId,
            areaId=solicitacao.areaId,
            especialidadeId=solicitacao.especialidadeId,
            dataSessao=solicitacao.dataPretendida,
            horarioInicio=solicitacao.agendaId.horarioInicio,
            horarioFim=solicitacao.agendaId.horarioFim
        )

        # Cascata semanal se for recorrente
        if eh_recorrente:
            proxima_data = solicitacao.dataPretendida + datetime.timedelta(days=7)
            nova_validade = calcular_validade_solicitacao(proxima_data, solicitacao.agendaId.horarioInicio)

            SolicitacaoModel.objects.create(
                usuarioId=solicitacao.usuarioId,
                agendaId=solicitacao.agendaId,
                areaId=solicitacao.areaId,
                especialidadeId=solicitacao.especialidadeId,
                dataPretendida=proxima_data,
                validade=nova_validade,
                recorrente=True,
                estado=SolicitacaoModel.EstadoSolicitacao.PENDENTE
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
            'tutorId',
            'tutorId__usuarioId', 
            'areaId', 
            'especialidadeId'
        ).annotate(
            qtd_avaliacoes_aprendiz=Count('usuarioId__avaliacoes_aprendiz', distinct=True),
            qtd_avaliacoes_tutor=Count('tutorId__avaliacoes_tutor', distinct=True)
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
	summary="Listar todas as sessões de um tutor como Tutor e Aprendiz (Sem Paginação)",
	description="Endpoint exclusivo para verificação. Retorna a lista completa de sessões onde o Tutor informado participa, seja ensinando ou aprendendo.",
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
			
		try:
			tutor_registro = TutorModel.objects.get(id=tutor_id)
			usuario_do_tutor_id = tutor_registro.usuarioId_id
		except TutorModel.DoesNotExist:
			return SessaoModel.objects.none()
			
		return SessaoModel.objects.filter(
			Q(tutorId=tutor_id) | Q(usuarioId=usuario_do_tutor_id)
		).select_related(
			'usuarioId', 
			'tutorId__usuarioId', 
			'areaId', 
			'especialidadeId'
		).order_by('-dataSessao', '-horarioInicio')
    
@extend_schema(
	summary="Listar todas as solicitações do usuário autenticado (Sem Paginação)",
	description=(
		"Retorna a lista de solicitações associadas ao usuário logado sem paginação. "
		"Suporta parâmetros opcionais para filtrar pelo papel do usuário ('tutor' ou 'aprendiz') "
		"e para trazer apenas solicitações pendentes futuras."
	),
	responses=SolicitacaoSerializer(many=True),
	tags=['05. Solicitar Sessão'],
	parameters=[
		OpenApiParameter(
			name='tipo',
			description="Filtra pelo papel do usuário logado: 'tutor' (recebidas) ou 'aprendiz' (enviadas)",
			required=False,
			type=str
		),
		OpenApiParameter(
			name='apenas_futuras',
			description="Se 'true', retorna apenas solicitações PENDENTES cujo dia e horário ainda não passaram",
			required=False,
			type=bool
		),
	]
)
class TodasSolicitacoesUsuarioViewSet(viewsets.ReadOnlyModelViewSet):
	serializer_class = SolicitacaoSerializer
	permission_classes = [IsAuthenticated]
	pagination_class = None
	http_method_names = ['get']

	def get_queryset(self):
		user = self.request.user

		tipo_filtro = self.request.query_params.get('tipo', '').lower()
		apenas_futuras = self.request.query_params.get('apenas_futuras', '').lower() in ['true', '1']

		# Base QuerySet
		queryset = SolicitacaoModel.objects.filter(
			Q(usuarioId=user) | Q(agendaId__tutorId__usuarioId=user)
		).select_related(
			'usuarioId', 
			'agendaId__tutorId',
			'agendaId__tutorId__usuarioId', 
			'areaId', 
			'especialidadeId'
		).annotate(
			qtd_avaliacoes_aprendiz=Count('usuarioId__avaliacoes_aprendiz', distinct=True),
			qtd_avaliacoes_tutor=Count('agendaId__tutorId__avaliacoes_tutor', distinct=True)
		)

		# Filtro opcional de papel (Tutor ou Aprendiz)
		if tipo_filtro == 'tutor':
			queryset = queryset.filter(agendaId__tutorId__usuarioId=user)
		elif tipo_filtro == 'aprendiz':
			queryset = queryset.filter(usuarioId=user)

		# Filtro opcional: apenas PENDENTES que ainda não venceram o horário
		if apenas_futuras:
			agora = timezone.localtime(timezone.now())
			hoje = agora.date()
			hora_atual = agora.time()

			queryset = queryset.filter(
				estado=SolicitacaoModel.EstadoSolicitacao.PENDENTE
			).filter(
				Q(dataPretendida__gt=hoje) |
				Q(dataPretendida=hoje, agendaId__horarioInicio__gt=hora_atual)
			)

		return queryset.order_by('-dataPretendida', '-agendaId__horarioInicio')
     
@extend_schema(
	summary="Listar todas as sessões do usuário autenticado (Sem Paginação)",
	description="Retorna a lista completa de todas as sessões associadas ao usuário logado, englobando tanto o papel de Tutor quanto o de Aprendiz, sem filtros restritivos ou paginação.",
	responses=SessaoSerializer(many=True),
	tags=['06. Sessões']
)
class TodasSessoesUsuarioViewSet(viewsets.ReadOnlyModelViewSet):
	serializer_class = SessaoSerializer
	permission_classes = [IsAuthenticated]
	pagination_class = None
	http_method_names = ['get']

	def get_queryset(self):
		user = self.request.user

		# Puxa todas as sessões onde o usuário é o aprendiz OU onde ele é o tutor cadastrado
		return SessaoModel.objects.filter(
			Q(usuarioId=user) | Q(tutorId__usuarioId=user)
		).select_related(
			'usuarioId', 
			'tutorId__usuarioId', 
			'areaId', 
			'especialidadeId'
		).order_by('-dataSessao', '-horarioInicio')
