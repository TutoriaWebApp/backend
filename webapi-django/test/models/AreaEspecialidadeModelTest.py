from django.test import TestCase
from project.models import AreaModel, EspecialidadeModel, TutorModel, UsuarioModel, ContemModel
from datetime import date

class AreaEspecialidadeModelTest(TestCase):
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

    def test_area_creation(self):
        self.assertEqual(self.area.nomeArea, 'Tecnologia')
        self.assertEqual(str(self.area), 'Tecnologia')

    def test_especialidade_creation(self):
        esp = EspecialidadeModel.objects.create(
            areaId=self.area,
            nomeEspecialidade='Django'
        )
        self.assertEqual(esp.nomeEspecialidade, 'Django')
        self.assertEqual(esp.areaId, self.area)
        self.assertEqual(str(esp), 'Django (Tecnologia)')

    def test_contem_relationship(self):
        esp = EspecialidadeModel.objects.create(
            areaId=self.area,
            nomeEspecialidade='React'
        )
        rel = ContemModel.objects.create(
            tutorId=self.tutor,
            especialidadeId=esp
        )
        self.assertEqual(self.tutor.especialidades.count(), 1)
        self.assertIn(esp, self.tutor.especialidades.all())
        self.assertIn('tutor@tutoria.com', str(rel))
        self.assertIn('React', str(rel))
