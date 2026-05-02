from drf_spectacular.utils import extend_schema
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import ValidationError

from project.models import *
from project.serializers import *

@extend_schema(
	summary="Usuário tutor",
	description="Este endpoint retorna informações sobre os tutores cadastrados na plataforma, incluindo suas especialidades",
	request=TutorSerializer,
	responses=TutorSerializer,
	tags=['03. Tutor']
)
class TutorViewSet(viewsets.ModelViewSet):
	queryset = TutorModel.objects.all()
	serializer_class = TutorSerializer
	permission_classes = [IsAuthenticated]
	http_method_names = ['get', 'post']

	def perform_create(self, serializer):
		if TutorModel.objects.filter(usuarioId=self.request.user).exists():
			raise ValidationError({"detail": "Este usuário já está cadastrado como tutor."})
		serializer.save(usuarioId=self.request.user)



@extend_schema(
	summary="Áreas de conhecimento",
	description="Este endpoint permite listar, criar, visualizar, atualizar e deletar áreas de conhecimento",
	request=AreaSerializer,
	responses=AreaSerializer,
	tags=['04. Areas']
)
class AreaViewSet(viewsets.ModelViewSet):
	queryset = AreaModel.objects.all()
	serializer_class = AreaSerializer
	http_method_names = ['get']



@extend_schema(
	summary="Especialidades",
	description="Este endpoint permite listar, criar, visualizar, atualizar e deletar especialidades",
	request=EspecialidadeSerializer,
	responses=EspecialidadeSerializer,
	tags=['04. Areas']
)
class EspecialidadeViewSet(viewsets.ModelViewSet):
	queryset = EspecialidadeModel.objects.all()
	serializer_class = EspecialidadeSerializer
	http_method_names = ['get']



@extend_schema(
	summary="Relacionamento Tutor-Especialidade (Contém)",
	description="Este endpoint permite gerenciar quais especialidades um tutor possui",
	request=ContemSerializer,
	responses=ContemSerializer,
	tags=['04. Areas']
)
class ContemViewSet(viewsets.ModelViewSet):
	queryset = ContemModel.objects.all()
	serializer_class = ContemSerializer
	http_method_names = ['get', 'post', 'delete']
