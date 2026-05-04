from drf_spectacular.extensions import OpenApiAuthenticationExtension
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

class WebTutoriaJWTScheme(OpenApiAuthenticationExtension):
	target_class = WebTutoriaJWTAuthentication  # A sua classe customizada
	name = 'WebTutoriaAuth'  # Um nome único para o esquema no Swagger

	def get_security_definition(self, auto_schema):
		return {
			'type': 'apiKey',
			'in': 'cookie',
			'name': 'access_token',
			'description': 'Autenticação baseada em HttpOnly Cookies (access_token).'
		}
