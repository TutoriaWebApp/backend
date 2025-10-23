from django.db import models
from project.models import Usuario

class Tutor(models.Model):
	id = models.AutoField(primary_key=True, db_column='tutorId')
	usuarioId = models.OneToOneField(
		Usuario,
		unique=True,
		on_delete=models.CASCADE,
		db_column='usuarioId'
	)

	class Meta:
		db_table = 'TUTOR'
		verbose_name = 'TUTOR'
		verbose_name_plural = 'TUTORES'
