from django.db import models
from .TutorModel import TutorModel

class SessaoModel(models.Model):
	class DiaSemana(models.TextChoices):
		SEGUNDA = 'SEG', 'Segunda-feira'
		TERCA = 'TER', 'Terça-feira'
		QUARTA = 'QUA', 'Quarta-feira'
		QUINTA = 'QUI', 'Quinta-feira'
		SEXTA = 'SEX', 'Sexta-feira'
		SABADO = 'SAB', 'Sábado'
		DOMINGO = 'DOM', 'Domingo'

	id = models.AutoField(primary_key=True, db_column='sessaoId')

	tutorId = models.ForeignKey(
		TutorModel,
		on_delete=models.CASCADE,
		db_column='tutorId',
		related_name='sessoes'
	)

	horarioInicio = models.TimeField()
	horarioFim = models.TimeField()

	dia = models.CharField(
		max_length=3,
		choices=DiaSemana.choices,
	)

	def __str__(self):
		return f"[{self.tutorId}]({self.dia} {self.horarioInicio})"

	class Meta:
		unique_together = ('tutorId', 'horarioInicio', 'dia')
		db_table = 'SESSAO'
		verbose_name = 'SESSAO'
		verbose_name_plural = 'SESSOES'
