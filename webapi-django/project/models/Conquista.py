from django.db import models

class Conquista(models.Model):
	id        = models.AutoField(primary_key=True, db_column='conquistaId')
	titulo    = models.CharField(max_length=32)
	descricao = models.CharField(max_length=64)
	urlImagem = models.CharField(max_length=256)
	pontos    = models.IntegerField()

	def __str__(self):
		return self.titulo

	class Meta:
		db_table = 'CONQUISTA'
		verbose_name = 'CONQUISTA'
		verbose_name_plural = 'CONQUISTAS'
