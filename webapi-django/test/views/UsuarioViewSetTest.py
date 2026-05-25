import io
import os
import shutil
import tempfile
from PIL import Image

from django.urls import reverse
from django.test import override_settings
from django.core.files.uploadedfile import SimpleUploadedFile
from rest_framework import status
from rest_framework.test import APITestCase

from project.models import UsuarioModel, TutorModel, AreaModel, EspecialidadeModel, ContemModel

MEDIA_ROOT = tempfile.mkdtemp()

@override_settings(MEDIA_ROOT=MEDIA_ROOT)
class UsuarioViewSetTest(APITestCase):
	@classmethod
	def tearDownClass(cls):
		shutil.rmtree(MEDIA_ROOT, ignore_errors=True)
		super().tearDownClass()

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
		"""Verifica se a listagem de usuários retorna apenas campos públicos."""
		response = self.client.get(self.list_url)
		self.assertEqual(response.status_code, status.HTTP_200_OK)

		self.assertTrue(len(response.data) >= 1)

		usuario_data = response.data[0]
		self.assertIn('nomePerfil', usuario_data)
		self.assertIn('pontuacao', usuario_data)
		self.assertIn('fotoURL', usuario_data)

		self.assertNotIn('email', usuario_data)
		self.assertNotIn('aniversario', usuario_data)
		self.assertNotIn('perfilTutor', usuario_data)

	def test_registro_usuario_simples(self):
		"""Testa o registro de um usuário sem especialidades (não vira tutor)."""
		data = {
			'email': 'new@example.com',
			'password': 'newpassword123',
			'nomePerfil': 'New User',
			'cidade': 'New City',
			'estado': 'NW'
		}
		response = self.client.post(self.registro_url, data)
		self.assertEqual(response.status_code, status.HTTP_201_CREATED)
		self.assertTrue(UsuarioModel.objects.filter(email='new@example.com').exists())

		self.assertFalse(TutorModel.objects.filter(usuarioId__email='new@example.com').exists())

	def test_registro_usuario_com_especialidades(self):
		"""Testa o registro de um usuário com especialidades (deve criar perfil de tutor)."""
		area = AreaModel.objects.create(nomeArea='Ciências')
		esp = EspecialidadeModel.objects.create(areaId=area, nomeEspecialidade='Física')

		data = {
			'email': 'tutor@example.com',
			'password': 'newpassword123',
			'nomePerfil': 'Tutor User',
			'cidade': 'New City',
			'estado': 'NW',
			'especialidades': [esp.id]
		}
		response = self.client.post(self.registro_url, data)
		self.assertEqual(response.status_code, status.HTTP_201_CREATED)

		user = UsuarioModel.objects.get(email='tutor@example.com')

		tutor = TutorModel.objects.filter(usuarioId=user).first()
		self.assertIsNotNone(tutor)

		self.assertTrue(ContemModel.objects.filter(tutorId=tutor, especialidadeId=esp).exists())

	def test_registro_usuario_com_foto(self):
		"""Testa o registro de usuário enviando uma foto de perfil."""
		import glob
		file = io.BytesIO()
		image = Image.new('RGB', size=(100, 100), color=(155, 0, 0))
		image.save(file, 'png')
		file.name = 'perfil.png'
		file.seek(0)

		foto = SimpleUploadedFile(file.name, file.read(), content_type='image/png')

		data = {
			'email': 'photo@example.com',
			'password': 'newpassword123',
			'nomePerfil': 'Photo User',
			'cidade': 'New City',
			'estado': 'NW',
			'foto': foto
		}
		response = self.client.post(self.registro_url, data, format='multipart')
		self.assertEqual(response.status_code, status.HTTP_201_CREATED)

		user = UsuarioModel.objects.get(email='photo@example.com')

		caminho_foto = os.path.join(MEDIA_ROOT, 'perfis', f'{user.email.lower()}.*')
		self.assertTrue(len(glob.glob(caminho_foto)) > 0)

	def test_perfil_logado_unauthenticated(self):
		response = self.client.get(self.perfil_url)
		self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

	def test_perfil_logado_authenticated(self):
		self.client.force_authenticate(user=self.usuario)
		response = self.client.get(self.perfil_url)
		self.assertEqual(response.status_code, status.HTTP_200_OK)

		self.assertEqual(response.data['email'], self.usuario.email)
		self.assertIn('perfilTutor', response.data)
		self.assertIn('fotoURL', response.data)

	def test_edita_perfil_logado(self):
		self.client.force_authenticate(user=self.usuario)
		data = {'nomePerfil': 'Updated Name', 'cidade': 'Updated City'}
		response = self.client.patch(self.perfil_url, data)
		self.assertEqual(response.status_code, status.HTTP_200_OK)

		self.usuario.refresh_from_db()
		self.assertEqual(self.usuario.nomePerfil, 'Updated Name')
		self.assertEqual(self.usuario.cidade, 'Updated City')

	def test_altera_senha_sucesso(self):
		self.client.force_authenticate(user=self.usuario)
		data = {
			'senhaAntiga': 'testpassword123',
			'senhaAtual': 'newpassword456'
		}
		response = self.client.post(self.altera_senha_url, data)
		self.assertEqual(response.status_code, status.HTTP_200_OK)

		self.usuario.refresh_from_db()
		self.assertTrue(self.usuario.check_password('newpassword456'))

	def test_altera_senha_antiga_incorreta(self):
		self.client.force_authenticate(user=self.usuario)
		data = {
			'senhaAntiga': 'wrongpassword',
			'senhaAtual': 'newpassword456'
		}
		response = self.client.post(self.altera_senha_url, data)
		self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
		self.assertIn('senhaAntiga', response.data)
