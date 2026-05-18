from django.test import TestCase
from project.models import AgendaModel, SolicitacaoModel, SessaoModel, TutorModel, UsuarioModel, AreaModel, EspecialidadeModel
from datetime import date, time

class SessaoSolicitacaoModelTest(TestCase):
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
        # Tutor
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
        # Agenda
        self.agenda = AgendaModel.objects.create(
            tutorId=self.tutor,
            horarioInicio=time(14, 0),
            horarioFim=time(15, 0),
            dia=AgendaModel.DiaSemana.SEGUNDA
        )

    def test_agenda_creation(self):
        self.assertEqual(self.agenda.dia, 'SEG')
        self.assertEqual(str(self.agenda), '[tutor@tutoria.com](SEG 14:00:00)')

    def test_solicitacao_creation(self):
        solicitacao = SolicitacaoModel.objects.create(
            usuarioId=self.aluno,
            agendaId=self.agenda,
            areaId=self.area,
            especialidadeId=self.esp,
            dataPretendida=date(2025, 10, 20)
        )
        self.assertEqual(solicitacao.estado, 'PENDENTE')
        self.assertEqual(str(solicitacao), f"Aluno aluno@tutoria.com SOLICITA AGENDA: {self.agenda}")

    def test_sessao_creation(self):
        solicitacao = SolicitacaoModel.objects.create(
            usuarioId=self.aluno,
            agendaId=self.agenda,
            areaId=self.area,
            especialidadeId=self.esp,
            dataPretendida=date(2025, 10, 20),
            estado='ACEITO'
        )
        sessao = SessaoModel.objects.create(
            usuarioId=self.aluno,
            tutorId=self.tutor,
            areaId=self.area,
            especialidadeId=self.esp,
            dataSessao=date(2025, 10, 20),
            horarioInicio=time(14, 0),
            horarioFim=time(15, 0)
        )
        self.assertEqual(sessao.dataSessao, date(2025, 10, 20))
