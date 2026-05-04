from django.test import TestCase
from project.models import TutorModel, AreaModel, EspecialidadeModel, UsuarioModel, ContemModel
from project.serializers import TutorSerializer, AreaSerializer, EspecialidadeSerializer, ContemSerializer
from datetime import date

class TutorAreaSerializerTest(TestCase):
    def setUp(self):
        self.user = UsuarioModel.objects.create_user(
            email='tutor@tutoria.com',
            password='password123',
            nomePerfil='Tutor',
            cidade='City',
            estado='TS',
            aniversario=date(1985, 1, 1)
        )
        self.tutor = TutorModel.objects.create(usuarioId=self.user)
        self.area = AreaModel.objects.create(nomeArea='Tecnologia')
        self.esp = EspecialidadeModel.objects.create(areaId=self.area, nomeEspecialidade='Django')
        ContemModel.objects.create(tutorId=self.tutor, especialidadeId=self.esp)

    def test_area_serializer(self):
        serializer = AreaSerializer(self.area)
        self.assertEqual(serializer.data['nomeArea'], 'Tecnologia')

    def test_especialidade_serializer(self):
        serializer = EspecialidadeSerializer(self.esp)
        self.assertEqual(serializer.data['nomeEspecialidade'], 'Django')
        self.assertEqual(serializer.data['areaId'], self.area.id)

    def test_tutor_serializer(self):
        serializer = TutorSerializer(self.tutor)
        data = serializer.data
        self.assertEqual(data['usuarioId'], self.user.id)
        self.assertEqual(len(data['especialidades']), 1)
        self.assertEqual(data['especialidades'][0]['nomeEspecialidade'], 'Django')

    def test_contem_serializer(self):
        rel = ContemModel.objects.get(tutorId=self.tutor, especialidadeId=self.esp)
        serializer = ContemSerializer(rel)
        self.assertEqual(serializer.data['tutorId'], self.tutor.id)
        self.assertEqual(serializer.data['especialidadeId'], self.esp.id)
