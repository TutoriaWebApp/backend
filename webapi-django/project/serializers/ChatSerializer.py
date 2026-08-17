from rest_framework import serializers
from project.models import ChatModel, TutorModel, MensagemModel
from project.utils import UsuarioUtils


class MensagemSerializer(serializers.ModelSerializer):
    ehMinha = serializers.SerializerMethodField()

    class Meta:
        model = MensagemModel
        fields = ['id', 'chatId', 'usuarioId',
                  'conteudo', 'horario', 'ehMinha']
        read_only_fields = ['id', 'usuarioId', 'horario', 'ehMinha']

    def get_ehMinha(self, obj) -> bool:
        request = self.context.get('request')
        if request and hasattr(request, 'user') and request.user.is_authenticated:
            return obj.usuarioId == request.user
        return False


class ChatSerializer(serializers.ModelSerializer):
    tutorId = serializers.PrimaryKeyRelatedField(
        queryset=TutorModel.objects.all(),
        write_only=True,
        required=False
    )
    usuarioId = serializers.SerializerMethodField()
    nomePessoa = serializers.SerializerMethodField()
    fotoURL = serializers.SerializerMethodField()
    ultimaMensagem = serializers.SerializerMethodField()
    horarioUltimaMensagem = serializers.SerializerMethodField()
    mensagensNaoLidas = serializers.SerializerMethodField()

    class Meta:
        model = ChatModel
        fields = [
            'id',
            'tutorId',
            'usuarioId',
            'nomePessoa',
            'fotoURL',
            'ultimaMensagem',
            'horarioUltimaMensagem',
            'mensagensNaoLidas'
        ]
        read_only_fields = [
            'id',
            'usuarioId',
            'nomePessoa',
            'fotoURL',
            'ultimaMensagem',
            'horarioUltimaMensagem',
            'mensagensNaoLidas'
        ]

    def _get_outro_usuario(self, obj):
        request = self.context.get('request')
        if not request or not hasattr(request, 'user'):
            return obj.tutorId.usuarioId

        if obj.usuarioId == request.user:
            return obj.tutorId.usuarioId
        return obj.usuarioId

    def _get_ultima_mensagem_obj(self, obj):
        if not hasattr(obj, '_cached_ultima_mensagem'):
            obj._cached_ultima_mensagem = obj.mensagens.order_by('-horario', '-id').first()
        return obj._cached_ultima_mensagem

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

    def get_ultimaMensagem(self, obj):
        msg = self._get_ultima_mensagem_obj(obj)
        return msg.conteudo if msg else None

    def get_horarioUltimaMensagem(self, obj):
        msg = self._get_ultima_mensagem_obj(obj)
        return msg.horario.isoformat() if msg else None
    
    def get_mensagensNaoLidas(self, obj) -> int:
        request = self.context.get('request')
        if not request or not hasattr(request, 'user') or not request.user.is_authenticated:
            return 0

        return obj.mensagens.filter(lida=False).exclude(usuarioId=request.user).count()