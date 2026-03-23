from django.db import models
from .SessaoModel import SessaoModel
from .UsuarioModel import UsuarioModel

class SolicitacaoModel(models.Model):
	class EstadoSolicitacao(models.TextChoices):
		ACEITO     = 'ACEITO', 'Solicitação Aceita'
		PENDENTE   = 'PENDENTE', 'Tutor precisa aceitar'
		RECUSADO   = 'RECUSADO', 'Solicitação recusada'
		RECORRENTE = 'RECORRENTE', 'Solicitação recorrente'

	id = models.AutoField(primary_key=True, db_column='solicitacaoId')
	dataCriacao = models.DateTimeField(auto_now_add=True)
	validade    = models.DateTimeField(null=True)
	estado      = models.CharField(max_length=10, choices=EstadoSolicitacao)

	usuarioId = models.ForeignKey(
		UsuarioModel,
		on_delete=models.CASCADE,
		db_column='usuarioId'
	)

	sessaoId = models.ForeignKey(
		SessaoModel,
		on_delete=models.CASCADE,
		db_column='sessaoId'
	)

	def __str__(self):
		return f"Aluno {self.usuarioId} SOLICITA SESSAO: {self.sessaoId}"
	class Meta:
		unique_together = ('usuarioId', 'sessaoId')
		db_table = 'SOLICITACAO'
