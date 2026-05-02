from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator
from project.models import *

class AgendaSerializer(serializers.ModelSerializer):
	class Meta:
		model  = AgendaModel
		fields = '__all__'
		validators = [
            UniqueTogetherValidator(
                queryset=AgendaModel.objects.all(),
                fields=['tutorId', 'dia', 'horarioInicio'],
                message="Você já possui um horário cadastrado para este dia e início."
            )
        ]

class SolicitacaoSerializer(serializers.ModelSerializer):
	class Meta:
		model  = SolicitacaoModel
		fields = '__all__'
		read_only_fields = ['id', 'usuarioId', 'dataCriacao', 'validade']

class SessaoSerializer(serializers.ModelSerializer):
	class Meta:
		model  = SessaoModel
		fields = '__all__'
		read_only_fields = ['id', 'usuarioId', 'tutorId', 'areaId', 'especialidadeId', 'dataSessao', 'horaInicio', 'horaFim']
