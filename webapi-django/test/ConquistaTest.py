from datetime import date
from django.test import TestCase
from django.contrib.auth import get_user_model
from rest_framework.test import APIRequestFactory

from project.models import UsuarioModel, ConquistaModel, consegueModel
from project.serializers.ConquistaSerializer import ConquistaSerializer, ConquistaUsuarioSerializer, consegueSerializer

UsuarioModel = get_user_model()

class ConquistaSerializerTest(TestCase):
    def setUp(self):
        self.factory = APIRequestFactory()
        self.conquista = ConquistaModel.objects.create(
            titulo='Primeira Conquista',
            descricao='Descrição da primeira conquista',
            urlImagem='http://example.com/image.jpg',
            pontos=10
        )

    def test_conquista_serializer(self):
        """Testa serialização completa de Conquista"""
        serializer = ConquistaSerializer(self.conquista)
        data = serializer.data
        self.assertEqual(data['titulo'], 'Primeira Conquista')
        self.assertEqual(data['descricao'], 'Descrição da primeira conquista')
        self.assertEqual(data['urlImagem'], 'http://example.com/image.jpg')
        self.assertEqual(data['pontos'], 10)
        self.assertIn('id', data)


class ConquistaUsuarioSerializerTest(TestCase):
    def setUp(self):
        self.factory = APIRequestFactory()
        self.conquista = ConquistaModel.objects.create(
            titulo='Conquista Usuario',
            descricao='Descrição para usuario',
            urlImagem='http://example.com/user_image.jpg',
            pontos=20
        )

    def test_conquista_usuario_serializer(self):
        """Testa serialização limitada de Conquista para usuario"""
        serializer = ConquistaUsuarioSerializer(self.conquista)
        data = serializer.data
        self.assertEqual(data['titulo'], 'Conquista Usuario')
        self.assertEqual(data['descricao'], 'Descrição para usuario')
        self.assertEqual(data['urlImagem'], 'http://example.com/user_image.jpg')
        self.assertEqual(data['pontos'], 20)
        # Não deve incluir 'id'
        self.assertNotIn('id', data)


class consegueSerializerTest(TestCase):
    def setUp(self):
        self.factory = APIRequestFactory()
        self.user = UsuarioModel.objects.create_user(
            email='test@example.com',
            nomePerfil='Test User',
            cidade='Test City',
            estado='TS',
            aniversario=date(1990, 1, 1),
            password='testpass123'
        )
        self.conquista = ConquistaModel.objects.create(
            titulo='Conquista Conseguida',
            descricao='Descrição',
            urlImagem='http://example.com/image.jpg',
            pontos=15
        )
        self.consegue = consegueModel.objects.create(
            usuarioId=self.user,
            conquistaId=self.conquista
        )

    def test_consegue_serializer(self):
        """Testa serialização de consegue"""
        serializer = consegueSerializer(self.consegue)
        data = serializer.data
        self.assertEqual(data['usuarioId'], self.user.id)
        self.assertEqual(data['conquistaId'], self.conquista.id)
        self.assertIn('dataObtido', data)
        self.assertIn('id', data)
