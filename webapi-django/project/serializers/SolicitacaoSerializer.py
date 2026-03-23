from rest_framework import serializers
from project.models import SolicitacaoModel

class SolicitacaoSerializer(serializers.ModelSerializer):
	class Meta:
		model  = SolicitacaoModel
		fields = '__all__'
		read_only_fields = ['id', 'usuarioId', 'validade', 'estado']
