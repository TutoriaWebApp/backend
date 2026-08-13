from rest_framework import serializers
from project.models import ChatModel, TutorModel, MensagemModel
from project.utils import UsuarioUtils

class MensagemSerializer(serializers.ModelSerializer):
    class Meta:
        model = MensagemModel
        fields = '__all__'
        read_only_fields = ['id', 'horario']

class ChatSerializer(serializers.ModelSerializer):
    tutorId = serializers.PrimaryKeyRelatedField(
        queryset=TutorModel.objects.all(),
        write_only=True,
        required=False
    )
    usuarioId = serializers.SerializerMethodField()
    nomePessoa = serializers.SerializerMethodField()
    fotoURL = serializers.SerializerMethodField()

    class Meta:
        model = ChatModel
        fields = ['id', 'tutorId', 'usuarioId', 'nomePessoa', 'fotoURL']        
        read_only_fields = ['id', 'usuarioId', 'nomePessoa', 'fotoURL']

    def _get_outro_usuario(self, obj):
        request = self.context.get('request')
        if not request or not hasattr(request, 'user'):
            return obj.tutorId.usuarioId

        if obj.usuarioId == request.user:
            return obj.tutorId.usuarioId
        return obj.usuarioId

    def get_usuarioId(self, obj):
        outro_usuario = self._get_outro_usuario(obj)
        return outro_usuario.id if outro_usuario else None

    def get_nomePessoa(self, obj):
        outro_usuario = self._get_outro_usuario(obj)
        return outro_usuario.nomePerfil if outro_usuario else ""

    def get_fotoURL(self, obj):
        outro_usuario = self._get_outro_usuario(obj)
        if not outro_usuario:
            return None
        return UsuarioUtils.get_fotoUrl(outro_usuario.email, self.context.get('request'))