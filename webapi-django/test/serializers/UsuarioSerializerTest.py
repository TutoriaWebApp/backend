from django.test import TestCase
from project.models import UsuarioModel, AreaModel, EspecialidadeModel, TutorModel, ContemModel
from project.serializers import *
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
        self.request.user = self.user

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
        self.assertNotIn('email', data)
        self.assertIn('fotoURL', data)

    def test_usuario_registro_serializer(self):
        data = self.user_data.copy()
        data['email'] = 'new@tutoria.com'
        serializer = UsuarioRegistroSerializer(data=data)
        self.assertTrue(serializer.is_valid())
        user = serializer.save()
        self.assertEqual(user.email, 'new@tutoria.com')

    def test_usuario_registro_with_especialidades(self):
        area = AreaModel.objects.create(nomeArea='Matemática')
        esp1 = EspecialidadeModel.objects.create(areaId=area, nomeEspecialidade='Cálculo 1')
        esp2 = EspecialidadeModel.objects.create(areaId=area, nomeEspecialidade='Cálculo 2')

        data = self.user_data.copy()
        data['email'] = 'tutor_new@tutoria.com'
        data['especialidades'] = [esp1.id, esp2.id]

        serializer = UsuarioRegistroSerializer(data=data)
        self.assertTrue(serializer.is_valid(), serializer.errors)
        user = serializer.save()

        self.assertEqual(user.email, 'tutor_new@tutoria.com')
        
        tutor = TutorModel.objects.get(usuarioId=user)
        self.assertIsNotNone(tutor)
        
        especialidades_tutor = ContemModel.objects.filter(tutorId=tutor)
        self.assertEqual(especialidades_tutor.count(), 2)
        self.assertEqual(especialidades_tutor[0].especialidadeId, esp1)
        self.assertEqual(especialidades_tutor[1].especialidadeId, esp2)

