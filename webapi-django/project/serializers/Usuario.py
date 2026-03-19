from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers
from project.models import Usuario

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = [
            'email',
            'nomePerfil',
            'aniversario',
            'cidade',
            'estado'
        ]
        read_only_fields = ['__all__']

    def create(self):
        raise serializers.ValidationError(
            "Criação de usuário não permitida por esta rota."
		)

    def update(self, instance, validated_data):
        request = self.context.get('request')
        if instance != request.user:
             raise serializers.ValidationError(
                 "Você não tem permissão para atualizar outros usuários."
             )
        return super().update(instance, validated_data)

class UsuarioRegistroSerializer(serializers.ModelSerializer):
	password = serializers.CharField(write_only=True, required=True, style={'input_type': 'password'})

	class Meta:
		model = Usuario
		fields = [
			'email',
			'password',
			'nomePerfil',
			'aniversario',
			'cidade',
			'estado'
		]

	def create(self, validated_data):
		user = Usuario.objects.create_user(
			email=validated_data['email'],
			password=validated_data['password'],
			nomePerfil=validated_data['nomePerfil'],
			aniversario=validated_data.get('aniversario'),
			cidade=validated_data.get('cidade', ''),
			estado=validated_data.get('estado', '')
		)
		return user

class UsuarioAlteraSenhaSerializer(serializers.Serializer):
	senhaAntiga = serializers.CharField(required=True, write_only=True)
	senhaAtual = serializers.CharField(required=True, write_only=True)

	def validate_senhaAntiga(self, value):
		user = self.context['request'].user
		if not user.check_password(value):
			raise serializers.ValidationError("A senha antiga esta incorreta")
		return value

	def validate_senhaAtual(self, value):
		validate_password(value)
		return value
