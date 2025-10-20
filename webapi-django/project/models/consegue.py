from django.db import models
from project.models import Usuario, Conquista

class consegue(models.Model):
	id = models.AutoField(primary_key=True, db_column='consegueId')

	usuarioId = models.ForeignKey(
		Usuario,
		on_delete=models.CASCADE,
		db_column='usuarioId')

	conquistaId = models.ForeignKey(
		Conquista,
		on_delete=models.CASCADE,
		db_column='conquistaId'
	)

	dataObtido = models.DateTimeField()

	class Meta:
		unique_together = ('usuarioId', 'conquistaId')
		db_table = 'consegue'

