from drf_spectacular.utils import extend_schema, OpenApiParameter
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.pagination import PageNumberPagination
from rest_framework.exceptions import ValidationError

from django_filters import rest_framework as filters

from project.models import *
from project.serializers import *


class TutorPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 50


class TutorFilter(filters.FilterSet):
    # Filtra buscando o ID da área através das especialidades que o tutor contém
    area = filters.NumberFilter(
        field_name='especialidades__areaId', lookup_expr='exact')
    # Filtra buscando o ID da especialidade diretamente
    especialidade = filters.NumberFilter(
        field_name='especialidades', lookup_expr='exact')

    class Meta:
        model = TutorModel
        fields = ['area', 'especialidade']


@extend_schema(
    summary="Usuário tutor",
    description="Este endpoint retorna informações sobre os tutores cadastrados na plataforma, filtrados por área/especialidade e paginados.",
    request=TutorSerializer,
    responses=TutorSerializer,
    tags=['03. Tutor'],
    # Adiciona a documentação dos parâmetros de filtro no Swagger/Spectacular
    parameters=[
        OpenApiParameter(
            name='area', description='ID da Área de Conhecimento para filtrar', required=False, type=int),
        OpenApiParameter(
            name='especialidade', description='ID da Especialidade para filtrar', required=False, type=int),
        OpenApiParameter(
            name='page', description='Número da página', required=False, type=int),
    ]
)
class TutorViewSet(viewsets.ModelViewSet):
	queryset = TutorModel.objects.all()
	serializer_class = TutorSerializer
	permission_classes = [IsAuthenticated]
	http_method_names = ['get', 'post']

	# Configura os backends de filtro e paginação do DRF
	filter_backends = (filters.DjangoFilterBackend,)
	filterset_class = TutorFilter
	pagination_class = TutorPagination

	def get_queryset(self):
		return TutorModel.objects.all().select_related('usuarioId').prefetch_related('especialidades', 'especialidades__areaId')

	def perform_create(self, serializer):
		if TutorModel.objects.filter(usuarioId=self.request.user).exists():
			raise ValidationError({"mensagem": "Este usuário já está cadastrado como tutor."})
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
	permission_classes = [IsAuthenticatedOrReadOnly]
	http_method_names = ['get', 'post', 'delete']

	def create(self, request, *args, **kwargs):
		from rest_framework import status
		from rest_framework.response import Response

		try:
			tutor = TutorModel.objects.get(usuarioId=request.user)
		except TutorModel.DoesNotExist:
			raise ValidationError({"mensagem": "Apenas tutores podem adicionar especialidades."})

		data = request.data.copy()
		data['tutorId'] = tutor.id

		serializer = self.get_serializer(data=data)
		serializer.is_valid(raise_exception=True)
		self.perform_create(serializer)
		headers = self.get_success_headers(serializer.data)
		return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
