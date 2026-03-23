from datetime import timedelta
from django.utils import timezone
from rest_framework import viewsets, generics
from rest_framework.permissions import IsAuthenticated

from project.models import *
from project.serializers import *

class SolicitacaoViewSet(viewsets.ModelViewSet):
	queryset = SolicitacaoModel.objects.all()
	serializer_class = SolicitacaoSerializer
	permission_classes = [IsAuthenticated]

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
