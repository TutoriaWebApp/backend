from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from project.models import UsuarioModel, ConquistaModel, consegueModel

class ConquistaViewSetTest(APITestCase):
	def setUp(self):
		self.usuario = UsuarioModel.objects.create_user(
			email='test@example.com',
			password='testpassword123',
			nomePerfil='Test User',
			cidade='Test City',
			estado='TS'
		)
		self.conquista = ConquistaModel.objects.create(
			titulo='Primeira Conquista',
			descricao='Descrição da conquista',
			urlImagem='http://example.com/img.png',
			pontos=10
		)
		self.consegue = consegueModel.objects.create(
			usuarioId=self.usuario,
			conquistaId=self.conquista
		)
		self.list_url = reverse('conquista-list')
		self.consegue_url = reverse('consegue-list')
		self.usuario_conquista_url = reverse('conquistas_do_usuario', kwargs={'usuarioId': self.usuario.id})

	def test_lista_conquistas(self):
		response = self.client.get(self.list_url)
		self.assertEqual(response.status_code, status.HTTP_200_OK)
		self.assertEqual(len(response.data), 1)

	def test_lista_consegue_unauthenticated(self):
		response = self.client.get(self.consegue_url)
		self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

	def test_lista_consegue_authenticated(self):
		self.client.force_authenticate(user=self.usuario)
		response = self.client.get(self.consegue_url)
		self.assertEqual(response.status_code, status.HTTP_200_OK)
		self.assertEqual(len(response.data), 1)

	def test_usuario_conquistas_unauthenticated(self):
		response = self.client.get(self.usuario_conquista_url)
		self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

	def test_usuario_conquistas_authenticated(self):
		self.client.force_authenticate(user=self.usuario)
		response = self.client.get(self.usuario_conquista_url)
		self.assertEqual(response.status_code, status.HTTP_200_OK)
		self.assertEqual(len(response.data), 1)
