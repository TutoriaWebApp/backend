from django.db import models
from .UsuarioModel import UsuarioModel

class ConquistaModel(models.Model):
	id        = models.AutoField(primary_key=True, db_column='conquistaId')
	titulo    = models.CharField(max_length=32)
	descricao = models.CharField(max_length=64)
	urlImagem = models.CharField(max_length=256)
	pontos    = models.IntegerField()

	usuarios  = models.ManyToManyField(
		UsuarioModel,
		through='consegueModel',
		related_name='conquistas'
	)

	def __str__(self):
		return self.titulo

	class Meta:
		db_table = 'CONQUISTA'
		verbose_name = 'CONQUISTA'
		verbose_name_plural = 'CONQUISTAS'

class consegueModel(models.Model):
	id = models.AutoField(primary_key=True, db_column='consegueId')

	usuarioId = models.ForeignKey(
		UsuarioModel,
		on_delete=models.CASCADE,
		db_column='usuarioId')

	conquistaId = models.ForeignKey(
		ConquistaModel,
		on_delete=models.CASCADE,
		db_column='conquistaId'
	)

	dataObtido = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return f"[{self.usuarioId}\n -> {self.conquistaId}]"

	class Meta:
		unique_together = ('usuarioId', 'conquistaId')
		db_table = 'consegue'
		verbose_name = 'RELACIONAMENTO USUARIO-CONQUISTA'
		verbose_name_plural = 'RELACIONAMENTOS USUARIO-CONQUISTA'
