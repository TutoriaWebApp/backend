from django.test import TestCase
from project.models import AgendaModel, SolicitacaoModel, SessaoModel, TutorModel, UsuarioModel, AreaModel, EspecialidadeModel
from project.serializers import AgendaSerializer, SolicitacaoSerializer, SessaoSerializer
from datetime import date, time

class SessaoSolicitacaoSerializerTest(TestCase):
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

    def test_agenda_serializer(self):
        serializer = AgendaSerializer(self.agenda)
        self.assertEqual(serializer.data['dia'], 'SEG')
        self.assertEqual(serializer.data['tutorId'], self.tutor.id)

    def test_solicitacao_serializer(self):
        solicitacao = SolicitacaoModel.objects.create(
            usuarioId=self.aluno,
            agendaId=self.agenda,
            areaId=self.area,
            especialidadeId=self.esp,
            dataPretendida=date(2025, 10, 20)
        )
        serializer = SolicitacaoSerializer(solicitacao)
        self.assertEqual(serializer.data['usuarioId'], self.aluno.id)
        self.assertEqual(serializer.data['agendaId'], self.agenda.id)

    def test_sessao_serializer(self):
        solicitacao = SolicitacaoModel.objects.create(
            usuarioId=self.aluno,
            agendaId=self.agenda,
            areaId=self.area,
            especialidadeId=self.esp,
            dataPretendida=date(2025, 10, 20),
            estado='ACEITO'
        )
        sessao = SessaoModel.objects.create(
            solicitacaoId=solicitacao,
            agendaId=self.agenda,
            usuarioId=self.aluno,
            tutorId=self.tutor,
            areaId=self.area,
            especialidadeId=self.esp,
            dataRealizacao=date(2025, 10, 20)
        )
        serializer = SessaoSerializer(sessao)
        self.assertEqual(serializer.data['dataRealizacao'], '2025-10-20')
        self.assertEqual(serializer.data['tutorId'], self.tutor.id)
