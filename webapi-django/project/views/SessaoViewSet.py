from drf_spectacular.utils import extend_schema
from rest_framework import viewsets, generics
from rest_framework.permissions import IsAuthenticated

from project.models import *
from project.serializers import *

@extend_schema(
	summary="Sessao",
	description="Este endpoint retorna Sessão",
	request=SessaoSerializer,
	responses=SessaoSerializer,
	tags=['Sessão']
)
class SessaoViewSet(viewsets.ModelViewSet):
	# queryset = SessaoModel.objects.all()
	serializer_class = SessaoSerializer
	permission_classes = [IsAuthenticated]
	http_method_names = ['get', 'post', 'delete', 'patch']

	def get_queryset(self):
		return SolicitacaoModel.objects.filter(usuarioId=self.request.user)
