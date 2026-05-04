from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from project.models import UsuarioModel

class UsuarioViewSetTest(APITestCase):
	def setUp(self):
		self.usuario = UsuarioModel.objects.create_user(
			email='test@example.com',
			password='testpassword123',
			nomePerfil='Test User',
			cidade='Test City',
			estado='TS'
		)
		self.list_url = reverse('usuario-list')
		self.registro_url = reverse('criar_novo_usuario')
		self.perfil_url = reverse('perfil_do_usuario')
		self.altera_senha_url = reverse('altera_a_senha')

	def test_lista_usuarios(self):
		response = self.client.get(self.list_url)
		self.assertEqual(response.status_code, status.HTTP_200_OK)
		self.assertEqual(len(response.data), 1)

	def test_registro_usuario(self):
		data = {
			'email': 'new@example.com',
			'password': 'newpassword123',
			'nomePerfil': 'New User',
			'cidade': 'New City',
			'estado': 'NW'
		}
		response = self.client.post(self.registro_url, data)
		self.assertEqual(response.status_code, status.HTTP_201_CREATED)
		self.assertEqual(UsuarioModel.objects.count(), 2)

	def test_perfil_logado_unauthenticated(self):
		response = self.client.get(self.perfil_url)
		self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

	def test_perfil_logado_authenticated(self):
		self.client.force_authenticate(user=self.usuario)
		response = self.client.get(self.perfil_url)
		self.assertEqual(response.status_code, status.HTTP_200_OK)
		self.assertEqual(response.data['email'], self.usuario.email)

	def test_edita_perfil_logado(self):
		self.client.force_authenticate(user=self.usuario)
		data = {'nomePerfil': 'Updated Name'}
		response = self.client.patch(self.perfil_url, data)
		self.assertEqual(response.status_code, status.HTTP_200_OK)
		self.usuario.refresh_from_db()
		self.assertEqual(self.usuario.nomePerfil, 'Updated Name')

	def test_altera_senha(self):
		self.client.force_authenticate(user=self.usuario)
		data = {
			'senhaAntiga': 'testpassword123',
			'senhaAtual': 'newpassword456',
			'senhaConfirmar': 'newpassword456'
		}
		response = self.client.post(self.altera_senha_url, data)
		self.assertEqual(response.status_code, status.HTTP_200_OK)
		self.usuario.refresh_from_db()
		self.assertTrue(self.usuario.check_password('newpassword456'))
