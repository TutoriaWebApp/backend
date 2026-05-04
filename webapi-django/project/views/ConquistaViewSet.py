from django.shortcuts import get_object_or_404
from drf_spectacular.utils import extend_schema
from rest_framework import viewsets, generics
from rest_framework.permissions import IsAuthenticated

from project.models import *
from project.serializers import *

@extend_schema(
	summary="Lista conquistas da platafoma",
	description="Este endpoint retorna uma lista com todas as conquistas exibidas na plataforma",
	request=ConquistaSerializer,
	responses=ConquistaSerializer,
	tags=['Conquistas']
)
class ConquistaViewSet(viewsets.ReadOnlyModelViewSet):
	queryset = ConquistaModel.objects.all()
	serializer_class = ConquistaSerializer

@extend_schema(
	summary="Confirma a alteração de senha",
	description="Este endpoint recebe uid, token e a nova senha. Caso o uid e o token sejam válidos, a senha é alterada",
	request=consegueSerializer,
	responses=consegueSerializer,
	tags=['Conquistas']
)
class consegueViewSet(viewsets.ModelViewSet):
	queryset = consegueModel.objects.all()
	serializer_class = consegueSerializer
	permission_classes = [IsAuthenticated]
	http_method_names = ['get']

@extend_schema(
	summary="Confirma a alteração de senha",
	description="Este endpoint recebe uid, token e a nova senha. Caso o uid e o token sejam válidos, a senha é alterada",
	request=ConquistaUsuarioSerializer,
	responses=ConquistaUsuarioSerializer,
	tags=['Conquistas']
)
class Usuario_conseguiu_ConquistaView(generics.ListAPIView):
	serializer_class = ConquistaUsuarioSerializer
	permission_classes = [IsAuthenticated]
	http_method_names = ['get', 'post']

	def get_queryset(self):
		usuarioId = self.kwargs['usuarioId']
		get_object_or_404(UsuarioModel, pk=usuarioId)
		conquistas_list = ConquistaModel.objects.filter(usuarios__pk=usuarioId)
		return conquistas_list

