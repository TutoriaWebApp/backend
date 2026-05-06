from drf_spectacular.utils import extend_schema
from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.db.models import Q

from rest_framework.exceptions import ValidationError

from project.models import *
from project.serializers import *

@extend_schema(
	summary="Agenda do Tutor",
	description="Este endpoint permite gerenciar os horários disponíveis (slots) de um tutor.",
	request=AgendaSerializer,
	responses=AgendaSerializer,
	tags=['05. Solicitar Sessão']
)
class AgendaViewSet(viewsets.ModelViewSet):
	queryset = AgendaModel.objects.all()
	serializer_class = AgendaSerializer
	permission_classes = [IsAuthenticated]
	http_method_names = ['get', 'post', 'delete']

	def get_queryset(self):
		return AgendaModel.objects.all()

	def create(self, request, *args, **kwargs):

		try:
			tutor = TutorModel.objects.get(usuarioId=self.request.user)
		except TutorModel.DoesNotExist:
			raise ValidationError({"mensagem": "Apenas tutores podem criar agendas."})

		data = request.data.copy()
		data['tutorId'] = tutor.id

		serializer = self.get_serializer(data=data)
		serializer.is_valid(raise_exception=True)

		self.perform_create(serializer)
		headers = self.get_success_headers(serializer.data)
		return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)




@extend_schema(
	summary="Dados de Solicitação",
	description="Este endpoint gerencia as solicitações de tutoria feitas por alunos.",
	request=SolicitacaoSerializer,
	responses=SolicitacaoSerializer,
	tags=['05. Solicitar Sessão']
)
class SolicitacaoViewSet(viewsets.ModelViewSet):
	serializer_class = SolicitacaoSerializer
	permission_classes = [IsAuthenticated]
	http_method_names = ['get', 'post', 'patch']

	def get_queryset(self):
		from django.utils import timezone
		import datetime

		user = self.request.user

		solicitacoes = SolicitacaoModel.objects.filter(
			Q(usuarioId=user) | Q(agendaId__tutorId__usuarioId=user)
		).distinct()

		agora = timezone.now()

		for sol in solicitacoes:
			if sol.validade:
				validade_delta = datetime.timedelta(
					hours=sol.validade.hour,
					minutes=sol.validade.minute,
					seconds=sol.validade.second
				)
				data_expiracao = sol.dataCriacao + validade_delta

				if agora > data_expiracao:
					sol.delete()

		return SolicitacaoModel.objects.filter(
			Q(usuarioId=user) | Q(agendaId__tutorId__usuarioId=user)
		).distinct()

	def perform_create(self, serializer):
		logged_user = self.request.user
		serializer.save(
			usuarioId=logged_user
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
			raise ValidationError({"mensagem": "Apenas o tutor responsável pode aceitar esta solicitação."})

		if solicitacao.estado == SolicitacaoModel.EstadoSolicitacao.RECORRENTE:
			solicitacao.recorrente = True
			solicitacao.estado = SolicitacaoModel.EstadoSolicitacao.ACEITO
			solicitacao.save()

			SessaoModel.objects.create(
				usuarioId=solicitacao.usuarioId,
				tutorId=solicitacao.agendaId.tutorId.id,
				areaId=solicitacao.areaId.id,
				especialidadeId=solicitacao.especialidadeId.id,
				dataSessao=solicitacao.dataPretendida,
				horaInicio=solicitacao.agendaId.horarioInicio,
				horaFim=solicitacao.agendaId.horarioFim
			)
			return

		if solicitacao.estado != SolicitacaoModel.EstadoSolicitacao.PENDENTE:

			raise ValidationError({"mensagem": "Apenas solicitações pendentes podem ser aceitas."})
		solicitacao.estado = SolicitacaoModel.EstadoSolicitacao.ACEITO
		solicitacao.save()

		SessaoModel.objects.create(
			usuarioId=solicitacao.usuarioId,
			tutorId=solicitacao.agendaId.tutorId,
			areaId=solicitacao.areaId,
			especialidadeId=solicitacao.especialidadeId,
			dataSessao=solicitacao.dataPretendida,
			horaInicio=solicitacao.agendaId.horarioInicio,
			horaFim=solicitacao.agendaId.horarioFim
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
			raise ValidationError({"mensagem": "Apenas o tutor responsável pode recusar esta solicitação."})

		if solicitacao.estado not in [SolicitacaoModel.EstadoSolicitacao.PENDENTE, SolicitacaoModel.EstadoSolicitacao.RECORRENTE]:
			raise ValidationError({"mensagem": "Apenas solicitações pendentes ou recorrentes podem ser recusadas."})

		solicitacao.estado = SolicitacaoModel.EstadoSolicitacao.RECUSADO
		solicitacao.save()



@extend_schema(
	summary="Sessão de Tutoria",
	description="Este endpoint gerencia as sessões de tutoria confirmadas.",
	request=SessaoSerializer,
	responses=SessaoSerializer,
	tags=['05. Solicitar Sessão']
)
class SessaoViewSet(viewsets.ModelViewSet):
	serializer_class = SessaoSerializer
	permission_classes = [IsAuthenticated]
	http_method_names = ['get']

	def get_queryset(self):
		user = self.request.user
		return SessaoModel.objects.filter(
			Q(usuarioId=user) | Q(tutorId__usuarioId=user)
		)
