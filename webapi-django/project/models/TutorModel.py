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
	notaAvaliacao = models.FloatField(default=5.0, db_default=5.0)

	def __str__(self):
		return f"{self.usuarioId}"

	class Meta:
		db_table = 'TUTOR'
		verbose_name = 'TUTOR'
		verbose_name_plural = 'TUTORES'



class AreaModel(models.Model):
	id       = models.AutoField(primary_key=True, db_column='areaId')
	nomeArea = models.CharField(max_length=60, unique=True)

	def __str__(self):
		return self.nomeArea

	class Meta:
		db_table = 'AREA'
		verbose_name = 'AREA'
		verbose_name_plural = 'AREAS'



class EspecialidadeModel(models.Model):
	id                = models.AutoField(primary_key=True, db_column='especialidadeId')
	areaId            = models.ForeignKey(
		AreaModel,
		on_delete=models.CASCADE,
		db_column='areaId',
		related_name='especialidades'
	)
	nomeEspecialidade = models.CharField(max_length=100)

	tutores = models.ManyToManyField(
		TutorModel,
		through='ContemModel',
		related_name='especialidades'
	)

	def __str__(self):
		return f"{self.nomeEspecialidade} ({self.areaId})"

	class Meta:
		unique_together = ('areaId', 'nomeEspecialidade')
		db_table = 'ESPECIALIDADE'
		verbose_name = 'ESPECIALIDADE'
		verbose_name_plural = 'ESPECIALIDADES'



class ContemModel(models.Model):
	id = models.AutoField(primary_key=True, db_column='contemId')

	especialidadeId = models.ForeignKey(
		EspecialidadeModel,
		on_delete=models.CASCADE,
		db_column='especialidadeId'
	)

	tutorId = models.ForeignKey(
		TutorModel,
		on_delete=models.CASCADE,
		db_column='tutorId'
	)

	def __str__(self):
		return f"[{self.tutorId} -> {self.especialidadeId}]"

	class Meta:
		unique_together = ('especialidadeId', 'tutorId')
		db_table = 'contem'
		verbose_name = 'RELACIONAMENTO TUTOR-ESPECIALIDADE'
		verbose_name_plural = 'RELACIONAMENTOS TUTOR-ESPECIALIDADE'
