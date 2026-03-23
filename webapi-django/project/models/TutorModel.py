from django.db import models
from .UsuarioModel import UsuarioModel

class TutorModel(models.Model):
	id = models.AutoField(primary_key=True, db_column='tutorId')
	usuarioId = models.OneToOneField(
		UsuarioModel,
		unique=True,
		on_delete=models.CASCADE,
		db_column='usuarioId'
	)

	def __str__(self):
		return f"{self.usuarioId}"

	class Meta:
		db_table = 'TUTOR'
		verbose_name = 'TUTOR'
		verbose_name_plural = 'TUTORES'
