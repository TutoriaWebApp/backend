from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from project.models import UsuarioModel, TutorModel, AreaModel, EspecialidadeModel, ContemModel
from project.utils.GeoLocalizacaoUtil import Point

class TutorViewSetTest(APITestCase):
	def setUp(self):
		self.usuario = UsuarioModel.objects.create_user(
			email='test@example.com', password='testpassword123',
			nomePerfil='Test User', cidade='Test City', estado='TS',
			localizacao=Point(0, 0, srid=4326)
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
		outro_usuario = UsuarioModel.objects.create_user(
			email='outro@example.com', password='testpassword123',
			nomePerfil='Outro', cidade='Test City', estado='TS',
			localizacao=Point(0, 0, srid=4326)
		)
		TutorModel.objects.create(usuarioId=outro_usuario)

		self.client.force_authenticate(user=self.usuario)
		response = self.client.get(self.tutores_url)
		self.assertEqual(response.status_code, status.HTTP_200_OK)
		self.assertEqual(len(response.data['results']), 1)

	def test_cria_tutor_ja_existente(self):
		self.client.force_authenticate(user=self.usuario)
		response = self.client.post(self.tutores_url, {})
		self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

	def test_cria_tutor_novo(self):
		novo_usuario = UsuarioModel.objects.create_user(
			email='novo@example.com', password='testpassword123',
			nomePerfil='Novo', cidade='Test City', estado='TS',
			localizacao=Point(0, 0, srid=4326)
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

	def test_lista_tutores_filtro_raio(self):
		from project.utils.GeoLocalizacaoUtil import Point

		# Atualiza localização do usuário logado para Brasília
		self.usuario.localizacao = Point(-47.882778, -15.793889)
		self.usuario.save()

		# Tutor 1: Brasília (próximo, 0km)
		u1 = UsuarioModel.objects.create_user(
			email='tutor_bsb@example.com', password='testpassword123',
			nomePerfil='Tutor BSB', cidade='Brasília', estado='DF',
			localizacao=Point(-47.882778, -15.793889)
		)
		t1 = TutorModel.objects.create(usuarioId=u1)

		# Tutor 2: São Paulo (~870km de distância)
		u2 = UsuarioModel.objects.create_user(
			email='tutor_sp@example.com', password='testpassword123',
			nomePerfil='Tutor SP', cidade='São Paulo', estado='SP',
			localizacao=Point(-46.633308, -23.550520)
		)
		t2 = TutorModel.objects.create(usuarioId=u2)

		self.client.force_authenticate(user=self.usuario)

		# Filtra com raio de 50km -> deve retornar apenas t1 (BSB)
		resp_50 = self.client.get(f"{self.tutores_url}?raio=50")
		self.assertEqual(resp_50.status_code, status.HTTP_200_OK)
		ids_50 = [t['id'] for t in resp_50.data['results']]
		self.assertIn(t1.id, ids_50)
		self.assertNotIn(t2.id, ids_50)

		# Filtra com raio de 1000km -> deve retornar ambos (t1 e t2)
		resp_1000 = self.client.get(f"{self.tutores_url}?raio=1000")
		self.assertEqual(resp_1000.status_code, status.HTTP_200_OK)
		ids_1000 = [t['id'] for t in resp_1000.data['results']]
		self.assertIn(t1.id, ids_1000)
		self.assertIn(t2.id, ids_1000)

	def test_lista_tutores_filtro_raio_invalido(self):
		self.client.force_authenticate(user=self.usuario)
		response = self.client.get(f"{self.tutores_url}?raio=abc")
		self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

