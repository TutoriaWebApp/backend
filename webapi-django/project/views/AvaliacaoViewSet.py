from rest_framework.filters import OrderingFilter
from drf_spectacular.utils import extend_schema, OpenApiParameter
from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from django.utils import timezone

from project.models import *
from project.serializers import *

class AvaliacaoPagination(PageNumberPagination):
    page_size = 6
    page_size_query_param = 'page_size'  
    max_page_size = 50  

@extend_schema(
    summary="Avaliação do Aprendiz",
	description=(
        "Este endpoint permite gerenciar e listar as avaliações feitas pelos aprendizes sobre as sessões. "
		"Utilize o parâmetro '?usuario=ID' para filtrar as avaliações e notas recebidas por um aprendiz específico."    
	),    
	request=AvaliacaoAprendizSerializer,
    responses=AvaliacaoAprendizSerializer,
    tags=['06. Avaliações'],
    parameters=[
		OpenApiParameter(
            name='usuario', 
            description='ID do Usuário (Aprendiz) para buscar o feedback recebido sobre ele', 
            required=False, 
            type=int
        ),
		OpenApiParameter(
            name='area', 
            description='ID da Área de Conhecimento vinculada à sessão para filtrar', 
            required=False, 
            type=int
        ),
        OpenApiParameter(
            name='especialidade', 
            description='ID da Especialidade vinculada à sessão para filtrar', 
            required=False, 
            type=int
        ),
		OpenApiParameter(
            name='ordering', 
            description="Ordenação por nota: use 'nota' para crescente (menores notas primeiro) ou '-nota' para decrescente (maiores notas primeiro).", 
            required=False, 
            type=str
        ),
        OpenApiParameter(name='page', description='Número da página', required=False, type=int),
        OpenApiParameter(name='page_size', description='Quantidade de comentários por página (ex: 6, 12, 18)', required=False, type=int),
    ]
)
class AvaliacaoAprendizViewSet(viewsets.ModelViewSet):
	serializer_class = AvaliacaoAprendizSerializer
	permission_classes = [IsAuthenticated]
	pagination_class = AvaliacaoPagination 
	filter_backends = (OrderingFilter,)
	ordering_fields = ['nota']
	http_method_names = ['get', 'post']

	def get_queryset(self):
		queryset = AvaliacaoAprendizModel.objects.all().select_related(
            'usuarioId',
            'sessaoId',
            'sessaoId__tutorId__usuarioId',
            'sessaoId__areaId',
            'sessaoId__especialidadeId'
        )        

		usuario_id = self.request.query_params.get('usuario')
		area_id = self.request.query_params.get('area')
		especialidade_id = self.request.query_params.get('especialidade')        
	
		if usuario_id is not None:
			queryset = queryset.filter(usuarioId=usuario_id)
		
		if area_id is not None:
			queryset = queryset.filter(sessaoId__areaId=area_id)

		if especialidade_id is not None:
			queryset = queryset.filter(sessaoId__especialidadeId=especialidade_id)	
		
		return queryset
	
@extend_schema(
    summary="Avaliação do Tutor",
    description="Este endpoint permite gerenciar e listar as avaliações feitas sobre os tutores após as sessões de forma paginada.",
    request=AvaliacaoTutorSerializer,
    responses=AvaliacaoTutorSerializer,
    tags=['06. Avaliações'],
    parameters=[
		OpenApiParameter(
            name='tutor', 
            description='ID do Tutor para buscar o feedback/reputação recebido por ele', 
            required=False, 
            type=int
        ),
		OpenApiParameter(
            name='area', 
            description='ID da Área de Conhecimento vinculada à sessão para filtrar', 
            required=False, 
            type=int
        ),
        OpenApiParameter(
            name='especialidade', 
            description='ID da Especialidade vinculada à sessão para filtrar', 
            required=False, 
            type=int
        ),
		OpenApiParameter(
            name='ordering', 
            description="Ordenação por nota: use 'nota' para crescente (menores notas primeiro) ou '-nota' para decrescente (maiores notas primeiro).", 
            required=False, 
            type=str
        ),
        OpenApiParameter(name='page', description='Número da página', required=False, type=int),
        OpenApiParameter(name='page_size', description='Quantidade de comentários por página (ex: 6, 12, 18)', required=False, type=int),
    ]
)
class AvaliacaoTutorViewSet(viewsets.ModelViewSet):
	serializer_class = AvaliacaoTutorSerializer
	permission_classes = [IsAuthenticated]
	pagination_class = AvaliacaoPagination
	filter_backends = (OrderingFilter,)
	ordering_fields = ['nota']	
	http_method_names = ['get', 'post']

	def get_queryset(self):
		queryset = AvaliacaoTutorModel.objects.all().select_related(
            'sessaoId__usuarioId',
            'sessaoId__areaId',
            'sessaoId__especialidadeId'
        )        

		tutor_id = self.request.query_params.get('tutor')
		area_id = self.request.query_params.get('area')
		especialidade_id = self.request.query_params.get('especialidade')        
		
		if tutor_id is not None:
			queryset = queryset.filter(tutorId=tutor_id)

		if area_id is not None:
			queryset = queryset.filter(sessaoId__areaId=area_id)

		if especialidade_id is not None:
			queryset = queryset.filter(sessaoId__especialidadeId=especialidade_id)
            
		return queryset

@extend_schema(
	summary="Sessões Pendentes de Avaliação",
	description="Retorna as sessões que o usuário participou (como aprendiz ou tutor) e que ainda não foram avaliadas por ele.",
	responses={200: SessaoPendenteAvaliacaoSerializer(many=True)},
	tags=['06. Avaliações']
)
class PendenteAvaliacaoView(APIView):
	permission_classes = [IsAuthenticated]

	def get(self, request):
		usuario = request.user
		hoje = timezone.now().date()
		agora = timezone.now().time()

		sessoes_como_aprendiz = SessaoModel.objects.filter(
			usuarioId=usuario,
		).exclude(
			avaliacoes_aprendiz_sessao__usuarioId=usuario
        ).select_related(
            'usuarioId',
            'tutorId__usuarioId',
            'areaId',
            'especialidadeId'
        )

		try:
			tutor = TutorModel.objects.get(usuarioId=usuario)
			sessoes_como_tutor = SessaoModel.objects.filter(
                tutorId=tutor,
            ).exclude(
                avaliacoes_tutor_sessao__tutorId=tutor
            ).select_related(
                'usuarioId',
                'tutorId__usuarioId',
                'areaId',
                'especialidadeId'
            )
		except TutorModel.DoesNotExist:
			sessoes_como_tutor = SessaoModel.objects.none()

		pendentes = []

		for s in sessoes_como_aprendiz:
			if s.dataSessao < hoje or (s.dataSessao == hoje and s.horarioFim <= agora):
				s.tipoPendente = 'APRENDIZ' 
				pendentes.append(s)

		for s in sessoes_como_tutor:
			if s.dataSessao < hoje or (s.dataSessao == hoje and s.horarioFim <= agora):
				s.tipoPendente = 'TUTOR' 
				pendentes.append(s)

		serializer = SessaoPendenteAvaliacaoSerializer(pendentes, many=True, context={'request': request})
		return Response(serializer.data, status=status.HTTP_200_OK)