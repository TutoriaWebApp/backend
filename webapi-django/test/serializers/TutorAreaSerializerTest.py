from django.test import TestCase, RequestFactory
from project.models import TutorModel, AreaModel, EspecialidadeModel, UsuarioModel, ContemModel
from project.serializers import TutorSerializer, AreaSerializer, EspecialidadeSerializer, ContemSerializer
from datetime import date

class TutorAreaSerializerTest(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.user = UsuarioModel.objects.create_user(
            email='tutor_serializer@tutoria.com',
            password='password123',
            nomePerfil='Tutor Supremo',
            cidade='São Paulo',
            estado='SP',
            pontuacao=4.5,
            aniversario=date(1985, 1, 1)
        )
        self.tutor = TutorModel.objects.create(usuarioId=self.user)
        self.area = AreaModel.objects.create(nomeArea='Tecnologia')
        self.esp = EspecialidadeModel.objects.create(areaId=self.area, nomeEspecialidade='Django')
        self.contem = ContemModel.objects.create(tutorId=self.tutor, especialidadeId=self.esp)

    def test_area_serializer(self):
        serializer = AreaSerializer(self.area)
        self.assertEqual(serializer.data['nomeArea'], 'Tecnologia')

    def test_especialidade_serializer(self):
        serializer = EspecialidadeSerializer(self.esp)
        self.assertEqual(serializer.data['nomeEspecialidade'], 'Django')
        self.assertEqual(serializer.data['areaId'], self.area.id)

    def test_contem_serializer(self):
        serializer = ContemSerializer(self.contem)
        self.assertEqual(serializer.data['tutorId'], self.tutor.id)
        self.assertEqual(serializer.data['especialidadeId'], self.esp.id)

    def test_tutor_serializer(self):
        request = self.factory.get('/')
        serializer = TutorSerializer(self.tutor, context={'request': request})
        data = serializer.data
        
        self.assertEqual(data['usuarioId'], self.user.id)
        self.assertEqual(data['nomePerfil'], 'Tutor Supremo')
        self.assertEqual(data['estado'], 'SP')
        self.assertEqual(data['cidade'], 'São Paulo')
        self.assertEqual(data['pontuacao'], 4.5)
        
        # Testing if fotoURL is handled correctly (currently no mock file, should be None)
        self.assertIsNone(data['fotoURL'])
        
        # Checking computed especialidades
        self.assertEqual(len(data['especialidades']), 1)
        self.assertEqual(data['especialidades'][0]['nomeEspecialidade'], 'Django')
        self.assertEqual(data['especialidades'][0]['id'], self.esp.id)
        self.assertEqual(data['especialidades'][0]['areaId'], self.area.id)

    def test_tutor_serializer_no_request_context(self):
        serializer = TutorSerializer(self.tutor)
        data = serializer.data
        
        self.assertEqual(data['nomePerfil'], 'Tutor Supremo')
        self.assertIsNone(data['fotoURL'])
