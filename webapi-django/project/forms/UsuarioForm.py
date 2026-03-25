from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from project.models import UsuarioModel

class UsuarioCreateForm(UserCreationForm):

	class Meta(UserCreationForm.Meta):
		model = UsuarioModel

		fields = [
			'email',
			'nomePerfil',
			'cidade',
			'estado',
		]

class UsuarioUpdateForm(UserChangeForm):

	password = None

	class Meta(UserChangeForm.Meta):
		model = UsuarioModel
		fields = [
			'email',
			'nomePerfil',
			'pontuacao',
			'cidade',
			'estado',
			'aniversario',
			'is_active',
			'is_staff',
		]
