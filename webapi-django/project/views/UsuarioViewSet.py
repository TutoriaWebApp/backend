from datetime import timedelta
from django.utils import timezone
from drf_spectacular.utils import extend_schema
from rest_framework import viewsets, generics
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from project.models import *
from project.serializers import *

@extend_schema(
	summary="Lista Usuário da plataforma",
	description="Este endpoint lista todos os usuários préviamente cadastrado na plataforma",
	request=UsuarioSerializer,
	responses=UsuarioSerializer,
	tags=['02. Usuário']
)
class UsuarioViewSet(viewsets.ModelViewSet):
	queryset = UsuarioModel.objects.all()
	serializer_class = UsuarioSerializer
	http_method_names = ['get']



@extend_schema(
	summary="Cadastro de Usuário",
	description="Este endpoint cadastra um usuário na plataforma",
	request=UsuarioRegistroSerializer,
	responses=UsuarioRegistroSerializer,
	tags=['02. Usuário']
)
class UsuarioRegistroView(generics.CreateAPIView):
	queryset = UsuarioModel.objects.all()
	serializer_class = UsuarioRegistroSerializer
	permission_classes = [AllowAny]
	http_method_names = ['post']



@extend_schema(
	summary="Altera a senha",
	description="Este endpoint é para confirmar a senha antiga, antes de alterar a senha do Usuário",
	request=UsuarioAlteraSenhaSerializer,
	responses=UsuarioAlteraSenhaSerializer,
	tags=['02. Usuário']
)
class UsuarioAlteraSenhaView(APIView):
	permission_classes = [IsAuthenticated] # Obrigatório estar logado

	def post(self, request, *args, **kwargs):
		serializer = UsuarioAlteraSenhaSerializer(data=request.data, context={'request': request})

		if not serializer.is_valid():
			return Response(serializer.errors, status=400)

		user = request.user
		user.set_password(serializer.validated_data['senhaAtual'])
		user.save()

		return Response({"message": "Senha alterada com sucesso!"}, status=200)

