from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from project.models import Usuario

class UsuarioCreateForm(UserCreationForm):

	class Meta(UserCreationForm.Meta):
		model = Usuario

		fields = [
			'email',
			'nomePerfil',
			'cidade',
			'estado',
			'aniversario',
		]

class UsuarioUpdateForm(UserChangeForm):

	password = None

	class Meta(UserChangeForm.Meta):
		model = Usuario
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
