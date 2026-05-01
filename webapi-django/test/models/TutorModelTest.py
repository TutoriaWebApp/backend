from django.test import TestCase
from project.models import TutorModel, UsuarioModel
from datetime import date

class TutorModelTest(TestCase):
    def setUp(self):
        self.user = UsuarioModel.objects.create_user(
            email='tutor@tutoria.com',
            password='password123',
            nomePerfil='Tutor',
            cidade='City',
            estado='TS',
            aniversario=date(1985, 1, 1)
        )

    def test_tutor_creation(self):
        tutor = TutorModel.objects.create(usuarioId=self.user)
        self.assertEqual(tutor.usuarioId, self.user)
        self.assertEqual(str(tutor), 'tutor@tutoria.com')
