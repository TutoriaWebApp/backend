from django.db import models
from .UsuarioModel import UsuarioModel
from .TutorModel import TutorModel

class ChatModel(models.Model):
	id       = models.AutoField(primary_key=True, db_column='chatId')

	usuarioId = models.ForeignKey(
		UsuarioModel,
		on_delete=models.CASCADE,
		db_column='usuarioId',
		related_name='chats'
	)

	tutorId  = models.ForeignKey(
		TutorModel,
		on_delete=models.CASCADE,
		db_column='tutorId',
		related_name='chats'
	)

	def __str__(self):
		return f"Chat - {self.tutorId.usuarioId.nomePerfil} -> {self.usuarioId.nomePerfil}"

	class Meta:
		constraints = [
			models.UniqueConstraint(fields=['tutorId', 'usuarioId'], name='CHAT_UK'),
		]
		db_table = 'CHAT'
		verbose_name = 'CHAT'
		verbose_name_plural = 'CHATS'


class MensagemModel(models.Model):
	id     = models.AutoField(primary_key=True, db_column='mensagemId')
	chatId = models.ForeignKey(
		ChatModel,
		on_delete=models.CASCADE,
		db_column='chatId',
		related_name='mensagens'
	)
	conteudo = models.CharField(max_length=200)
	horario = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return f"Mensagem em {self.chatId} - {self.conteudo[:20]}..."

	class Meta:
		db_table = 'MENSAGEM'
		verbose_name = 'MENSAGEM'
		verbose_name_plural = 'MENSAGENS'
