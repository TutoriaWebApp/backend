from django.shortcuts import get_object_or_404
from drf_spectacular.utils import extend_schema
from rest_framework import viewsets, generics, status
from rest_framework.response import Response
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
	queryset = ConquistaModel.objects.all().order_by('pontos')
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
    http_method_names = ['get', 'post']

    def create(self, request, *args, **kwargs):
        usuario_id = request.data.get('usuarioId')
        conquista_id = request.data.get('conquistaId')

        if not usuario_id or not conquista_id:
            return Response(
                {"mensagem": "usuarioId e conquistaId são obrigatórios."},
                status=status.HTTP_400_BAD_REQUEST
            )

        # Busca ou cria o vínculo sem estourar o erro de UniqueTogetherValidator
        consegue, criado = consegueModel.objects.get_or_create(
            usuarioId_id=usuario_id,
            conquistaId_id=conquista_id
        )

        serializer = self.get_serializer(consegue)
        return Response(
            {
                "desbloqueadoAgora": criado,
                "dados": serializer.data
            },
            status=status.HTTP_201_CREATED if criado else status.HTTP_200_OK
        )

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

