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

    def test_filter_avaliacao_aprendiz_by_usuario_id(self):
        # Criar outro aluno e avaliação
        outro_aluno = UsuarioModel.objects.create_user(
            email='outro@tutoria.com',
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
        response = self.client.get(url, {'usuarioId': self.aluno.id})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # 1 avaliação criada no setUp (pelo pendentes test, mas aqui o setUp só cria sessao, não avaliacao)
        # Ah, no test_create_avaliacao_aprendiz cria uma. Mas aqui cada teste é isolado.
        # No meu test_filter_avaliacao_aprendiz_by_usuario_id eu criei 2 avaliações, uma para self.aluno e uma para outro_aluno.
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['usuarioId'], self.aluno.id)

    def test_update_usuario_rating_every_10_evaluations(self):
        url = reverse('avaliacoes-aprendiz-list')
        # Criar 9 avaliações manualmente
        for i in range(9):
            s = SessaoModel.objects.create(
                usuarioId=self.aluno,
                tutorId=self.tutor,
                areaId=self.area,
                especialidadeId=self.esp,
                dataSessao=date.today(),
                horarioInicio=time(i, 0),
                horarioFim=time(i, 30)
            )
            AvaliacaoAprendizModel.objects.create(
                usuarioId=self.aluno,
                sessaoId=s,
                nota=4
            )
            # Como estamos criando via ORM, o perform_create não é chamado.
            # Não precisamos disparar manual aqui pois queremos ver que no 10º via API funciona.
        
        # Verificar se a nota não foi alterada ainda (default 5.0)
        self.aluno.refresh_from_db()
        self.assertEqual(self.aluno.notaAvaliacao, 5.0)

        # Criar a 10ª avaliação via POST
        s10 = SessaoModel.objects.create(
            usuarioId=self.aluno,
            tutorId=self.tutor,
            areaId=self.area,
            especialidadeId=self.esp,
            dataSessao=date.today(),
            horarioInicio=time(10, 0),
            horarioFim=time(10, 30)
        )
        data = {
            'usuarioId': self.aluno.id,
            'sessaoId': s10.id,
            'nota': 2,
            'comentario': "Final"
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # Verificar nota atualizada: (9*4 + 2) / 10 = 38 / 10 = 3.8
        self.aluno.refresh_from_db()
        self.assertEqual(self.aluno.notaAvaliacao, 3.8)

    def test_update_usuario_rating_last_100_only(self):
        url = reverse('avaliacoes-aprendiz-list')
        
        # 1. Criar 9 avaliações com nota 1 via POST para disparar no 10
        # Na verdade, para ser eficiente, vamos criar 9 via ORM e a 10ª via POST.
        for i in range(9):
            s = SessaoModel.objects.create(usuarioId=self.aluno, tutorId=self.tutor, areaId=self.area, especialidadeId=self.esp, dataSessao=date.today(), horarioInicio=time(0, i), horarioFim=time(0, i+1))
            AvaliacaoAprendizModel.objects.create(usuarioId=self.aluno, sessaoId=s, nota=1)
        
        s10 = SessaoModel.objects.create(usuarioId=self.aluno, tutorId=self.tutor, areaId=self.area, especialidadeId=self.esp, dataSessao=date.today(), horarioInicio=time(0, 10), horarioFim=time(0, 11))
        self.client.post(url, {'usuarioId': self.aluno.id, 'sessaoId': s10.id, 'nota': 1}, format='json')

        # Aqui a nota deve ser 1.0
        self.aluno.refresh_from_db()
        self.assertEqual(self.aluno.notaAvaliacao, 1.0)

        # 2. Criar mais 89 avaliações com nota 5 via ORM e a 100ª via POST
        for i in range(10, 99):
            s = SessaoModel.objects.create(usuarioId=self.aluno, tutorId=self.tutor, areaId=self.area, especialidadeId=self.esp, dataSessao=date.today(), horarioInicio=time(1, i%60), horarioFim=time(1, (i+1)%60))
            AvaliacaoAprendizModel.objects.create(usuarioId=self.aluno, sessaoId=s, nota=5)
        
        s100 = SessaoModel.objects.create(usuarioId=self.aluno, tutorId=self.tutor, areaId=self.area, especialidadeId=self.esp, dataSessao=date.today(), horarioInicio=time(1, 59), horarioFim=time(2, 0))
        self.client.post(url, {'usuarioId': self.aluno.id, 'sessaoId': s100.id, 'nota': 5}, format='json')

        # No 100, disparou. Média das 100 (10*1 + 90*5) / 100 = 4.6
        self.aluno.refresh_from_db()
        self.assertEqual(self.aluno.notaAvaliacao, 4.6)

        # 3. Criar mais 9 avaliações com nota 5 via ORM e a 110ª via POST
        for i in range(100, 109):
            s = SessaoModel.objects.create(usuarioId=self.aluno, tutorId=self.tutor, areaId=self.area, especialidadeId=self.esp, dataSessao=date.today(), horarioInicio=time(2, i-100), horarioFim=time(2, i-99))
            AvaliacaoAprendizModel.objects.create(usuarioId=self.aluno, sessaoId=s, nota=5)
            
        s110 = SessaoModel.objects.create(usuarioId=self.aluno, tutorId=self.tutor, areaId=self.area, especialidadeId=self.esp, dataSessao=date.today(), horarioInicio=time(3, 0), horarioFim=time(3, 30))
        self.client.post(url, {'usuarioId': self.aluno.id, 'sessaoId': s110.id, 'nota': 5}, format='json')

        # As últimas 100 agora ignoram as primeiras 10 nota 1.
        self.aluno.refresh_from_db()
        self.assertEqual(self.aluno.notaAvaliacao, 5.0)
