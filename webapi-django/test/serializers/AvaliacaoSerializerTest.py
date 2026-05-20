from django.test import TestCase
from project.models import AvaliacaoAprendizModel, AvaliacaoTutorModel, SessaoModel, TutorModel, UsuarioModel, AreaModel, EspecialidadeModel
from project.serializers import AvaliacaoAprendizSerializer, AvaliacaoTutorSerializer
from datetime import date, time

class AvaliacaoSerializerTest(TestCase):
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
        # Sessão
        self.sessao = SessaoModel.objects.create(
            usuarioId=self.aluno,
            tutorId=self.tutor,
            areaId=self.area,
            especialidadeId=self.esp,
            dataSessao=date(2025, 10, 20),
            horarioInicio=time(14, 0),
            horarioFim=time(15, 0)
        )

    def test_avaliacao_aprendiz_serializer(self):
        avaliacao = AvaliacaoAprendizModel.objects.create(
            usuarioId=self.aluno,
            sessaoId=self.sessao,
            nota=5,
            comentario="Ótima sessão!"
        )
        serializer = AvaliacaoAprendizSerializer(avaliacao)
        self.assertEqual(serializer.data['usuarioId'], self.aluno.id)
        self.assertEqual(serializer.data['nota'], 5)
        self.assertEqual(serializer.data['comentario'], "Ótima sessão!")

    def test_avaliacao_tutor_serializer(self):
        avaliacao = AvaliacaoTutorModel.objects.create(
            tutorId=self.tutor,
            sessaoId=self.sessao,
            nota=4,
            comentario="Bom desempenho."
        )
        serializer = AvaliacaoTutorSerializer(avaliacao)
        self.assertEqual(serializer.data['tutorId'], self.tutor.id)
        self.assertEqual(serializer.data['nota'], 4)
        self.assertEqual(serializer.data['comentario'], "Bom desempenho.")
