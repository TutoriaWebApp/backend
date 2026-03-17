from rest_framework_simplejwt.authentication import JWTAuthentication

class WebTutoriaJWTAuthentication(JWTAuthentication):
	def authenticate(self, request):
		token = request.COOKIES.get('access_token')

		if token is None:
			return None

		validate_token = self.get_validated_token(token)
		return self.get_user(validate_token), validate_token
