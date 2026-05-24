from django.db import models
from .UsuarioModel import UsuarioModel
from .TutorModel import TutorModel

class ChatModel(models.Model):
	id       = models.AutoField(primary_key=True, db_column='chatId')

	class Meta:
		db_table = 'CHAT'
		verbose_name = 'CHAT'
		verbose_name_plural = 'CHATS'


class MensagemModel(models.Model):
	id     = models.AutoField(primary_key=True, db_column='mensagemId')

	class Meta:
		db_table = 'MENSAGEM'
		verbose_name = 'MENSAGEM'
		verbose_name_plural = 'MENSAGENS'
