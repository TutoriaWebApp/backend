from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from project.models import *

class SistemaRecomendacaoViewSetTest(APITestCase):
    def setUp(self):
        # Usuário principal (aluno)
        self.aluno = UsuarioModel.objects.create_user(
            email='aluno@test.com', password='password123',
            nomePerfil='Aluno Teste', cidade='São Paulo', estado='SP'
        )
        
        # Tutor 1: Mesma cidade, mesma especialidade que o aluno terá interesse
        self.u_tutor1 = UsuarioModel.objects.create_user(
            email='tutor1@test.com', password='password123',
            nomePerfil='Tutor 1', cidade='São Paulo', estado='SP'
        )
        self.tutor1 = TutorModel.objects.create(usuarioId=self.u_tutor1)
        
        # Tutor 2: Outra cidade, mesma especialidade
        self.u_tutor2 = UsuarioModel.objects.create_user(
            email='tutor2@test.com', password='password123',
            nomePerfil='Tutor 2', cidade='Rio de Janeiro', estado='RJ'
        )
        self.tutor2 = TutorModel.objects.create(usuarioId=self.u_tutor2)
        
        # Setup de Áreas e Especialidades
        self.area = AreaModel.objects.create(nomeArea='Exatas')
        self.spec = EspecialidadeModel.objects.create(areaId=self.area, nomeEspecialidade='Matemática')
        self.spec2 = EspecialidadeModel.objects.create(areaId=self.area, nomeEspecialidade='Física')
        
        ContemModel.objects.create(tutorId=self.tutor1, especialidadeId=self.spec)
        ContemModel.objects.create(tutorId=self.tutor2, especialidadeId=self.spec)
        
        # Tutor 3: São Paulo, mas especialidade diferente (Física)
        self.u_tutor3 = UsuarioModel.objects.create_user(
            email='tutor3@test.com', password='password123',
            nomePerfil='Tutor 3', cidade='São Paulo', estado='SP'
        )
        self.tutor3 = TutorModel.objects.create(usuarioId=self.u_tutor3)
        ContemModel.objects.create(tutorId=self.tutor3, especialidadeId=self.spec2)

        # Simular interesse do aluno: uma sessão passada com Matemática
        SessaoModel.objects.create(
            usuarioId=self.aluno,
            tutorId=self.tutor2, 
            areaId=self.area,
            especialidadeId=self.spec,
            dataSessao='2023-01-01',
            horarioInicio='10:00',
            horarioFim='11:00'
        )
        
        # Setup de Agendas
        AgendaModel.objects.create(
            tutorId=self.tutor1,
            dia='SEG',
            horarioInicio='08:00',
            horarioFim='12:00'
        )
        
        self.recomendacoes_url = reverse('recomendacoes-list')

    def test_recomendacoes_unauthenticated(self):
        response = self.client.get(self.recomendacoes_url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_recomendacoes_list(self):
        self.client.force_authenticate(user=self.aluno)
        response = self.client.get(self.recomendacoes_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
        # Agora a resposta é paginada
        self.assertEqual(response.data['count'], 3)
        results = response.data['results']
        self.assertEqual(len(results), 3)
        
        # Tutor 1 deve estar em primeiro porque está na mesma cidade (SP)
        # e tem a especialidade de interesse (Matemática).
        self.assertEqual(results[0]['id'], self.tutor1.id)

    def test_recomendacoes_com_filtro_area_e_especialidade(self):
        self.client.force_authenticate(user=self.aluno)
        
        # Filtro por Área: Deve retornar os 3 tutores (Matemática e Física são Exatas)
        response = self.client.get(self.recomendacoes_url, {'area': self.area.id})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['count'], 3)
        
        # Filtro por Especialidade (Matemática): Deve retornar Tutor 1 e Tutor 2
        response = self.client.get(self.recomendacoes_url, {'especialidade': self.spec.id})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['count'], 2)
        results = response.data['results']
        self.assertIn(results[0]['id'], [self.tutor1.id, self.tutor2.id])
        
        # Filtro por Especialidade (Física): Deve retornar apenas Tutor 3
        response = self.client.get(self.recomendacoes_url, {'especialidade': self.spec2.id})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['count'], 1)
        self.assertEqual(response.data['results'][0]['id'], self.tutor3.id)

    def test_recomendacoes_com_filtro_agenda(self):
        self.client.force_authenticate(user=self.aluno)
        
        # Filtro que apenas o Tutor 1 atende
        response = self.client.get(self.recomendacoes_url, {
            'dia': 'SEG',
            'horarioInicio': '09:00',
            'horarioFim': '10:00'
        })
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['count'], 1)
        self.assertEqual(response.data['results'][0]['id'], self.tutor1.id)

    def test_recomendacoes_agenda_vazia(self):
        self.client.force_authenticate(user=self.aluno)
        
        # Filtro que ninguém atende (domingo)
        response = self.client.get(self.recomendacoes_url, {
            'dia': 'DOM',
            'horarioInicio': '09:00',
            'horarioFim': '10:00'
        })
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # Se vazio, o ViewSet retorna [] antes da paginação no código atual
        # OU se passar pelo paginator vazio, retorna estrutura com count 0
        if isinstance(response.data, list):
            self.assertEqual(len(response.data), 0)
        else:
            self.assertEqual(response.data['count'], 0)
