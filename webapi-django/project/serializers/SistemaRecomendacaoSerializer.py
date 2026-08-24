from rest_framework import serializers
from .TutorSerializer import TutorSerializer
from ..models.TutorModel import TutorModel

class SistemaRecomendacaoSerializer(serializers.ModelSerializer):
	score = serializers.FloatField(read_only=True)
	perfilTutor = TutorSerializer(source='*', read_only=True)

	class Meta:
		model = TutorModel
		fields = ['id', 'score', 'perfilTutor']
