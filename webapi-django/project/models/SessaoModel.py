from django.db import models
from .UsuarioModel import UsuarioModel
from .TutorModel import *

class AgendaModel(models.Model):
	class DiaSemana(models.TextChoices):
		SEGUNDA = 'SEG', 'Segunda-feira'
		TERCA = 'TER', 'Terça-feira'
		QUARTA = 'QUA', 'Quarta-feira'
		QUINTA = 'QUI', 'Quinta-feira'
		SEXTA = 'SEX', 'Sexta-feira'
		SABADO = 'SAB', 'Sábado'
		DOMINGO = 'DOM', 'Domingo'

	id = models.AutoField(primary_key=True, db_column='agendaId')

	tutorId = models.ForeignKey(
		TutorModel,
		on_delete=models.CASCADE,
		db_column='tutorId',
		related_name='agendas'
	)

	horarioInicio = models.TimeField()
	horarioFim = models.TimeField()

	dia = models.CharField(
		max_length=3,
		choices=DiaSemana.choices,
		null=False
	)

	def __str__(self):
		return f"[{self.tutorId}]({self.dia} {self.horarioInicio})"

	class Meta:
		unique_together = ('tutorId', 'dia', 'horarioInicio')
		db_table = 'AGENDA'
		verbose_name = 'AGENDA'
		verbose_name_plural = 'AGENDAS'



class SolicitacaoModel(models.Model):
	class EstadoSolicitacao(models.TextChoices):
		ACEITO     = 'ACEITO', 'Solicitação Aceita'
		PENDENTE   = 'PENDENTE', 'Tutor precisa aceitar'
		RECUSADO   = 'RECUSADO', 'Solicitação recusada'
		RECORRENTE = 'RECORRENTE', 'Solicitação recorrente'

	id = models.AutoField(primary_key=True, db_column='solicitacaoId')

	usuarioId = models.ForeignKey(
		UsuarioModel,
		on_delete=models.CASCADE,
		db_column='usuarioId',
		related_name='solicitacoes'
	)

	agendaId = models.ForeignKey(
		AgendaModel,
		on_delete=models.CASCADE,
		db_column='agendaId',
		related_name='solicitacoes'
	)

	areaId = models.ForeignKey(
		AreaModel,
		on_delete=models.CASCADE,
		db_column='areaId'
	)

	especialidadeId = models.ForeignKey(
		EspecialidadeModel,
		on_delete=models.CASCADE,
		db_column='especialidadeId'
	)

	dataCriacao = models.DateTimeField(auto_now_add=True)
	dataPretendida = models.DateField(null=False)
	validade    = models.TimeField(null=True)
	estado      = models.CharField(max_length=10, choices=EstadoSolicitacao, default=EstadoSolicitacao.PENDENTE)

	def __str__(self):
		return f"Aluno {self.usuarioId} SOLICITA AGENDA: {self.agendaId}"
	class Meta:
		unique_together = ('usuarioId', 'agendaId')
		db_table = 'SOLICITACAO'
		verbose_name = 'SOLICITACAO'
		verbose_name_plural = 'SOLICITACOES'



class SessaoModel(models.Model):
	id = models.AutoField(primary_key=True, db_column='sessaoId')

	solicitacaoId = models.ForeignKey(
		SolicitacaoModel,
		on_delete=models.CASCADE,
		db_column='solicitacaoId',
		related_name='sessoes'
	)

	agendaId = models.ForeignKey(
		AgendaModel,
		on_delete=models.CASCADE,
		db_column='agendaId',
		related_name='sessoes'
	)

	usuarioId = models.ForeignKey(
		UsuarioModel,
		on_delete=models.CASCADE,
		db_column='usuarioId',
		related_name='sessoes'
	)

	tutorId = models.ForeignKey(
		TutorModel,
		on_delete=models.CASCADE,
		db_column='tutorId',
		related_name='sessoes'
	)

	areaId = models.ForeignKey(
		AreaModel,
		on_delete=models.CASCADE,
		db_column='areaId'
	)

	especialidadeId = models.ForeignKey(
		EspecialidadeModel,
		on_delete=models.CASCADE,
		db_column='especialidadeId'
	)

	dataRealizacao = models.DateField()

	def __str__(self):
		return f"Sessao {self.id} ({self.dataRealizacao})"

	class Meta:
		db_table = 'SESSAO'
		verbose_name = 'SESSAO'
		verbose_name_plural = 'SESSOES'
