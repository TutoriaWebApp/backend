from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers

from project.models import Usuario
from project.utils import UsuarioUtils

class UsuarioSerializer(serializers.ModelSerializer):
	fotoURL = serializers.SerializerMethodField()
	foto = serializers.ImageField(write_only=True, required=False)

	class Meta:
		model = Usuario
		fields = [
			'email',
			'nomePerfil',
			'estado',
			'cidade',
			'aniversario',
			'pontuacao',
			'fotoURL',
			'foto'
		]
		read_only_fields = ['pontuacao', 'fotoURL']

	def create(self):
		"""
		Mensagem de erro caso queira utilizar esta rota para POST
		"""
		raise serializers.ValidationError(
			"Criação de usuário não permitida por esta rota."
		)

	def get_fotoURL(self, obj):
		"""
		Retorna se o Usuário tem uma foto
		"""
		return UsuarioUtils.get_fotoUrl(obj.email, self.context.get('request'))

	def update(self, instance, validated_data):
		"""
		Atualiza os dados do Usuário logado
		"""
		request = self.context.get('request')
		if instance != request.user:
			raise serializers.ValidationError(
				"Você não tem permissão para atualizar outros usuários."
			)

		foto_arquivo = validated_data.pop('foto', None)

		if foto_arquivo:
			UsuarioUtils.set_fotoUrl(instance.email, foto_arquivo)

		return super().update(instance, validated_data)




class UsuarioRegistroSerializer(serializers.ModelSerializer):
	password = serializers.CharField(write_only=True, required=True, style={'input_type': 'password'})
	foto = serializers.ImageField(write_only=True, required=False)

	class Meta:
		model = Usuario
		fields = [
			'email',
			'password',
			'nomePerfil',
			'estado',
			'cidade',
			'aniversario',
			'foto'
		]

	def create(self, validated_data):
		foto_file = validated_data.pop('foto', None)

		user = Usuario.objects.create_user(**validated_data)

		if foto_file:
			UsuarioUtils.set_fotoUrl(user.email, foto_file)

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
