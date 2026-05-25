from rest_framework import serializers
from project.models import *

class AvaliacaoAprendizSerializer(serializers.ModelSerializer):
	class Meta:
		model  = AvaliacaoAprendizModel
		fields = '__all__'

class AvaliacaoTutorSerializer(serializers.ModelSerializer):
	class Meta:
		model  = AvaliacaoTutorModel
		fields = '__all__'

class SessaoPendenteAvaliacaoSerializer(serializers.Serializer):
	sessaoId = serializers.IntegerField(source='id')
	dataSessao = serializers.DateField()
	horarioInicio = serializers.TimeField()
	tutorNome = serializers.CharField(source='tutorId.usuarioId.nomePerfil', read_only=True)
	aprendizNome = serializers.CharField(source='usuarioId.nomePerfil', read_only=True)
	tipoPendente = serializers.CharField() # 'APRENDIZ' ou 'TUTOR'
