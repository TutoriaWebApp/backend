from rest_framework import serializers
from project.models import ConquistaModel, consegueModel

class ConquistaSerializer(serializers.ModelSerializer):
	class Meta:
		model  = ConquistaModel
		fields = '__all__'

class ConquistaUsuarioSerializer(serializers.ModelSerializer):
	class Meta:
		model  = ConquistaModel
		fields = ['titulo', 'descricao', 'urlImagem', 'pontos']

class consegueSerializer(serializers.ModelSerializer):
	class Meta:
		model = consegueModel
		fields = '__all__'
