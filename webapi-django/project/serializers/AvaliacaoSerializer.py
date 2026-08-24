from rest_framework import serializers
from project.models import *
from project.utils import UsuarioUtils

class AvaliacaoAprendizSerializer(serializers.ModelSerializer):
	fotoURL = serializers.SerializerMethodField()
	nomeUsuario = serializers.ReadOnlyField(source='sessaoId.tutorId.usuarioId.nomePerfil')
	usuarioAvaliadorId = serializers.ReadOnlyField(source='sessaoId.tutorId.usuarioId.id')

	class Meta:
		model  = AvaliacaoAprendizModel
		fields = '__all__'

	def get_fotoURL(self, obj):
		request = self.context.get('request')
		if obj.sessaoId and obj.sessaoId.tutorId and obj.sessaoId.tutorId.usuarioId:
			return UsuarioUtils.get_fotoUrl(obj.sessaoId.tutorId.usuarioId.email, request)
		return None

class AvaliacaoTutorSerializer(serializers.ModelSerializer):
	fotoURL = serializers.SerializerMethodField()
	nomeUsuario = serializers.ReadOnlyField(source='sessaoId.usuarioId.nomePerfil')
	usuarioAvaliadorId = serializers.ReadOnlyField(source='sessaoId.usuarioId.id')

	class Meta:
		model  = AvaliacaoTutorModel
		fields = '__all__'

	def get_fotoURL(self, obj):
		request = self.context.get('request')
		if obj.sessaoId and obj.sessaoId.usuarioId and hasattr(obj.sessaoId.usuarioId, 'email'):
			return UsuarioUtils.get_fotoUrl(obj.sessaoId.usuarioId.email, request)
		return None

class SessaoPendenteAvaliacaoSerializer(serializers.Serializer):
	sessaoId = serializers.IntegerField(source='id')
	dataSessao = serializers.DateField()
	horarioInicio = serializers.TimeField()

	usuarioAvaliadoId = serializers.SerializerMethodField()
	nome = serializers.SerializerMethodField()
	fotoURL = serializers.SerializerMethodField()

	nomeArea = serializers.ReadOnlyField(source='areaId.nomeArea')
	nomeEspecialidade = serializers.ReadOnlyField(source='especialidadeId.nomeEspecialidade')

	tipoPendente = serializers.CharField()

	def get_usuarioAvaliadoId(self, obj):
		if getattr(obj, 'tipoPendente', None) == 'APRENDIZ':
			return obj.tutorId.usuarioId.id
		return obj.usuarioId.id

	def get_nome(self, obj):
		if getattr(obj, 'tipoPendente', None) == 'APRENDIZ':
			return obj.tutorId.usuarioId.nomePerfil
		return obj.usuarioId.nomePerfil

	def get_fotoURL(self, obj):
		request = self.context.get('request')
		if getattr(obj, 'tipoPendente', None) == 'APRENDIZ':
			usuario_avaliado = obj.tutorId.usuarioId
		else:
			usuario_avaliado = obj.usuarioId

		if usuario_avaliado and hasattr(usuario_avaliado, 'email'):
			return UsuarioUtils.get_fotoUrl(usuario_avaliado.email, request)
		return None