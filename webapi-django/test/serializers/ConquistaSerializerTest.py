from django.test import TestCase
from project.models import ConquistaModel, consegueModel, UsuarioModel
from project.serializers import ConquistaSerializer, ConquistaUsuarioSerializer, consegueSerializer
from datetime import date

class ConquistaSerializerTest(TestCase):
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

    def test_conquista_serializer(self):
        serializer = ConquistaSerializer(self.conquista)
        data = serializer.data
        self.assertEqual(data['titulo'], 'Primeira Aula')
        self.assertEqual(data['pontos'], 10)

    def test_conquista_usuario_serializer(self):
        serializer = ConquistaUsuarioSerializer(self.conquista)
        data = serializer.data
        self.assertEqual(data['titulo'], 'Primeira Aula')
        self.assertNotIn('id', data)

    def test_consegue_serializer(self):
        rel = consegueModel.objects.create(
            usuarioId=self.user,
            conquistaId=self.conquista
        )
        serializer = consegueSerializer(rel)
        data = serializer.data
        self.assertEqual(data['usuarioId'], self.user.id)
        self.assertEqual(data['conquistaId'], self.conquista.id)
