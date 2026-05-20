from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from project.models import AvaliacaoAprendizModel, AvaliacaoTutorModel, SessaoModel, TutorModel, UsuarioModel, AreaModel, EspecialidadeModel
from datetime import date, time, timedelta
from django.utils import timezone

class AvaliacaoViewSetTest(APITestCase):
    def setUp(self):
        # Aluno
        self.aluno = UsuarioModel.objects.create_user(
            email='aluno@tutoria.com',
            password='password123',
            nomePerfil='Aluno',
            cidade='City',
            estado='TS',
            aniversario=date(1995, 5, 5)
        )
        # Tutor (Usuário e Objeto Tutor)
        self.usuario_tutor = UsuarioModel.objects.create_user(
            email='tutor@tutoria.com',
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
        # Aluno avalia
        AvaliacaoAprendizModel.objects.create(
            usuarioId=self.aluno,
            sessaoId=self.sessao_passada,
            nota=5
        )
        url = reverse('avaliacoes_pendentes')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 0)
