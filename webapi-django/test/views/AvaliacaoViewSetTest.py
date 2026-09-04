from rest_framework.test import APITestCase
from project.utils.GeoLocalizacaoUtil import Point

from rest_framework import status
from django.urls import reverse
from project.models import AvaliacaoAprendizModel, AvaliacaoTutorModel, SessaoModel, TutorModel, UsuarioModel, AreaModel, EspecialidadeModel
from datetime import date, time, timedelta
from django.utils import timezone

class AvaliacaoViewSetTest(APITestCase):
    def setUp(self):
        # Aluno
        self.aluno = UsuarioModel.objects.create_user(
            localizacao=Point(0, 0, srid=4326), email='aluno@tutoria.com',
            password='password123',
            nomePerfil='Aluno',
            cidade='City',
            estado='TS',
            aniversario=date(1995, 5, 5)
        )
        # Tutor (Usuário e Objeto Tutor)
        self.usuario_tutor = UsuarioModel.objects.create_user(
            localizacao=Point(0, 0, srid=4326), email='tutor@tutoria.com',
            password='password123',
            nomePerfil='Tutor',
            cidade='City',
            estado='TS',
            aniversario=date(1985, 5, 5)
        )
        self.tutor = TutorModel.objects.create(usuarioId=self.usuario_tutor)
        # Area e Especialidade
        self.area = AreaModel.objects.create(nomeArea='Exatas')
        self.esp = EspecialidadeModel.objects.create(areaId=self.area, nomeEspecialidade='Cálculo')
        
        # Sessão Passada (Pendente de Avaliação)
        hoje = timezone.now().date()
        self.sessao_passada = SessaoModel.objects.create(
            usuarioId=self.aluno,
            tutorId=self.tutor,
            areaId=self.area,
            especialidadeId=self.esp,
            dataSessao=hoje - timedelta(days=1),
            horarioInicio=time(14, 0),
            horarioFim=time(15, 0)
        )
        
        # Autenticar
        self.client.force_authenticate(user=self.aluno)

    def test_create_avaliacao_aprendiz(self):
        url = reverse('avaliacoes-aprendiz-list')
        data = {
            'usuarioId': self.aluno.id,
            'sessaoId': self.sessao_passada.id,
            'nota': 5,
            'comentario': "Muito bom!"
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(AvaliacaoAprendizModel.objects.count(), 1)

    def test_create_avaliacao_tutor(self):
        url = reverse('avaliacoes-tutor-list')
        data = {
            'tutorId': self.tutor.id,
            'sessaoId': self.sessao_passada.id,
            'nota': 4,
            'comentario': "Dedicado."
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(AvaliacaoTutorModel.objects.count(), 1)

    def test_get_avaliacoes_pendentes_como_aprendiz(self):
        url = reverse('avaliacoes_pendentes')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['tipoPendente'], 'APRENDIZ')

    def test_get_avaliacoes_pendentes_como_tutor(self):
        # Autenticar como tutor
        self.client.force_authenticate(user=self.usuario_tutor)
        url = reverse('avaliacoes_pendentes')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['tipoPendente'], 'TUTOR')

    def test_get_avaliacoes_pendentes_apos_avaliar(self):
        # Aluno avalia o Tutor
        AvaliacaoTutorModel.objects.create(
            tutorId=self.tutor,
            sessaoId=self.sessao_passada,
            nota=5
        )
        url = reverse('avaliacoes_pendentes')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 0)

    def test_filter_avaliacao_aprendiz_by_usuario_id(self):
        # Criar outro aluno e avaliação
        outro_aluno = UsuarioModel.objects.create_user(
            localizacao=Point(0, 0, srid=4326), email='outro@tutoria.com',
            password='password123',
            nomePerfil='Outro',
            cidade='City',
            estado='TS'
        )
        AvaliacaoAprendizModel.objects.create(
            usuarioId=self.aluno,
            sessaoId=self.sessao_passada,
            nota=5
        )
        # O tutor precisa avaliar de volta para que a avaliação do aprendiz apareça (se não passou 48h)
        AvaliacaoTutorModel.objects.create(
            tutorId=self.tutor,
            sessaoId=self.sessao_passada,
            nota=5
        )
        sessao2 = SessaoModel.objects.create(
            usuarioId=outro_aluno,
            tutorId=self.tutor,
            areaId=self.area,
            especialidadeId=self.esp,
            dataSessao=date.today(),
            horarioInicio=time(10, 0),
            horarioFim=time(11, 0)
        )
        AvaliacaoAprendizModel.objects.create(
            usuarioId=outro_aluno,
            sessaoId=sessao2,
            nota=3
        )

        url = reverse('avaliacoes-aprendiz-list')
        response = self.client.get(url, {'usuario': self.aluno.id})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['count'], 1)
        self.assertEqual(response.data['results'][0]['usuarioId'], self.aluno.id)

    def test_avaliacao_nao_contabiliza_antes_48h_sem_resposta(self):
        url = reverse('avaliacoes-aprendiz-list')
        data = {
            'usuarioId': self.aluno.id,
            'sessaoId': self.sessao_passada.id,
            'nota': 2,
            'comentario': "Ruim"
        }
        self.client.post(url, data, format='json')
        self.aluno.refresh_from_db()
        self.assertEqual(self.aluno.notaAvaliacao, 5.0)

    def test_avaliacao_contabiliza_com_resposta(self):
        url = reverse('avaliacoes-aprendiz-list')
        data = {
            'usuarioId': self.aluno.id,
            'sessaoId': self.sessao_passada.id,
            'nota': 2,
            'comentario': "Ruim"
        }
        self.client.post(url, data, format='json')
        
        # Agora o tutor responde a avaliação
        url_tutor = reverse('avaliacoes-tutor-list')
        self.client.force_authenticate(user=self.usuario_tutor)
        data_tutor = {
            'tutorId': self.tutor.id,
            'sessaoId': self.sessao_passada.id,
            'nota': 4,
            'comentario': "Boa"
        }
        self.client.post(url_tutor, data_tutor, format='json')
        
        self.aluno.refresh_from_db()
        self.assertEqual(self.aluno.notaAvaliacao, 2.0)
        self.tutor.refresh_from_db()
        self.assertEqual(self.tutor.notaAvaliacao, 4.0)
