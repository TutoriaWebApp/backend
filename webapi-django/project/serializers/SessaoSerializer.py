from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator
from project.models import *
from project.utils import UsuarioUtils

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
	usuarioId = serializers.HiddenField(default=serializers.CurrentUserDefault())

	nomeArea = serializers.ReadOnlyField(source='areaId.nomeArea')
	nomeEspecialidade = serializers.ReadOnlyField(source='especialidadeId.nomeEspecialidade')
	nomeUsuario = serializers.ReadOnlyField(source='usuarioId.nomePerfil')
	nomeTutor = serializers.ReadOnlyField(source='agendaId.tutorId.usuarioId.nomePerfil')
	horarioInicio = serializers.ReadOnlyField(source='agendaId.horarioInicio')
	horarioFim = serializers.ReadOnlyField(source='agendaId.horarioFim')

	fotoAprendizURL = serializers.SerializerMethodField()
	fotoTutorURL = serializers.SerializerMethodField()

	class Meta:
		model  = SolicitacaoModel
		fields = '__all__'
		read_only_fields = ['id', 'usuarioId', 'dataCriacao', 'validade']

		validators = [
				UniqueTogetherValidator(
					queryset=SolicitacaoModel.objects.all(),
					fields=['usuarioId', 'agendaId', 'dataPretendida'],
					message="Você já enviou uma solicitação para este horário nesta data específica."
				)
		]

	def get_fotoAprendizURL(self, obj):
		request = self.context.get('request')
		if obj.usuarioId and hasattr(obj.usuarioId, 'email'):
			return UsuarioUtils.get_fotoUrl(obj.usuarioId.email, request)
		return None

	def get_fotoTutorURL(self, obj):
		request = self.context.get('request')
		if obj.agendaId and obj.agendaId.tutorId and obj.agendaId.tutorId.usuarioId:
			tutor_user = obj.agendaId.tutorId.usuarioId
			if hasattr(tutor_user, 'email'):
				return UsuarioUtils.get_fotoUrl(tutor_user.email, request)
		return None

class SessaoSerializer(serializers.ModelSerializer):
	nomeArea = serializers.ReadOnlyField(source='areaId.nomeArea')
	nomeEspecialidade = serializers.ReadOnlyField(source='especialidadeId.nomeEspecialidade')
	nomeUsuario = serializers.ReadOnlyField(source='usuarioId.nomePerfil')
	nomeTutor = serializers.ReadOnlyField(source='tutorId.usuarioId.nomePerfil')
	fotoAprendizURL = serializers.SerializerMethodField()
	fotoTutorURL = serializers.SerializerMethodField()

	class Meta:
		model  = SessaoModel
		fields = '__all__'
		read_only_fields = ['id', 'usuarioId', 'tutorId', 'areaId', 'especialidadeId', 'dataSessao', 'horarioInicio', 'horarioFim']

	def get_fotoAprendizURL(self, obj):
		request = self.context.get('request')
		if obj.usuarioId and hasattr(obj.usuarioId, 'email'):
			return UsuarioUtils.get_fotoUrl(obj.usuarioId.email, request)
		return None

	def get_fotoTutorURL(self, obj):
		request = self.context.get('request')
		if obj.tutorId and obj.tutorId.usuarioId and hasattr(obj.tutorId.usuarioId, 'email'):
			return UsuarioUtils.get_fotoUrl(obj.tutorId.usuarioId.email, request)
		return None