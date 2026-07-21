from rest_framework import serializers
from project.models import *
from project.utils import UsuarioUtils

class AvaliacaoAprendizSerializer(serializers.ModelSerializer):
	fotoURL = serializers.SerializerMethodField()
	nomeUsuario = serializers.ReadOnlyField(source='usuarioId.nomePerfil')

	class Meta:
		model  = AvaliacaoAprendizModel
		fields = '__all__'

	def get_fotoURL(self, obj):
		request = self.context.get('request')
		if obj.usuarioId and hasattr(obj.usuarioId, 'email'):
			return UsuarioUtils.get_fotoUrl(obj.usuarioId.email, request)
		return None

class AvaliacaoTutorSerializer(serializers.ModelSerializer):
	fotoURL = serializers.SerializerMethodField()
	nomeUsuario = serializers.ReadOnlyField(source='sessaoId.usuarioId.nomePerfil')
	class Meta:
		model  = AvaliacaoTutorModel
		fields = '__all__'

	def get_fotoURL(self, obj):
		request = self.context.get('request')
        # Acessa o aprendiz da sessão que fez a crítica ao tutor
		if obj.sessaoId and obj.sessaoId.usuarioId and hasattr(obj.sessaoId.usuarioId, 'email'):
			return UsuarioUtils.get_fotoUrl(obj.sessaoId.usuarioId.email, request)
		return None

class SessaoPendenteAvaliacaoSerializer(serializers.Serializer):
	sessaoId = serializers.IntegerField(source='id')
	dataSessao = serializers.DateField()
	horarioInicio = serializers.TimeField()
	tutorNome = serializers.CharField(source='tutorId.usuarioId.nomePerfil', read_only=True)
	aprendizNome = serializers.CharField(source='usuarioId.nomePerfil', read_only=True)
	tipoPendente = serializers.CharField() # 'APRENDIZ' ou 'TUTOR'
