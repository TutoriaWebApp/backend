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

	dataObtido = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return f"[{self.usuarioId}\n -> {self.conquistaId}]"

	class Meta:
		unique_together = ('usuarioId', 'conquistaId')
		db_table = 'consegue'

