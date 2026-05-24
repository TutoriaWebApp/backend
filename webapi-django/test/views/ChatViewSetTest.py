from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from project.models import ChatModel, MensagemModel, UsuarioModel, TutorModel
from datetime import date

class ChatViewSetTest(APITestCase):
    def setUp(self):
        self.aluno = UsuarioModel.objects.create_user(
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
        
        self.other_user = UsuarioModel.objects.create_user(
            email='other@test.com',
            password='password123',
            nomePerfil='Outro',
            cidade='Brasília',
            estado='DF',
            aniversario=date(1995, 1, 1)
        )

    def test_create_chat(self):
        self.client.force_authenticate(user=self.aluno)
        url = reverse('chat-list')
        data = {'tutorId': self.tutor.id}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(ChatModel.objects.count(), 1)
        self.assertEqual(ChatModel.objects.first().usuarioId, self.aluno)

    def test_list_chats(self):
        ChatModel.objects.create(usuarioId=self.aluno, tutorId=self.tutor)
        
        # Logged as alumno - should see the chat
        self.client.force_authenticate(user=self.aluno)
        url = reverse('chat-list')
        response = self.client.get(url)
        self.assertEqual(len(response.data), 1)

        # Logged as other user - should NOT see the chat
        self.client.force_authenticate(user=self.other_user)
        response = self.client.get(url)
        self.assertEqual(len(response.data), 0)

    def test_create_chat_self_fail(self):
        self.client.force_authenticate(user=self.usuario_tutor)
        url = reverse('chat-list')
        data = {'tutorId': self.tutor.id}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data['mensagem'], "Você não pode iniciar um chat consigo mesmo.")

class MensagemViewSetTest(APITestCase):
    def setUp(self):
        self.aluno = UsuarioModel.objects.create_user(
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
        self.chat = ChatModel.objects.create(usuarioId=self.aluno, tutorId=self.tutor)
        
        self.other_user = UsuarioModel.objects.create_user(
            email='other@test.com',
            password='password123',
            nomePerfil='Outro',
            cidade='Brasília',
            estado='DF',
            aniversario=date(1995, 1, 1)
        )

    def test_send_message(self):
        self.client.force_authenticate(user=self.aluno)
        url = reverse('mensagem-list')
        data = {'chatId': self.chat.id, 'conteudo': 'Olá Tutor!'}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(MensagemModel.objects.count(), 1)

    def test_send_message_unauthorized(self):
        self.client.force_authenticate(user=self.other_user)
        url = reverse('mensagem-list')
        data = {'chatId': self.chat.id, 'conteudo': 'Tentativa invasão'}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data['mensagem'], "Você não tem permissão para enviar mensagens neste chat.")
