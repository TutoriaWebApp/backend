from datetime import timedelta
from django.utils import timezone
from django.db.models import Count
from drf_spectacular.utils import extend_schema
from rest_framework import viewsets, generics, status
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from project.models import *
from project.serializers import *


@extend_schema(
	summary="Lista Usuário da plataforma",
	description="Este endpoint lista todos os usuários préviamente cadastrado na plataforma",
	request=UsuarioPublicoSerializer,
	responses=UsuarioPublicoSerializer,
	tags=['02. Usuário']
)
class UsuarioViewSet(viewsets.ModelViewSet):
	queryset = UsuarioModel.objects.all()
	serializer_class = UsuarioPublicoSerializer
	http_method_names = ['get']

	def get_queryset(self):
		return UsuarioModel.objects.all().select_related('tutormodel').annotate(
            qtd_avaliacoes_aprendiz=Count('avaliacoes_aprendiz')
        )


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

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if not serializer.is_valid():
            errors = serializer.errors
            
            if 'email' in errors:
                email_err = errors['email']
                msg = email_err[0] if isinstance(email_err, list) else str(email_err)
                return Response(
                    {"message": "Já existe uma conta cadastrada com esse e-mail!" if "already exists" in str(msg) or "Já existe" in str(msg) else str(msg)}, 
                    status=status.HTTP_400_BAD_REQUEST
                )

            primeiro_campo = next(iter(errors))
            primeiro_erro = errors[primeiro_campo]
            msg = primeiro_erro[0] if isinstance(primeiro_erro, list) else str(primeiro_erro)
            return Response({"message": str(msg)}, status=status.HTTP_400_BAD_REQUEST)

        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
@extend_schema(
	summary="Exibe/edita informações sobre o Usuário logado",
	description="Este endpoint exibe/edita um usuário cadastrado na plataforma",
	request=UsuarioSerializer,
	responses=UsuarioSerializer,
	tags=['02. Usuário']
)
class UsuarioPerfilLogadoView(APIView):
	permission_classes = [IsAuthenticated]
	serializer_class = UsuarioSerializer
	http_method_names = ['get', 'patch']

	def get(self, request):
		user = UsuarioModel.objects.annotate(
			qtd_avaliacoes_aprendiz=Count('avaliacoes_aprendiz')
		).get(pk=request.user.pk)

		try:
			serializer = UsuarioSerializer(user, context={'request': request})
		except Exception as err:
			return Response({'mensagem': str(err)}, status=400)
		return Response(serializer.data, status=200)

	def patch(self, request):
		try:
			serialiazer = UsuarioSerializer(request.user, request.data, partial=True, context={'request': request})
			if not serialiazer.is_valid():
				return Response({'mensagem': 'Serializer não é válido', 'errors': serialiazer.errors}, status=400)
			serialiazer.save()
		except Exception as err:
			return Response({'mensagem': 'Não foi possível realizar alterações para o usuário', 'erro': f'{err}'}, status=400)
		return Response(serialiazer.data, status=200)



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

