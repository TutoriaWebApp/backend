from django.test import TestCase
from project.models import UsuarioModel
from project.serializers import UsuarioSerializer, UsuarioPublicoSerializer, UsuarioRegistroSerializer
from datetime import date
from rest_framework.test import APIRequestFactory

class UsuarioSerializerTest(TestCase):
    def setUp(self):
        self.factory = APIRequestFactory()
        self.user_data = {
            'email': 'test@tutoria.com',
            'password': 'password123',
            'nomePerfil': 'Teste User',
            'cidade': 'Brasília',
            'estado': 'DF',
            'aniversario': date(1990, 1, 1)
        }
        self.user = UsuarioModel.objects.create_user(**self.user_data)
        self.request = self.factory.get('/')

    def test_usuario_serializer(self):
        serializer = UsuarioSerializer(self.user, context={'request': self.request})
        data = serializer.data
        self.assertEqual(data['email'], self.user.email)
        self.assertEqual(data['nomePerfil'], self.user.nomePerfil)
        self.assertIn('fotoURL', data)

    def test_usuario_publico_serializer(self):
        serializer = UsuarioPublicoSerializer(self.user, context={'request': self.request})
        data = serializer.data
        self.assertEqual(data['nomePerfil'], self.user.nomePerfil)
        self.assertNotIn('password', data)
        self.assertNotIn('email', data) # UsuarioPublicoSerializer doesn't include email based on code provided earlier
        self.assertIn('fotoURL', data)

    def test_usuario_registro_serializer(self):
        data = self.user_data.copy()
        data['email'] = 'new@tutoria.com'
        serializer = UsuarioRegistroSerializer(data=data)
        self.assertTrue(serializer.is_valid())
        user = serializer.save()
        self.assertEqual(user.email, 'new@tutoria.com')
