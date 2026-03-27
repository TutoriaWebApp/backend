from datetime import timedelta
from django.db.models import Q
from django.utils import timezone
from drf_spectacular.utils import extend_schema
from rest_framework import viewsets, generics
from rest_framework.permissions import IsAuthenticated

from project.models import *
from project.serializers import *

@extend_schema(
	summary="Dados de Solicitação",
	description="Este endpoint retorna uma Solicitação",
	request=SolicitacaoSerializer,
	responses=SolicitacaoSerializer,
	tags=['Solicitação']
)
class SolicitacaoViewSet(viewsets.ModelViewSet):
	serializer_class = SolicitacaoSerializer
	permission_classes = [IsAuthenticated]
	http_method_names = ['get', 'post', 'delete']

	def get_queryset(self):
		user = UsuarioModel.objects.filter(email=self.request.user)[0].id
		print(user)
		return SolicitacaoModel.objects.\
		filter(Q(usuarioId=user) | Q(sessaoId__tutorId=user)).\
		distinct()

	def perform_create(self, serializer):
		logged_user = self.request.user
		dataCriacao = timezone.now()
		validade = dataCriacao + timedelta(hours=24)
		serializer.save(
			usuarioId=logged_user,
			dataCriacao=dataCriacao,
			validade=validade,
			estado=SolicitacaoModel.EstadoSolicitacao.PENDENTE
		)
