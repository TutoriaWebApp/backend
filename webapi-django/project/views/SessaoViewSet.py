from drf_spectacular.utils import extend_schema
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from django.db.models import Q

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

	def get_queryset(self):
		return AgendaModel.objects.all()



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
	http_method_names = ['get', 'post', 'delete']

	def get_queryset(self):
		user = self.request.user
		return SolicitacaoModel.objects.filter(
			Q(usuarioId=user) | Q(agendaId__tutorId__usuarioId=user)
		).distinct()

	def perform_create(self, serializer):
		logged_user = self.request.user
		serializer.save(
			usuarioId=logged_user,
			estado=SolicitacaoModel.EstadoSolicitacao.PENDENTE
		)



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
	http_method_names = ['get', 'post', 'delete', 'patch']

	def get_queryset(self):
		user = self.request.user
		return SessaoModel.objects.filter(
			Q(usuarioId=user) | Q(tutorId__usuarioId=user)
		)
