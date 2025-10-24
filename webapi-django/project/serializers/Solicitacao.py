from rest_framework import serializers
from project.models import Solicitacao

class SolicitacaoSerializer(serializers.ModelSerializer):
	class Meta:
		model  = Solicitacao
		fields = ['usuarioId', 'sessaoId', 'estado']
