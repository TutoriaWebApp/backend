from django.test import TestCase
from django.db import IntegrityError
from project.utils.GeoLocalizacaoUtil import Point

from project.models import ConquistaModel, consegueModel, UsuarioModel
from datetime import date

class ConquistaModelTest(TestCase):
    def setUp(self):
        self.user = UsuarioModel.objects.create_user(
            localizacao=Point(0, 0, srid=4326), email='test@tutoria.com',
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
            pontos=10,
            tier=ConquistaModel.Tier.BRONZE,
            secreta=False,
            pista='Nenhuma'
        )

    def test_conquista_creation(self):
        self.assertEqual(self.conquista.titulo, 'Primeira Aula')
        self.assertEqual(self.conquista.descricao, 'Completou a primeira aula')
        self.assertEqual(self.conquista.urlImagem, 'http://image.url')
        self.assertEqual(self.conquista.pontos, 10)
        self.assertEqual(self.conquista.tier, 'B')
        self.assertFalse(self.conquista.secreta)
        self.assertEqual(self.conquista.pista, 'Nenhuma')
        self.assertEqual(str(self.conquista), 'Primeira Aula')

    def test_conquista_defaults(self):
        conq = ConquistaModel.objects.create(
            titulo='Conquista Padrao',
            descricao='Sem campos opcionais',
            urlImagem='url',
            pontos=50
        )
        self.assertEqual(conq.tier, 'B')
        self.assertFalse(conq.secreta)

    def test_consegue_relationship(self):
        rel = consegueModel.objects.create(
            usuarioId=self.user,
            conquistaId=self.conquista
        )
        self.assertEqual(self.user.conquistas.count(), 1)
        self.assertIn(self.conquista, self.user.conquistas.all())
        
        # Test __str__ method of consegueModel
        rel_str = str(rel)
        self.assertIn(str(self.user), rel_str)
        self.assertIn('Primeira Aula', rel_str)
        self.assertIn('->', rel_str)
        
        # Test unique together
        with self.assertRaises(IntegrityError):
            consegueModel.objects.create(
                usuarioId=self.user,
                conquistaId=self.conquista
            )
