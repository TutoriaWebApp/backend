from django.shortcuts import get_object_or_404
from drf_spectacular.utils import extend_schema
from rest_framework import viewsets, generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from project.models import *
from project.serializers import *


class ConquistaViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = ConquistaModel.objects.all().order_by('pontos')
    serializer_class = ConquistaSerializer

    @extend_schema(
        summary="Lista conquistas da plataforma",
        description="Este endpoint retorna a lista de todas as conquistas cadastradas no banco de dados, ordenadas por pontuação.",
        responses={200: ConquistaSerializer(many=True)},
        tags=['10. Conquistas']
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @extend_schema(
        summary="Detalha uma conquista por ID",
        description="Recebe o ID de uma conquista específica e retorna seus detalhes.",
        responses={200: ConquistaSerializer},
        tags=['10. Conquistas']
    )
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

@extend_schema(
	summary="Destrava conquista para um usuário",
	description="Este endpoint destrava uma conquista para um usuário. Recebe o ID do usuário a qual a conquista será destrava e o ID da conquista.",
	request=consegueSerializer,
	responses=consegueSerializer,
	tags=['10. Conquistas']
)
class consegueViewSet(viewsets.ModelViewSet):
    queryset = consegueModel.objects.all()
    serializer_class = consegueSerializer
    permission_classes = [IsAuthenticated]
    http_method_names = ['post']

    def create(self, request, *args, **kwargs):
        usuario_id = request.data.get('usuarioId')
        conquista_id = request.data.get('conquistaId')

        if not usuario_id or not conquista_id:
            return Response(
                {"mensagem": "usuarioId e conquistaId são obrigatórios."},
                status=status.HTTP_400_BAD_REQUEST
            )

        consegue, criado = consegueModel.objects.get_or_create(
            usuarioId_id=usuario_id,
            conquistaId_id=conquista_id
        )

        if criado:
            usuario = get_object_or_404(UsuarioModel, pk=usuario_id)
            conquista = get_object_or_404(ConquistaModel, pk=conquista_id)
            
            usuario.pontuacao = (usuario.pontuacao or 0) + conquista.pontos
            usuario.save(update_fields=['pontuacao'])

        serializer = self.get_serializer(consegue)
        return Response(
            {
                "desbloqueadoAgora": criado,
                "dados": serializer.data
            },
            status=status.HTTP_201_CREATED if criado else status.HTTP_200_OK
        )

@extend_schema(
	summary="Lista as conquistas destravadas pelo usuário",
	description="Este endpoint lista todas as conquistas destravadas pelo usuário, trazendo suas informações.",
	request=ConquistaUsuarioSerializer,
	responses=ConquistaUsuarioSerializer,
	tags=['10. Conquistas']
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

