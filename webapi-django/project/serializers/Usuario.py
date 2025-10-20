from rest_framework import serializers
from project.models import Usuario

class UsuarioSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, style={'input_type': 'password'})

    class Meta:
        model = Usuario
        fields = [
            'id',
            'email',
            'password',
            'nomePerfil',
            'pontuacao',
            'cidade',
            'estado',
            'urlFoto'
        ]
        read_only_fields = ['pontuacao']

    def create(self, validated_data):
        user = Usuario.objects.create_user(
            email=validated_data['email'],
            nomePerfil=validated_data['nomePerfil'],
            cidade=validated_data['cidade'],
            estado=validated_data['estado'],
            urlFoto=validated_data['urlFoto'],
            password=validated_data['password']
        )
        return user
