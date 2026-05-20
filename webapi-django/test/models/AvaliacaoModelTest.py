from django.test import TestCase
from django.core.exceptions import ValidationError
from project.models import AvaliacaoAprendizModel, AvaliacaoTutorModel, UsuarioModel, TutorModel, SessaoModel, AreaModel, EspecialidadeModel
from datetime import date, time

class AvaliacaoModelTest(TestCase):
    def setUp(self):
        # Create users
        self.aluno = UsuarioModel.objects.create_user(
            email='aluno@tutoria.com',
            password='password123',
            nomePerfil='Aluno Avaliador',
            cidade='City',
            estado='TS',
            aniversario=date(1995, 5, 5)
        )
        self.tutor_user = UsuarioModel.objects.create_user(
            email='tutor@tutoria.com',
            password='password123',
            nomePerfil='Tutor Avaliado',
            cidade='City',
            estado='TS',
            aniversario=date(1985, 5, 5)
        )
        # Create tutor
        self.tutor = TutorModel.objects.create(usuarioId=self.tutor_user)
        
        # Create Area and Especialidade for Sessao
        self.area = AreaModel.objects.create(nomeArea='Exatas')
        self.especialidade = EspecialidadeModel.objects.create(areaId=self.area, nomeEspecialidade='Matemática')
        
        # Create Sessao
        self.sessao = SessaoModel.objects.create(
            usuarioId=self.aluno,
            tutorId=self.tutor,
            areaId=self.area,
            especialidadeId=self.especialidade,
            dataSessao=date.today(),
            horarioInicio=time(10, 0),
            horarioFim=time(11, 0)
        )

    def test_avaliar_aprendiz(self):
        avaliacao = AvaliacaoAprendizModel.objects.create(
            usuarioId=self.aluno,
            sessaoId=self.sessao,
            nota=5,
            comentario='Ótimo aluno!'
        )
        self.assertEqual(avaliacao.nota, 5)
        self.assertEqual(avaliacao.comentario, 'Ótimo aluno!')
        self.assertEqual(str(avaliacao), 'Avaliação Aprendiz - Aluno Avaliador (5)')

    def test_avaliar_tutor(self):
        avaliacao = AvaliacaoTutorModel.objects.create(
            tutorId=self.tutor,
            sessaoId=self.sessao,
            nota=4,
            comentario='Muito bom!'
        )
        self.assertEqual(avaliacao.nota, 4)
        self.assertEqual(avaliacao.comentario, 'Muito bom!')
        self.assertEqual(str(avaliacao), 'Avaliação Tutor - Tutor Avaliado (4)')

    def test_nota_validator_should_enforce_min_max_when_full_clean_is_called(self):
        # Test values above 5
        avaliacao_invalida_max = AvaliacaoTutorModel(
            tutorId=self.tutor,
            sessaoId=self.sessao,
            nota=6,
            comentario='Invalido'
        )
        with self.assertRaises(ValidationError):
            avaliacao_invalida_max.full_clean()

        # Test values below 1
        avaliacao_invalida_min = AvaliacaoAprendizModel(
            usuarioId=self.aluno,
            sessaoId=self.sessao,
            nota=0,
            comentario='Invalido'
        )
        with self.assertRaises(ValidationError):
            avaliacao_invalida_min.full_clean()
