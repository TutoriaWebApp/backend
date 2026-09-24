import datetime
from django.utils import timezone
from django.db import transaction
from django.db.models import F, Q, Exists, OuterRef
from rest_framework.filters import OrderingFilter
from drf_spectacular.utils import extend_schema, extend_schema_serializer, OpenApiExample, OpenApiParameter
from rest_framework import viewsets, status, serializers
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response

from project.models import *
from project.serializers import *

class AvaliacaoItemSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    nota = serializers.IntegerField()
    comentario = serializers.CharField(allow_blank=True, allow_null=True)
@extend_schema_serializer(
    examples=[
        OpenApiExample(
            'Exemplo de Avaliações Recebidas',
            value={
                "comoAprendiz": [
                    {
                        "id": 1,
                        "nota": 5,
                        "comentario": "Excelente pontualidade e engajamento durante a sessão."
                    }
                ],
                "comoTutor": [
                    {
                        "id": 10,
                        "nota": 5,
                        "comentario": "Ótima explicação, tirou todas as dúvidas com clareza."
                    }
                ]
            },
            response_only=True,
        )
    ]
)
class TodasAvaliacoesResponseSerializer(serializers.Serializer):
    comoAprendiz = AvaliacaoItemSerializer(many=True)
    comoTutor = AvaliacaoItemSerializer(many=True)

class AvaliacaoPagination(PageNumberPagination):
	page_size = 6
	page_size_query_param = 'page_size'  
	max_page_size = 50  

