from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from config.manager import UsuarioManager

class UsuarioModel(AbstractBaseUser, PermissionsMixin):
	id = models.AutoField(primary_key=True, db_column='usuarioId')
	pontuacao = models.PositiveIntegerField(default=0, db_default=0)
	email = models.EmailField(unique=True)
	password = models.CharField(max_length=256, db_column='senha')
	nomePerfil = models.CharField(max_length=100)
	cidade = models.CharField(max_length=80)
	estado = models.CharField(max_length=2)
	aniversario = models.DateField(blank=True, null=True, db_default=None, default=None)
	notaAvaliacao = models.FloatField(default=5.0, db_default=5.0)

	# Campos necessários para o funcionamento do Django Admin e Auth
	is_staff = models.BooleanField(default=False, db_default=False)
	is_superuser = models.BooleanField(default=False, db_default=False)
	is_active = models.BooleanField(default=True, db_default=True)
	date_joined = models.DateTimeField(auto_now_add=True)
	last_login = models.DateTimeField(null=True)

	objects = UsuarioManager()

	USERNAME_FIELD = 'email'
	# Campos requeridos ao criar um superusuário via linha de comando
	REQUIRED_FIELDS = ['nomePerfil', 'cidade', 'estado']

	def __str__(self):
		return self.email

	class Meta:
		db_table = 'USUARIO'
		verbose_name = 'USUARIO'
		verbose_name_plural = 'USUARIOS'
