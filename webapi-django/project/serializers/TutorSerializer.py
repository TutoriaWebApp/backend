from rest_framework import serializers
from project.models import *

class TutorSerializer(serializers.ModelSerializer):
	especialidades = serializers.SerializerMethodField()

	class Meta:
		model = TutorModel
		fields = ['id', 'usuarioId', 'especialidades']

	def get_especialidades(self, obj):
		contem_queryset = ContemModel.objects.filter(tutorId=obj)
		especialidades = [item.especialidadeId for item in contem_queryset]
		return EspecialidadeSerializer(especialidades, many=True).data

class AreaSerializer(serializers.ModelSerializer):
	class Meta:
		model = AreaModel
		fields = '__all__'

class EspecialidadeSerializer(serializers.ModelSerializer):
	class Meta:
		model = EspecialidadeModel
		fields = ['id', 'nomeEspecialidade', 'areaId']

class ContemSerializer(serializers.ModelSerializer):
	class Meta:
		model = ContemModel
		fields = '__all__'
