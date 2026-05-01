from django.test import TestCase
from project.models import ConquistaModel, consegueModel, UsuarioModel
from datetime import date

class ConquistaModelTest(TestCase):
    def setUp(self):
        self.user = UsuarioModel.objects.create_user(
            email='test@tutoria.com',
            password='password123',
            nomePerfil='User',
            cidade='City',
            estado='TS',
            aniversario=date(1990, 1, 1)
        )
        self.conquista = ConquistaModel.objects.create(
            titulo='Primeira Aula',
            descricao='Completou a primeira aula',
            urlImagem='http://image.url',
            pontos=10
        )

    def test_conquista_creation(self):
        self.assertEqual(self.conquista.titulo, 'Primeira Aula')
        self.assertEqual(str(self.conquista), 'Primeira Aula')

    def test_consegue_relationship(self):
        rel = consegueModel.objects.create(
            usuarioId=self.user,
            conquistaId=self.conquista
        )
        self.assertEqual(self.user.conquistas.count(), 1)
        self.assertIn(self.conquista, self.user.conquistas.all())
        self.assertIn('test@tutoria.com', str(rel))
        self.assertIn('Primeira Aula', str(rel))
