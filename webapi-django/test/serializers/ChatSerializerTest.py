from django.test import TestCase
from project.models import ChatModel, MensagemModel, UsuarioModel, TutorModel
from project.serializers import ChatSerializer, MensagemSerializer
from datetime import date

class ChatSerializerTest(TestCase):
    def setUp(self):
        self.usuario = UsuarioModel.objects.create_user(
            email='aluno@test.com',
            password='password123',
            nomePerfil='Aluno',
            cidade='Brasília',
            estado='DF',
            aniversario=date(2000, 1, 1)
        )
        self.usuario_tutor = UsuarioModel.objects.create_user(
            email='tutor@test.com',
            password='password123',
            nomePerfil='Tutor',
            cidade='Brasília',
            estado='DF',
            aniversario=date(1990, 1, 1)
        )
        self.tutor = TutorModel.objects.create(usuarioId=self.usuario_tutor)
        self.chat = ChatModel.objects.create(usuarioId=self.usuario, tutorId=self.tutor)

    def test_chat_serializer_output(self):
        serializer = ChatSerializer(instance=self.chat)
        data = serializer.data
        self.assertEqual(data['id'], self.chat.id)
        self.assertEqual(data['usuarioId'], self.usuario.id)
        self.assertEqual(data['tutorId'], self.tutor.id)
        self.assertEqual(len(data['mensagens']), 0)

    def test_chat_serializer_with_messages(self):
        MensagemModel.objects.create(chatId=self.chat, conteudo='Olá')
        serializer = ChatSerializer(instance=self.chat)
        self.assertEqual(len(serializer.data['mensagens']), 1)
        self.assertEqual(serializer.data['mensagens'][0]['conteudo'], 'Olá')

class MensagemSerializerTest(TestCase):
    def setUp(self):
        self.usuario = UsuarioModel.objects.create_user(
            email='aluno@test.com',
            password='password123',
            nomePerfil='Aluno',
            cidade='Brasília',
            estado='DF',
            aniversario=date(2000, 1, 1)
        )
        self.usuario_tutor = UsuarioModel.objects.create_user(
            email='tutor@test.com',
            password='password123',
            nomePerfil='Tutor',
            cidade='Brasília',
            estado='DF',
            aniversario=date(1990, 1, 1)
        )
        self.tutor = TutorModel.objects.create(usuarioId=self.usuario_tutor)
        self.chat = ChatModel.objects.create(usuarioId=self.usuario, tutorId=self.tutor)

    def test_mensagem_serializer_valid(self):
        data = {
            'chatId': self.chat.id,
            'conteudo': 'Teste de mensagem'
        }
        serializer = MensagemSerializer(data=data)
        self.assertTrue(serializer.is_valid())
        mensagem = serializer.save()
        self.assertEqual(mensagem.conteudo, 'Teste de mensagem')
        self.assertIsNotNone(mensagem.horario)
