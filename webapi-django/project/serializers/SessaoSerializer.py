from rest_framework import serializers
from project.models import *

class AgendaSerializer(serializers.ModelSerializer):
	class Meta:
		model  = AgendaModel
		fields = '__all__'

class SolicitacaoSerializer(serializers.ModelSerializer):
	class Meta:
		model  = SolicitacaoModel
		fields = '__all__'
		read_only_fields = ['id', 'usuarioId', 'dataCriacao', 'validade', 'estado']

class SessaoSerializer(serializers.ModelSerializer):
	class Meta:
		model  = SessaoModel
		fields = '__all__'
