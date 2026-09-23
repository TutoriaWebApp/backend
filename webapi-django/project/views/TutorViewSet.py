from drf_spectacular.utils import extend_schema, OpenApiParameter
from rest_framework import viewsets
from django.db.models import Count

from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.pagination import PageNumberPagination
from rest_framework.exceptions import ValidationError

from django_filters import rest_framework as filters

from project.models import *
from project.serializers import *
from project.utils import GeoLocalizacaoUtil


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


class TutorViewSet(viewsets.ModelViewSet):
    queryset = TutorModel.objects.all()
    serializer_class = TutorSerializer
    permission_classes = [IsAuthenticated]
    http_method_names = ['get', 'post']

    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = TutorFilter
    pagination_class = TutorPagination

    @extend_schema(
        summary="Lista todos os tutores",
        description=(
            "Este endpoint retorna informações sobre os tutores cadastrados na plataforma, "
            "permitindo filtragem por área, especialidade e raio de distância em quilômetros a partir da localização do usuário logado.\n\n"
            "É possível também ordenar os resultados por nota como tutor e quantidade de tutorias.\n\n"
            "Os resultados são paginados, podendo-se escolher a quantidade de resultados por página."
        ),
        responses={200: TutorSerializer(many=True)},
        tags=['03. Tutor'],
        parameters=[
            OpenApiParameter(
                name='area', description='ID da Área de Conhecimento para filtrar', required=False, type=int),
            OpenApiParameter(
                name='especialidade', description='ID da Especialidade para filtrar', required=False, type=int),
            OpenApiParameter(
                name='ordenar_nota',
                description="Ordenação por nota. Use 'asc' (menores notas primeiro) ou 'desc' (maiores notas primeiro).",
                required=False,
                type=str
            ),
            OpenApiParameter(
                name='ordenar_tutorias',
                description="Ordenação por quantidade de tutorias realizadas. Use 'asc' (menos tutorias) ou 'desc' (mais tutorias).",
                required=False,
                type=str
            ),
            OpenApiParameter(
                name='raio',
                description='Raio máximo de busca (em quilômetros) a partir da localização do usuário logado.',
                required=False,
                type=float
            ),
            OpenApiParameter(
                name='page', description='Número da página', required=False, type=int),
        ]
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @extend_schema(
        summary="Exibe detalhes de um tutor específico",
        description="Recebe o ID do tutor e retorna suas informações detalhadas.",
        responses={200: TutorSerializer},
        tags=['03. Tutor'],
        parameters=[]  
    )
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @extend_schema(
        summary="Cadastra o usuário logado como Tutor",
        description="Torna o usuário autenticado em um tutor na plataforma. Se ele já for tutor, retorna erro de validação.",
        request=TutorSerializer,
        responses={201: TutorSerializer},
        tags=['03. Tutor'],
        parameters=[] 
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    def get_queryset(self):
        user = self.request.user

        queryset = TutorModel.objects.all().select_related('usuarioId').prefetch_related(
            'especialidades',
            'especialidades__areaId'
        ).annotate(
            qtd_tutorias_realizadas=Count('sessoes')
        )

        if user and user.is_authenticated:
            queryset = queryset.exclude(usuarioId=user)

            raio_param = (
                self.request.query_params.get('raio') or
                self.request.query_params.get('raio_km') or
                self.request.query_params.get('distancia') or
                self.request.query_params.get('distancia_km')
            )
            if raio_param is not None:
                try:
                    raio = float(raio_param)
                except (ValueError, TypeError):
                    raise ValidationError(
                        {"raio": "O parâmetro de raio/distância deve ser um número válido em quilômetros (Km)."})

                user_loc = getattr(user, 'localizacao', None)
                if not user_loc:
                    return queryset.none()

                try:
                    from django.contrib.gis.measure import D
                    qs_test = queryset.filter(
                        usuarioId__localizacao__distance_lte=(user_loc, D(km=raio)))
                    qs_test.exists()
                    queryset = qs_test
                except Exception:
                    valid_tutor_ids = [
                        t.id for t in queryset
                        if GeoLocalizacaoUtil.haversine_distance(user_loc, getattr(t.usuarioId, 'localizacao', None)) <= raio
                    ]
                    queryset = queryset.filter(id__in=valid_tutor_ids)

        ordem_nota = self.request.query_params.get('ordenar_nota', '').lower()
        ordem_tutorias = self.request.query_params.get(
            'ordenar_tutorias', '').lower()

        order_by_fields = []

        if ordem_nota == 'asc':
            order_by_fields.append('notaAvaliacao')
        elif ordem_nota == 'desc':
            order_by_fields.append('-notaAvaliacao')

        if ordem_tutorias == 'asc':
            order_by_fields.append('qtd_tutorias_realizadas')
        elif ordem_tutorias == 'desc':
            order_by_fields.append('-qtd_tutorias_realizadas')

        if order_by_fields:
            queryset = queryset.order_by(*order_by_fields)

        return queryset

    def perform_create(self, serializer):
        if TutorModel.objects.filter(usuarioId=self.request.user).exists():
            raise ValidationError(
                {"mensagem": "Este usuário já está cadastrado como tutor."})
        serializer.save(usuarioId=self.request.user)

class AreaViewSet(viewsets.ModelViewSet):
    queryset = AreaModel.objects.all().order_by('nomeArea')
    serializer_class = AreaSerializer
    http_method_names = ['get']

    @extend_schema(
        summary="Lista áreas de conhecimento",
        description="Este endpoint lista todas as áreas de conhecimento cadastradas no banco de dados, trazendo seu ID e seu nome, em ordem alfabética.",
        responses={200: AreaSerializer(many=True)},
        tags=['04. Areas']
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @extend_schema(
        summary="Detalha área de conhecimento por ID",
        description="Este endpoint recebe o ID de uma área de conhecimento e retorna suas informações detalhadas.",
        responses={200: AreaSerializer},
        tags=['04. Areas']
    )
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)


class EspecialidadeFilter(filters.FilterSet):
    # Cria o filtro 'areaId' para trazer as especialidades de uma área específica
    area = filters.NumberFilter(field_name='areaId', lookup_expr='exact')

    class Meta:
        model = EspecialidadeModel
        fields = ['area']


class EspecialidadeViewSet(viewsets.ModelViewSet):
    queryset = EspecialidadeModel.objects.all().order_by('nomeEspecialidade')
    serializer_class = EspecialidadeSerializer
    http_method_names = ['get']

    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = EspecialidadeFilter

    @extend_schema(
        summary="Lista especialidades",
        description=(
            "Este endpoint lista todas as especialidades cadastradas no banco de dados.\n\n"
            "É possível passar o parâmetro 'area', cujo valor é o ID de uma área de conhecimento "
            "cadastrada, para buscar todas as especialidades associadas a essa área específica."
        ),
        responses={200: EspecialidadeSerializer(many=True)},
        tags=['04. Areas'],
        parameters=[
            OpenApiParameter(
                name='area',
                description='ID da Área de Conhecimento para listar suas especialidades',
                required=False,
                type=int
            ),
        ]
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @extend_schema(
        summary="Detalha especialidade por ID",
        description="Este endpoint recebe o ID de uma especialidade e retorna suas informações detalhadas.",
        responses={200: EspecialidadeSerializer},
        tags=['04. Areas'],
        parameters=[] 
    )
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    def get_queryset(self):
        return EspecialidadeModel.objects.all().select_related('areaId')


class ContemViewSet(viewsets.ModelViewSet):
    queryset = ContemModel.objects.all()
    serializer_class = ContemSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    http_method_names = ['get', 'post', 'delete']

    @extend_schema(
        summary="Lista as especialidades associadas aos tutores",
        description="Retorna a lista completa de vínculos entre tutores e suas respectivas especialidades cadastradas.",
        responses={200: ContemSerializer(many=True)},
        tags=['04. Areas']
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @extend_schema(
        summary="Detalha um registro de relacionamento tutor-especialidade por ID",
        description="Recebe o ID do vínculo de especialidade e retorna os detalhes da associação.",
        responses={200: ContemSerializer},
        tags=['04. Areas']
    )
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @extend_schema(
        summary="Associa uma nova especialidade ao tutor logado",
        description="Permite que o tutor autenticado adicione uma nova especialidade ao seu perfil. Apenas usuários cadastrados como tutores podem realizar esta ação.",
        request=ContemSerializer,
        responses={201: ContemSerializer},
        tags=['04. Areas']
    )
    def create(self, request, *args, **kwargs):
        from rest_framework import status
        from rest_framework.response import Response

        try:
            tutor = TutorModel.objects.get(usuarioId=request.user)
        except TutorModel.DoesNotExist:
            raise ValidationError(
                {"mensagem": "Apenas tutores podem adicionar especialidades."})

        data = request.data.copy()
        data['tutorId'] = tutor.id

        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    @extend_schema(
        summary="Remove uma especialidade do tutor",
        description="Remove a associação de uma especialidade do perfil do tutor com base no ID do relacionamento tutor-especialidade fornecido.",
        responses={204: None},
        tags=['04. Areas']
    )
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)