class AvaliacaoAprendizViewSet(viewsets.ModelViewSet):
	serializer_class = AvaliacaoAprendizSerializer
	permission_classes = [IsAuthenticated]
	pagination_class = AvaliacaoPagination 
	filter_backends = (OrderingFilter,)
	ordering_fields = ['nota']
	http_method_names = ['get', 'post']

	@extend_schema(
        summary="Lista as avaliações de aprendizes",
        description=(
            "Este endpoint lista todas as avaliações recebidas por aprendizes cadastradas na plataforma.\n\n"
            "Permite filtrar por aprendiz específico utilizando '?usuario=ID', ordenar as notas em ordem crescente ou decrescente "
            "e possui suporte a paginação."
        ),
        responses={200: AvaliacaoAprendizSerializer(many=True)},
        tags=['07. Avaliações'],
        parameters=[
            OpenApiParameter(
                name='usuario', 
                description='ID do Usuário (Aprendiz) para buscar os feedbacks recebidos sobre ele', 
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
	def list(self, request, *args, **kwargs):
		return super().list(request, *args, **kwargs)

	@extend_schema(
        summary="Detalha uma avaliação de aprendiz por ID",
        description="Recebe o ID de uma avaliação feita sobre um aprendiz e retorna suas informações detalhadas.",
        responses={200: AvaliacaoAprendizSerializer},
        tags=['07. Avaliações'],
        parameters=[]  # Remove os parâmetros de query da busca geral no GET por ID
    )
	def retrieve(self, request, *args, **kwargs):
		return super().retrieve(request, *args, **kwargs)

	@extend_schema(
        summary="Cria uma avaliação para um aprendiz",
        description=(
            "Permite cadastrar uma nova avaliação sobre a participação de um aprendiz em uma sessão de tutoria.\n\n"
            "Ao registrar a avaliação, o sistema bonifica o usuário com 50 pontos na plataforma."
        ),
        request=AvaliacaoAprendizSerializer,
        responses={201: AvaliacaoAprendizSerializer},
        tags=['07. Avaliações'],
        parameters=[] 
    )
	def create(self, request, *args, **kwargs):
		return super().create(request, *args, **kwargs)

	def get_queryset(self):
		agora = timezone.now()
		limite_48h = agora - datetime.timedelta(hours=48)
		tutor_avaliou_de_volta = AvaliacaoTutorModel.objects.filter(
			sessaoId=OuterRef('sessaoId')
		)
		queryset = AvaliacaoAprendizModel.objects.filter(
			Q(dataCriacao__lte=limite_48h) | Exists(tutor_avaliou_de_volta)
		).select_related(
			'usuarioId',
			'sessaoId',
			'sessaoId__tutorId__usuarioId',
			'sessaoId__areaId',
			'sessaoId__especialidadeId'
		)    

		usuario_id = self.request.query_params.get('usuario')
	
		if usuario_id is not None:
			queryset = queryset.filter(usuarioId=usuario_id)
		
		return queryset

	@transaction.atomic
	def perform_create(self, serializer):
		serializer.save()
		UsuarioModel.objects.filter(pk=self.request.user.pk).update(
			pontuacao=F('pontuacao') + 50
		)
	
@extend_schema(
	summary="Lista todas as avaliações do usuário autenticado",
	description=(
		"Retorna o conjunto completo de avaliações recebidas pelo usuário autenticado (tanto como aprendiz quanto como tutor) sem paginação."
	),    
	responses={200: TodasAvaliacoesResponseSerializer},
	tags=['07. Avaliações'],
)
class TodasAvaliacoesUsuarioViewSet(viewsets.ViewSet):
    permission_classes = [IsAuthenticated]

    def list(self, request):
        usuario = request.user

        avaliacoes_aprendiz = AvaliacaoAprendizModel.objects.filter(
            usuarioId=usuario
        ).values('id', 'nota', 'comentario')

        avaliacoes_tutor = AvaliacaoTutorModel.objects.filter(
            tutorId__usuarioId=usuario
        ).values('id', 'nota', 'comentario')

        return Response({
            'comoAprendiz': list(avaliacoes_aprendiz),
            'comoTutor': list(avaliacoes_tutor)
        }, status=status.HTTP_200_OK)

class AvaliacaoTutorViewSet(viewsets.ModelViewSet):
	serializer_class = AvaliacaoTutorSerializer
	permission_classes = [IsAuthenticated]
	pagination_class = AvaliacaoPagination
	filter_backends = (OrderingFilter,)
	ordering_fields = ['nota']	
	http_method_names = ['get', 'post']

	@extend_schema(
        summary="Lista as avaliações de tutores",
        description=(
            "Este endpoint lista todas as avaliações recebidas por tutores cadastradas na plataforma.\n\n"
            "Permite filtrar por ID do tutor, Área de Conhecimento, Especialidade, além de permitir ordenação por nota "
            "(crescente ou decrescente) e paginação dos resultados."
        ),
        responses={200: AvaliacaoTutorSerializer(many=True)},
        tags=['07. Avaliações'],
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
	def list(self, request, *args, **kwargs):
		return super().list(request, *args, **kwargs)

	@extend_schema(
        summary="Detalha uma avaliação de tutor por ID",
        description="Recebe o ID de uma avaliação de tutor e retorna suas informações detalhadas.",
        responses={200: AvaliacaoTutorSerializer},
        tags=['07. Avaliações'],
        parameters=[]  # Zera os parâmetros de query da busca geral no GET por ID
    )
	def retrieve(self, request, *args, **kwargs):
		return super().retrieve(request, *args, **kwargs)

	@extend_schema(
        summary="Cria uma avaliação para um tutor",
        description=(
            "Permite que um aprendiz registre uma avaliação sobre um tutor após a realização de uma sessão de tutoria.\n\n"
            "Ao registrar a avaliação, o usuário recebe uma bonificação de 50 pontos na plataforma."
        ),
        request=AvaliacaoTutorSerializer,
        responses={201: AvaliacaoTutorSerializer},
        tags=['07. Avaliações'],
        parameters=[]  # Zera os parâmetros de query para o POST
    )
	def create(self, request, *args, **kwargs):
		return super().create(request, *args, **kwargs)

	def get_queryset(self):
		agora = timezone.now()
		limite_48h = agora - datetime.timedelta(hours=48)
		aprendiz_avaliou_de_volta = AvaliacaoAprendizModel.objects.filter(
			sessaoId=OuterRef('sessaoId')
		)
		queryset = AvaliacaoTutorModel.objects.filter(
			Q(dataCriacao__lte=limite_48h) | Exists(aprendiz_avaliou_de_volta)
		).select_related(
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

	@transaction.atomic
	def perform_create(self, serializer):
		serializer.save()
		UsuarioModel.objects.filter(pk=self.request.user.pk).update(
			pontuacao=F('pontuacao') + 50
		)

@extend_schema(
	summary="Lista sessões pendentes de avaliação",
	description="Este endpoint retorna as sessões que o usuário participou (como aprendiz ou tutor) e que ainda não foram avaliadas por ele.",
	responses={200: SessaoPendenteAvaliacaoSerializer(many=True)},
	tags=['07. Avaliações']
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
			avaliacoes_tutor_sessao__isnull=False
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
				avaliacoes_aprendiz_sessao__isnull=False
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