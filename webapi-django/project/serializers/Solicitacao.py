from rest_framework import serializers
from project.models import Solicitacao

class SolicitacaoSerializer(serializers.ModelSerializer):
	class Meta:
		model  = Solicitacao
		fields = '__all__'
		read_only_fields = ['id', 'usuarioId', 'validade', 'estado']
