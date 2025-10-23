from django.db import models
from .Usuario import Usuario

class Conquista(models.Model):
	id        = models.AutoField(primary_key=True, db_column='conquistaId')
	titulo    = models.CharField(max_length=32)
	descricao = models.CharField(max_length=64)
	urlImagem = models.CharField(max_length=256)
	pontos    = models.IntegerField()

	usuarios  = models.ManyToManyField(
		Usuario,
		through='consegue',
		related_name='conquistas'
	)

	def __str__(self):
		return self.titulo

	class Meta:
		db_table = 'CONQUISTA'
		verbose_name = 'CONQUISTA'
		verbose_name_plural = 'CONQUISTAS'
