from django.test import TestCase, override_settings

import os
import tempfile
from datetime import date

from django.core.files.uploadedfile import SimpleUploadedFile
from rest_framework import status
from rest_framework.test import APIRequestFactory, APITestCase, APIClient

from project.forms import UsuarioCreateForm, UsuarioUpdateForm
from project.models import UsuarioModel
from project.serializers import UsuarioSerializer, UsuarioRegistroSerializer, UsuarioAlteraSenhaSerializer
from project.views import UsuarioViewSet, UsuarioRegistroView

_email='test@tutoria.com'
_password='test123'
_nomePerfil='Teste'
_estado='DF'
_cidade='Brasília'
_aniversario=date(1970,10,1)
_foto_jpg_base64 = b'\xff\xd8\xff\xe0\x00\x10JFIF\x00\x01\x01\x01\x00H\x00H\x00\x00\xff\xdb\x00C\x00\x08\x06\x06\x07\x06\x05\x08\x07\x07\x07\t\t\x08\n\x0c\x14\r\x0c\x0b\x0b\x0c\x19\x12\x13\x0f\x14\x1d\x1a\x1f\x1e\x1d\x1a\x1c\x1c $.\' ",#\x1c\x1c(7),01444\x1f\'9=82<.342\xff\xc0\x00\x11\x08\x00\x01\x00\x01\x01\x01\x11\x00\x02\x11\x01\x03\x11\x01\xff\xc4\x00\x14\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x08\xff\xc4\x00\x14\x10\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xff\xda\x00\x0c\x03\x01\x00\x02\x11\x03\x11\x00\x3f\x00\xaa\xff\xd9'
_foto = SimpleUploadedFile('foto.jpg', _foto_jpg_base64, content_type='image/jpeg')

class UsuarioModelTest(TestCase):
	def test_model_OK(self):
		UserOk = UsuarioModel.objects.create_user(
			email=_email,
			password=_password,
			nomePerfil=_nomePerfil,
			estado=_estado,
			cidade=_cidade,
			aniversario=_aniversario,
		)
		self.assertEqual(str(UserOk), _email)
		self.assertEqual(UserOk.email, _email)
		self.assertEqual(UserOk.nomePerfil, _nomePerfil)
		self.assertEqual(UserOk.estado, _estado)
		self.assertEqual(UserOk.cidade, _cidade)
		self.assertEqual(UserOk.aniversario, _aniversario)
	pass

class UsuarioRegistroSerializerTest(TestCase):
	def setUp(self):
		self.factory = APIRequestFactory()

		self.user = UsuarioModel.objects.create_user(
			email='test@example.com',
			nomePerfil='Test User',
			cidade='Test City',
			estado='TS',
			password='testpass123'
		)

	def _serializer_user(self, user):
		return UsuarioSerializer(user, context={'request': self.factory.get('/')})

	@override_settings(MEDIA_ROOT=tempfile.mkdtemp())
	def test_UsuarioRegistroSerializer_OK(self):
		media_root = tempfile.mkdtemp()
		with override_settings(MEDIA_ROOT=media_root):
			data = {
				'email': _email,
				'password': _password,
				'nomePerfil': _nomePerfil,
				'estado': _estado,
				'cidade': _cidade,
				'aniversario': _aniversario,
				'foto': _foto
			}
			response = UsuarioRegistroSerializer(data=data)
			response.is_valid()
			user = response.save()

			serializer = self._serializer_user(user)
			fotoURL = serializer.get_fotoURL(user)
			self.assertIn(_email, fotoURL)
			self.assertEqual(_email, serializer.data['email'])
			self.assertEqual(_nomePerfil, serializer.data['nomePerfil'])

	def test_UsuarioRegistroSerializer_OK_opcionais(self):
		data = {
			'email': _email,
			'password': _password,
			'nomePerfil': _nomePerfil,
			'estado': _estado,
			'cidade': _cidade
		}
		response = UsuarioRegistroSerializer(data=data)
		response.is_valid()
		user = response.save()

		serializer = self._serializer_user(user)
		self.assertEqual(_email, serializer.data['email'])

	def test_UsuarioRegistroSerializer_email_obrigatorio(self):
		with self.assertRaises(AssertionError):
			data = {
				'email': '',
				'password': _password,
				'nomePerfil': _nomePerfil,
				'estado': _estado,
				'cidade': _cidade,
				'aniversario': _aniversario
			}
			response = UsuarioRegistroSerializer(data=data)
			response.is_valid()
			response.save()

	def test_UsuarioRegistroSerializer_password_obrigatorio(self):
		with self.assertRaises(AssertionError):
			data = {
				'email': _email,
				'password': '',
				'nomePerfil': _nomePerfil,
				'estado': _estado,
				'cidade': _cidade,
				'aniversario': _aniversario
			}
			response = UsuarioRegistroSerializer(data=data)
			response.is_valid()
			response.save()

	def test_UsuarioRegistroSerializer_nomePerfil_obrigatorio(self):
		with self.assertRaises(AssertionError):
			data = {
				'email': _email,
				'password': _password,
				'nomePerfil': '',
				'estado': _estado,
				'cidade': _cidade,
				'aniversario': _aniversario
			}
			response = UsuarioRegistroSerializer(data=data)
			response.is_valid()
			response.save()

	def test_UsuarioRegistroSerializer_estado_obrigatorio(self):
		with self.assertRaises(AssertionError):
			data = {
				'email': _email,
				'password': _password,
				'nomePerfil': _nomePerfil,
				'estado': '',
				'cidade': _cidade,
				'aniversario': _aniversario
			}
			response = UsuarioRegistroSerializer(data=data)
			response.is_valid()
			response.save()

	def test_UsuarioRegistroSerializer_cidade_obrigatorio(self):
		with self.assertRaises(AssertionError):
			data = {
				'email': _email,
				'password': _password,
				'nomePerfil': _nomePerfil,
				'estado': _estado,
				'cidade': '',
				'aniversario': _aniversario
			}
			response = UsuarioRegistroSerializer(data=data)
			response.is_valid()
			response.save()

	def test_UsuarioSerializer_put(self):
		media_root = tempfile.mkdtemp()
		with override_settings(MEDIA_ROOT=media_root):
			request = self.factory.put('/')
			request.user = self.user
			serializer = UsuarioSerializer(self.user, context={'request': request})
			data = {'NomePerfil': 'Seu Zé', 'foto': _foto}
			UsuarioAtualizado = serializer.update(self.user, data)
			self.assertEqual('test@example.com', UsuarioAtualizado.email)
			self.assertIn('test@example.com', serializer.data['fotoURL'])
	pass

class UsuarioViewSetTest(APITestCase):
	def setUp(self):
		self.client = APIClient()
		self.user = UsuarioModel.objects.create_user(
			email=_email,
			password=_password,
			nomePerfil=_nomePerfil,
			estado=_estado,
			cidade=_cidade,
			aniversario=_aniversario,
		)

		self.client.force_authenticate(user=self.user)

	def test_pesquisar_Usuario(self):
		url = f'/v1/usuarios/{self.user.id}/'
		response = self.client.get(url)
		self.assertEqual(response.status_code, status.HTTP_200_OK)
		self.assertEqual(_email, response.data['email'])
		print(response.data)
