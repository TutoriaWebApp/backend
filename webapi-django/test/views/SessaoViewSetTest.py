from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from project.models import UsuarioModel, TutorModel, AgendaModel, AreaModel, EspecialidadeModel, SolicitacaoModel, SessaoModel
import datetime

class SessaoViewSetTest(APITestCase):
	def setUp(self):
		self.usuario_aluno = UsuarioModel.objects.create_user(
			email='aluno@example.com', password='testpassword123',
			nomePerfil='Aluno', cidade='Test City', estado='TS'
		)
		self.usuario_tutor = UsuarioModel.objects.create_user(
			email='tutor@example.com', password='testpassword123',
			nomePerfil='Tutor', cidade='Test City', estado='TS'
		)
		self.tutor = TutorModel.objects.create(usuarioId=self.usuario_tutor)

		self.area = AreaModel.objects.create(nomeArea='Exatas')
		self.especialidade = EspecialidadeModel.objects.create(areaId=self.area, nomeEspecialidade='Matemática')

		self.agenda = AgendaModel.objects.create(
			tutorId=self.tutor,
			dia=AgendaModel.DiaSemana.SEGUNDA,
			horarioInicio=datetime.time(10, 0),
			horarioFim=datetime.time(11, 0)
		)

		self.solicitacao = SolicitacaoModel.objects.create(
			usuarioId=self.usuario_aluno,
			agendaId=self.agenda,
			areaId=self.area,
			especialidadeId=self.especialidade,
			dataPretendida=datetime.date.today() + datetime.timedelta(days=1),
			estado=SolicitacaoModel.EstadoSolicitacao.PENDENTE
		)

		self.sessao = SessaoModel.objects.create(
			usuarioId=self.usuario_aluno,
			tutorId=self.tutor,
			areaId=self.area,
			especialidadeId=self.especialidade,
			dataSessao=datetime.date.today() + datetime.timedelta(days=2),
			horarioInicio=datetime.time(10, 0),
			horarioFim=datetime.time(11, 0)
		)

		self.agendas_url = reverse('agendas-list')
		self.solicitacoes_url = reverse('solicitacoes-list')
		self.sessoes_url = reverse('sessoes-list')

	def test_lista_agendas_unauthenticated(self):
		response = self.client.get(self.agendas_url)
		self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

	def test_lista_agendas_authenticated(self):
		self.client.force_authenticate(user=self.usuario_aluno)
		response = self.client.get(self.agendas_url)
		self.assertEqual(response.status_code, status.HTTP_200_OK)
		self.assertEqual(len(response.data), 1)

	def test_cria_agenda_como_tutor(self):
		self.client.force_authenticate(user=self.usuario_tutor)
		data = {
			'dia': AgendaModel.DiaSemana.TERCA,
			'horarioInicio': '14:00:00',
			'horarioFim': '15:00:00'
		}
		response = self.client.post(self.agendas_url, data)
		self.assertEqual(response.status_code, status.HTTP_201_CREATED)
		self.assertEqual(AgendaModel.objects.count(), 2)

	def test_cria_agenda_como_nao_tutor(self):
		self.client.force_authenticate(user=self.usuario_aluno)
		data = {
			'dia': AgendaModel.DiaSemana.QUARTA,
			'horarioInicio': '14:00:00',
			'horarioFim': '15:00:00'
		}
		response = self.client.post(self.agendas_url, data)
		self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

	def test_lista_solicitacoes_aluno(self):
		self.client.force_authenticate(user=self.usuario_aluno)
		response = self.client.get(self.solicitacoes_url)
		self.assertEqual(response.status_code, status.HTTP_200_OK)
		self.assertEqual(len(response.data), 1)

	def test_lista_sessoes_aluno(self):
		self.client.force_authenticate(user=self.usuario_aluno)
		response = self.client.get(self.sessoes_url)
		self.assertEqual(response.status_code, status.HTTP_200_OK)
		self.assertEqual(len(response.data), 1)

	def test_aceitar_solicitacao_como_tutor(self):
		self.client.force_authenticate(user=self.usuario_tutor)
		url = reverse('aceitar-solicitacao-detail', args=[self.solicitacao.id])

		sessoes_antes = SessaoModel.objects.count()

		response = self.client.patch(url)
		self.assertEqual(response.status_code, status.HTTP_200_OK)

		self.solicitacao.refresh_from_db()
		self.assertEqual(self.solicitacao.estado, SolicitacaoModel.EstadoSolicitacao.ACEITO)

		sessoes_depois = SessaoModel.objects.count()
		self.assertEqual(sessoes_depois, sessoes_antes + 1)

		nova_sessao = SessaoModel.objects.last()
		self.assertEqual(nova_sessao.usuarioId, self.solicitacao.usuarioId)
		self.assertEqual(nova_sessao.tutorId, self.solicitacao.agendaId.tutorId)
		self.assertEqual(nova_sessao.dataSessao, self.solicitacao.dataPretendida)
		self.assertEqual(nova_sessao.horarioInicio, self.solicitacao.agendaId.horarioInicio)
		self.assertEqual(nova_sessao.horarioFim, self.solicitacao.agendaId.horarioFim)

	def test_aceitar_solicitacao_nao_tutor(self):
		self.client.force_authenticate(user=self.usuario_aluno)
		url = reverse('aceitar-solicitacao-detail', args=[self.solicitacao.id])
		response = self.client.patch(url)
		self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
		self.assertIn("Apenas o tutor responsável pode aceitar", response.data[0] if isinstance(response.data, list) else str(response.data))

	def test_recusar_solicitacao_como_tutor(self):
		self.client.force_authenticate(user=self.usuario_tutor)
		url = reverse('recusar-solicitacao-detail', args=[self.solicitacao.id])
		response = self.client.patch(url)
		self.assertEqual(response.status_code, status.HTTP_200_OK)
		self.solicitacao.refresh_from_db()
		self.assertEqual(self.solicitacao.estado, SolicitacaoModel.EstadoSolicitacao.RECUSADO)

	def test_recusar_solicitacao_nao_tutor(self):
		self.client.force_authenticate(user=self.usuario_aluno)
		url = reverse('recusar-solicitacao-detail', args=[self.solicitacao.id])
		response = self.client.patch(url)
		self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
		self.assertIn("Apenas o tutor responsável pode recusar", response.data[0] if isinstance(response.data, list) else str(response.data))
