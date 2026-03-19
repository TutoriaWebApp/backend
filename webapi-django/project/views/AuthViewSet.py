from django.contrib.auth import authenticate
from django.contrib.auth.models import update_last_login
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes, force_str
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.core.mail import send_mail
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.exceptions import TokenError
from rest_framework_simplejwt.tokens import RefreshToken

from config.settings import EMAIL_HOST_USER
from project.models.Usuario import Usuario

class LogInView(APIView):
	permission_classes = [AllowAny]
	def post(self, request):

		username = request.data.get('username')
		password = request.data.get('password')

		user = authenticate(username=username, password=password)

		if user is None:
			return Response({"Credenciais inválidas"}, status=404)

		refresh = RefreshToken.for_user(user)

		response = Response({"mensagem": "Login com sucesso"}, status=200)

		response.set_cookie(
			key='access_token',
			value=str(refresh.access_token),
			httponly=True,
			secure=True,
			samesite='Lax'
		)

		response.set_cookie(
			key='refresh_token',
			value=str(refresh),
			httponly=True,
			secure=False,
			samesite='Lax'
		)
		return response

class LoginRefreshView(APIView):
	permission_classes = [AllowAny]
	def post(self, request):
		token = request.COOKIES.get('refresh_token')

		if not token:
			return Response({"mensagem": "Não foi possível encontrar Token de Autenticação"}, status=401)

		try:
			refresh = RefreshToken(token)
			response = Response({"mensagem": "Token renovado com sucesso"}, status=200)

			response.set_cookie(
				key='access_token',
				value=str(refresh.access_token),
				httponly=True,
				secure=False,
				samesite='Lax'
			)
			return response

		except TokenError:
			return Response({"mensagem": "Token inválido ou expirado"}, status=401)

class LogOutView(APIView):
	permission_classes = [AllowAny]
	def post(self, request):
		response = Response({"mensagem": "Logout realizado com sucesso"}, status=200)
		response.delete_cookie('access_token')
		response.delete_cookie('refresh_token')
		return response

class PasswordResetView(APIView):
	permission_classes = [AllowAny]
	def post(self, request):
		email = request.data.get('email')
		user = Usuario.objects.filter(email=email).first()

		print(f"Sending email to: {email}")
		if user:
			token = default_token_generator.make_token(user)
			uid = urlsafe_base64_encode(force_bytes(user.pk))

			reset_url = f"http://localhost:3000/reset-password/{uid}/{token}"

			print(f'De: {EMAIL_HOST_USER}')
			print(f'Para: {user.nomePerfil} {email}')
			send_mail(
				subject='WebTutoria - Recuperação de Senha',
				message=f'Prezado(a) {user.nomePerfil}, clique no no link para redefinir a sua senha: {reset_url}',
				recipient_list=[email],
				from_email="webapp.tutoria@gmail.com",
				fail_silently=False,
			)

		return Response({"mensagem": "Se este e-mail estiver cadastrado, um link será enviado para a recuperação de sua senha"}, status=200)

class PasswordResetConfirmView(APIView):
	permission_classes = [AllowAny]
	def post(self, request):
		uidb64 = request.data.get('uid')
		token = request.data.get('token')
		new_password = request.data.get('new_password')

		try:
			uid = force_str(urlsafe_base64_decode(uidb64))
			user = Usuario.objects.get(pk=uid)
		except (TypeError, ValueError, OverflowError, Usuario.DoesNotExist):
			user = None

		if user is None or not default_token_generator.check_token(user, token):
			return Response({"mensagem": "Link inválido ou experido"}, status=400)

		update_last_login(None, user)
		user.set_password(new_password)
		user.save()

		return Response({"mensagem": "Senha alterada com sucesso!"}, status=200)
