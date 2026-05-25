from django.test import TestCase
from django.db.utils import IntegrityError
from project.models import ChatModel, MensagemModel, UsuarioModel, TutorModel
from datetime import date

class ChatModelTest(TestCase):
    def setUp(self):
        # Create a user for the student
        self.usuario = UsuarioModel.objects.create_user(
            email='aluno@tutoria.com',
            password='password123',
            nomePerfil='Aluno Teste',
            cidade='Brasília',
            estado='DF',
            aniversario=date(2000, 1, 1)
        )
        
        # Create a user for the tutor
        self.usuario_tutor = UsuarioModel.objects.create_user(
            email='tutor@tutoria.com',
            password='password123',
            nomePerfil='Tutor Teste',
            cidade='Brasília',
            estado='DF',
            aniversario=date(1990, 1, 1)
        )
        
        # Create the tutor
        self.tutor = TutorModel.objects.create(usuarioId=self.usuario_tutor)

    def test_chat_creation(self):
        chat = ChatModel.objects.create(usuarioId=self.usuario, tutorId=self.tutor)
        self.assertEqual(chat.usuarioId, self.usuario)
        self.assertEqual(chat.tutorId, self.tutor)
        
    def test_chat_str(self):
        chat = ChatModel.objects.create(usuarioId=self.usuario, tutorId=self.tutor)
        # Expecting failure here if ChatModel uses self.tutorId.nomePerfil instead of self.tutorId.usuarioId.nomePerfil
        expected_str = f"Chat - {self.tutor.usuarioId.nomePerfil} -> {self.usuario.nomePerfil}"
        try:
            self.assertEqual(str(chat), expected_str)
        except AttributeError as e:
            self.fail(f"str(chat) raised AttributeError: {e}. Check if ChatModel uses tutorId.usuarioId.nomePerfil")

    def test_chat_unique_constraint(self):
        ChatModel.objects.create(usuarioId=self.usuario, tutorId=self.tutor)
        with self.assertRaises(IntegrityError):
            ChatModel.objects.create(usuarioId=self.usuario, tutorId=self.tutor)

    def test_mensagem_creation(self):
        chat = ChatModel.objects.create(usuarioId=self.usuario, tutorId=self.tutor)
        mensagem = MensagemModel.objects.create(
            chatId=chat,
            conteudo='Olá, tudo bem?'
        )
        self.assertEqual(mensagem.chatId, chat)
        self.assertEqual(mensagem.conteudo, 'Olá, tudo bem?')
        self.assertIsNotNone(mensagem.horario)

    def test_mensagem_str(self):
        chat = ChatModel.objects.create(usuarioId=self.usuario, tutorId=self.tutor)
        conteudo = 'Teste mensagem longa para verificar o slice do str'
        mensagem = MensagemModel.objects.create(
            chatId=chat,
            conteudo=conteudo
        )
        expected_str = f"Mensagem em {chat} - {conteudo[:20]}..."
        self.assertEqual(str(mensagem), expected_str)
        self.assertEqual(mensagem._meta.verbose_name, 'MENSAGEM')
