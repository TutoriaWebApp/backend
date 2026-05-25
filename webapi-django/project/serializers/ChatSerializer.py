from rest_framework import serializers
from project.models import ChatModel, MensagemModel

class MensagemSerializer(serializers.ModelSerializer):
    class Meta:
        model = MensagemModel
        fields = '__all__'
        read_only_fields = ['id', 'horario']

class ChatSerializer(serializers.ModelSerializer):
    mensagens = MensagemSerializer(many=True, read_only=True)

    class Meta:
        model = ChatModel
        fields = ['id', 'usuarioId', 'tutorId', 'mensagens']
        read_only_fields = ['id', 'usuarioId']
