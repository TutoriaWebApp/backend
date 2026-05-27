import json
from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers

from project.models import *
from project.serializers.TutorSerializer import TutorSerializer
from project.utils import UsuarioUtils


class UsuarioSerializer(serializers.ModelSerializer):
	fotoURL = serializers.SerializerMethodField()
	foto = serializers.ImageField(
	    allow_null=True, write_only=True, required=False)
	perfilTutor = serializers.SerializerMethodField()

	class Meta:
		model = UsuarioModel
		fields = [
			'id',
			'email',
			'nomePerfil',
			'estado',
			'cidade',
			'aniversario',
			'pontuacao',
			'fotoURL',
			'foto',
			'sobremim',
			'notaAvaliacao',
			'perfilTutor',
		]
		read_only_fields = ['pontuacao', 'fotoURL', 'notaAvaliacao', 'perfilTutor']

	def create(self, validated_data):
		raise serializers.ValidationError(
			"Criação de usuário não permitida por esta rota."
		)

	def get_fotoURL(self, obj):
		request = self.context.get('request')
		return UsuarioUtils.get_fotoUrl(obj.email, request)

	def get_perfilTutor(self, obj):
		request = self.context.get('request')
		usuarioId = request.user.id
		t_tutor = TutorModel.objects.filter(usuarioId=usuarioId).first()
		serializer = TutorSerializer(t_tutor, context=self.context)
		return serializer.data if t_tutor else None

	def update(self, instance, validated_data):
		foto_arquivo = validated_data.pop('foto', None)

		if foto_arquivo:
			UsuarioUtils.set_fotoUrl(instance.email, foto_arquivo)

		return super().update(instance, validated_data)


class UsuarioPublicoSerializer(serializers.ModelSerializer):
	fotoURL = serializers.SerializerMethodField()

	class Meta:
		model = UsuarioModel
		fields = [
			'id',
			'nomePerfil',
			'estado',
			'cidade',
			'pontuacao',
			'fotoURL',
			'sobremim',
			'notaAvaliacao',
		]
		read_only_fields = ['id', 'email', 'nomePerfil', 'estado',
		    'cidade', 'pontuacao', 'fotoURL', 'sobremim', 'notaAvaliacao']

	def get_fotoURL(self, obj):
		return UsuarioUtils.get_fotoUrl(obj.email, self.context.get('request'))


class UsuarioRegistroSerializer(serializers.ModelSerializer):
	password = serializers.CharField(write_only=True, required=True, style={
	                                 'input_type': 'password'})
	foto = serializers.ImageField(write_only=True, required=False)
	especialidades = serializers.ListField(
	    child=serializers.IntegerField(), write_only=True, required=False)
	agendas = serializers.CharField(write_only=True, required=False)

	class Meta:
		model = UsuarioModel
		fields = [
			'email',
			'password',
			'nomePerfil',
			'estado',
			'cidade',
			'aniversario',
			'foto',
			'sobremim',
			'especialidades',
			'agendas',
		]

	def create(self, validated_data):
		foto_file = validated_data.pop('foto', None)
		especialidades_data = validated_data.pop('especialidades', [])
		agendas_string = validated_data.pop('agendas', '[]')

		user = UsuarioModel.objects.create_user(**validated_data)

		if foto_file:
			UsuarioUtils.set_fotoUrl(user.email, foto_file)

		if especialidades_data:
			tutor = TutorModel.objects.create(usuarioId=user)
			for especialidade_id in especialidades_data:
				# print(especialidade_id)
				try:
					especialidade = EspecialidadeModel.objects.get(pk=especialidade_id)
					ContemModel.objects.create(tutorId=tutor, especialidadeId=especialidade)
				except EspecialidadeModel.DoesNotExist:
					continue


				try:
					agendas_lista = json.loads(agendas_string)

					for agenda_data in agendas_lista:
						try:
							AgendaModel.objects.create(
								tutorId=tutor,
								dia=agenda_data.get('dia'),
								horarioInicio=agenda_data.get('horarioInicio'),
								horarioFim=agenda_data.get('horarioFim')
							)
						except Exception:
							continue
				except Exception as e:
					print(f"Erro ao decodificar a string de agendas: {e}")

		return user




class UsuarioAlteraSenhaSerializer(serializers.Serializer):
	senhaAntiga = serializers.CharField(required=True, write_only=True)
	senhaAtual = serializers.CharField(required=True, write_only=True)

	def validate_senhaAntiga(self, value):
		user = self.context['request'].user
		if not user.check_password(value):
			raise serializers.ValidationError("A senha antiga esta incorreta.")
		return value

	def validate_senhaAtual(self, value):
		validate_password(value)
		return value
