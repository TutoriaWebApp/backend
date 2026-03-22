from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.exceptions import InvalidToken, AuthenticationFailed

class WebTutoriaJWTAuthentication(JWTAuthentication):
	def authenticate(self, request):
		token = request.COOKIES.get('access_token')

		if token is None:
			return None

		try:
			token_valido = self.get_validated_token(token)
			usuario = self.get_user(token_valido)
			return usuario, token_valido
		except (InvalidToken, AuthenticationFailed):
			return None
