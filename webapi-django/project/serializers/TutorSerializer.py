from rest_framework import serializers
from project.models import *
from project.utils import UsuarioUtils

class TutorSerializer(serializers.ModelSerializer):
	especialidades = serializers.SerializerMethodField()
	nomePerfil = serializers.SerializerMethodField()
	estado = serializers.SerializerMethodField()
	cidade = serializers.SerializerMethodField()
	pontuacao = serializers.SerializerMethodField()
	fotoURL = serializers.SerializerMethodField()

	class Meta:
		model = TutorModel
		fields = ['id', 'usuarioId', 'nomePerfil', 'estado', 'cidade', 'pontuacao', 'fotoURL', 'especialidades']
		read_only_fields = ['usuarioId', 'nomePerfil', 'estado', 'cidade', 'pontuacao', 'fotoURL']

	def get_especialidades(self, obj):
		contem_queryset = ContemModel.objects.filter(tutorId=obj)
		especialidades = [item.especialidadeId for item in contem_queryset]
		return EspecialidadeSerializer(especialidades, many=True).data

	def get_nomePerfil(self, obj):
		return obj.usuarioId.nomePerfil

	def get_estado(self, obj):
		return obj.usuarioId.estado

	def get_cidade(self, obj):
		return obj.usuarioId.cidade

	def get_pontuacao(self, obj):
		return obj.usuarioId.pontuacao

	def get_fotoURL(self, obj):
		return UsuarioUtils.get_fotoUrl(obj.usuarioId.email, self.context.get('request'))


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
