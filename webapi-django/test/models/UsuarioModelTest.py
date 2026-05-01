from django.test import TestCase
from project.models import UsuarioModel
from datetime import date

class UsuarioModelTest(TestCase):
    def setUp(self):
        self.user_data = {
            'email': 'test@tutoria.com',
            'password': 'password123',
            'nomePerfil': 'Teste User',
            'cidade': 'Brasília',
            'estado': 'DF',
            'aniversario': date(1990, 1, 1)
        }

    def test_create_user(self):
        user = UsuarioModel.objects.create_user(**self.user_data)
        self.assertEqual(user.email, self.user_data['email'])
        self.assertTrue(user.check_password(self.user_data['password']))
        self.assertEqual(user.nomePerfil, self.user_data['nomePerfil'])
        self.assertEqual(user.cidade, self.user_data['cidade'])
        self.assertEqual(user.estado, self.user_data['estado'])
        self.assertEqual(user.aniversario, self.user_data['aniversario'])
        self.assertEqual(str(user), self.user_data['email'])

    def test_user_default_fields(self):
        user = UsuarioModel.objects.create_user(**self.user_data)
        self.assertEqual(user.pontuacao, 0)
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)
