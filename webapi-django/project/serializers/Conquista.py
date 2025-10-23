from rest_framework import serializers
from project.models import Conquista

class ConquistaSerializer(serializers.ModelSerializer):
	class Meta:
		model  = Conquista
		fields = '__all__'

class ConquistaUsuarioSerializer(serializers.ModelSerializer):
	class Meta:
		model  = Conquista
		fields = ['titulo', 'descricao', 'urlImagem', 'pontos']
