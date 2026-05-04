from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from project.models import UsuarioModel, TutorModel, AreaModel, EspecialidadeModel, ContemModel

class TutorViewSetTest(APITestCase):
	def setUp(self):
		self.usuario = UsuarioModel.objects.create_user(
			email='test@example.com', password='testpassword123',
			nomePerfil='Test User', cidade='Test City', estado='TS'
		)
		self.area = AreaModel.objects.create(nomeArea='Ciências')
		self.especialidade = EspecialidadeModel.objects.create(areaId=self.area, nomeEspecialidade='Física')
		self.tutor = TutorModel.objects.create(usuarioId=self.usuario)
		self.contem = ContemModel.objects.create(tutorId=self.tutor, especialidadeId=self.especialidade)

		self.tutores_url = reverse('tutor-list')
		self.areas_url = reverse('areas-list')
		self.especialidades_url = reverse('especialidades-list')
		self.contem_url = reverse('contem-list')

	def test_lista_tutores_unauthenticated(self):
		response = self.client.get(self.tutores_url)
		self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

	def test_lista_tutores_authenticated(self):
		self.client.force_authenticate(user=self.usuario)
		response = self.client.get(self.tutores_url)
		self.assertEqual(response.status_code, status.HTTP_200_OK)
		self.assertEqual(len(response.data), 1)

	def test_cria_tutor_ja_existente(self):
		self.client.force_authenticate(user=self.usuario)
		response = self.client.post(self.tutores_url, {})
		self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

	def test_cria_tutor_novo(self):
		novo_usuario = UsuarioModel.objects.create_user(
			email='novo@example.com', password='testpassword123',
			nomePerfil='Novo', cidade='Test City', estado='TS'
		)
		self.client.force_authenticate(user=novo_usuario)
		response = self.client.post(self.tutores_url, {})
		self.assertEqual(response.status_code, status.HTTP_201_CREATED)
		self.assertEqual(TutorModel.objects.count(), 2)

	def test_lista_areas(self):
		response = self.client.get(self.areas_url)
		self.assertEqual(response.status_code, status.HTTP_200_OK)
		self.assertEqual(len(response.data), 1)

	def test_lista_especialidades(self):
		response = self.client.get(self.especialidades_url)
		self.assertEqual(response.status_code, status.HTTP_200_OK)
		self.assertEqual(len(response.data), 1)

	def test_lista_contem(self):
		response = self.client.get(self.contem_url)
		self.assertEqual(response.status_code, status.HTTP_200_OK)
		self.assertEqual(len(response.data), 1)
