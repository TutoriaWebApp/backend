from django.test import TestCase
from project.utils.GeoLocalizacaoUtil import Point

from project.models import ChatModel, MensagemModel, UsuarioModel, TutorModel
from project.serializers import ChatSerializer, MensagemSerializer
from datetime import date

class ChatSerializerTest(TestCase):
    def setUp(self):
        self.usuario = UsuarioModel.objects.create_user(
            localizacao=Point(0, 0, srid=4326), email='aluno@test.com',
            password='password123',
            nomePerfil='Aluno',
            cidade='Brasília',
            estado='DF',
            aniversario=date(2000, 1, 1)
        )
        self.usuario_tutor = UsuarioModel.objects.create_user(
            localizacao=Point(0, 0, srid=4326), email='tutor@test.com',
            password='password123',
            nomePerfil='Tutor',
            cidade='Brasília',
            estado='DF',
            aniversario=date(1990, 1, 1)
        )
        self.tutor = TutorModel.objects.create(usuarioId=self.usuario_tutor)
        self.chat = ChatModel.objects.create(usuarioId=self.usuario, tutorId=self.tutor)

    def test_chat_serializer_output(self):
        from rest_framework.test import APIRequestFactory
        factory = APIRequestFactory()
        request = factory.get('/')
        request.user = self.usuario_tutor
        
        serializer = ChatSerializer(instance=self.chat, context={'request': request})
        data = serializer.data
        self.assertEqual(data['id'], self.chat.id)
        self.assertEqual(data['usuarioId'], self.usuario.id)
        self.assertNotIn('tutorId', data)  # tutorId is write_only
        self.assertEqual(data['mensagensNaoLidas'], 0)

    def test_chat_serializer_with_messages(self):
        MensagemModel.objects.create(chatId=self.chat, usuarioId=self.usuario, conteudo='Olá')
        
        from rest_framework.test import APIRequestFactory
        factory = APIRequestFactory()
        request = factory.get('/')
        request.user = self.usuario_tutor

        serializer = ChatSerializer(instance=self.chat, context={'request': request})
        self.assertIn('ultimaMensagem', serializer.data)
        self.assertEqual(serializer.data['ultimaMensagem'], 'Olá')

class MensagemSerializerTest(TestCase):
    def setUp(self):
        self.usuario = UsuarioModel.objects.create_user(
            localizacao=Point(0, 0, srid=4326), email='aluno@test.com',
            password='password123',
            nomePerfil='Aluno',
            cidade='Brasília',
            estado='DF',
            aniversario=date(2000, 1, 1)
        )
        self.usuario_tutor = UsuarioModel.objects.create_user(
            localizacao=Point(0, 0, srid=4326), email='tutor@test.com',
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
        
        from rest_framework.test import APIRequestFactory
        factory = APIRequestFactory()
        request = factory.post('/')
        request.user = self.usuario

        serializer = MensagemSerializer(data=data, context={'request': request})
        self.assertTrue(serializer.is_valid())
        
        # serializer.save(usuarioId=self.usuario) as it's a read-only field
        mensagem = serializer.save(usuarioId=self.usuario)
        self.assertEqual(mensagem.conteudo, 'Teste de mensagem')
        self.assertIsNotNone(mensagem.horario)
