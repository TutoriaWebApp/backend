from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from .UsuarioModel import UsuarioModel
from .SessaoModel import SessaoModel
from .TutorModel import TutorModel

class AvaliacaoAprendizModel(models.Model):
	id        = models.AutoField(primary_key=True, db_column='avaliacaoAprendizId')
	usuarioId = models.ForeignKey(
		UsuarioModel,
		on_delete=models.CASCADE,
		db_column='usuarioId',
		related_name='avaliacoes_aprendiz'
	)
	sessaoId = models.ForeignKey(
		SessaoModel,
		on_delete=models.CASCADE,
		db_column='sessaoId',
		related_name='avaliacoes_aprendiz_sessao'
	)
	nota = models.IntegerField(
		validators=[MinValueValidator(1), MaxValueValidator(5)],
		null=False
	)
	comentario = models.CharField(max_length=200, blank=True, null=True)

	def __str__(self):
		return f"Avaliação Aprendiz - {self.usuarioId.nomePerfil} ({self.nota})"

	class Meta:
		db_table = 'AVALIACAO_APRENDIZ'
		verbose_name = 'AVALIAÇÃO DO APRENDIZ'
		verbose_name_plural = 'AVALIAÇÕES DOS APRENDIZES'


class AvaliacaoTutorModel(models.Model):
	id        = models.AutoField(primary_key=True, db_column='avaliacaoTutorId')
	tutorId = models.ForeignKey(
		TutorModel,
		on_delete=models.CASCADE,
		db_column='tutorId',
		related_name='avaliacoes_tutor'
	)
	sessaoId = models.ForeignKey(
		SessaoModel,
		on_delete=models.CASCADE,
		db_column='sessaoId',
		related_name='avaliacoes_tutor_sessao'
	)
	nota = models.IntegerField(
		validators=[MinValueValidator(1), MaxValueValidator(5)],
		null=False
	)
	comentario = models.CharField(max_length=200, blank=True, null=True)

	def __str__(self):
		return f"Avaliação Tutor - {self.tutorId.usuarioId.nomePerfil} ({self.nota})"

	class Meta:
		db_table = 'AVALIACAO_TUTOR'
		verbose_name = 'AVALIAÇÃO DO TUTOR'
		verbose_name_plural = 'AVALIAÇÕES DOS TUTORES'
