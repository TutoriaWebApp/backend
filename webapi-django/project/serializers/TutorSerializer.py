from rest_framework import serializers
from project.models import *
from project.utils import UsuarioUtils


class TutorSerializer(serializers.ModelSerializer):
    especialidades = serializers.SerializerMethodField()
    areas = serializers.SerializerMethodField()
    nomePerfil = serializers.SerializerMethodField()
    estado = serializers.SerializerMethodField()
    cidade = serializers.SerializerMethodField()
    pontuacao = serializers.SerializerMethodField()
    fotoURL = serializers.SerializerMethodField()
    sobremim = serializers.SerializerMethodField()
    totalAvaliacoes = serializers.SerializerMethodField()

    class Meta:
        model = TutorModel
        fields = ['id', 'usuarioId', 'nomePerfil', 'estado', 'cidade', 'pontuacao',
                  'fotoURL', 'sobremim', 'notaAvaliacao', 'totalAvaliacoes', 'especialidades', 'areas']
        read_only_fields = ['usuarioId', 'nomePerfil', 'estado', 'cidade', 'pontuacao',
                            'fotoURL', 'sobremim', 'notaAvaliacao', 'totalAvaliacoes', 'especialidades', 'areas']

    def get_especialidades(self, obj):
        contem_queryset = ContemModel.objects.filter(
            tutorId=obj).select_related('especialidadeId')
        result = []
        for item in contem_queryset:
            data = EspecialidadeSerializer(item.especialidadeId).data
            data['contemId'] = item.id
            result.append(data)
        return result

    def get_areas(self, obj):
        areas_queryset = AreaModel.objects.filter(
            especialidades__tutores=obj).distinct()
        return AreaSerializer(areas_queryset, many=True).data

    def get_nomePerfil(self, obj):
        return obj.usuarioId.nomePerfil

    def get_estado(self, obj):
        return obj.usuarioId.estado

    def get_cidade(self, obj):
        return obj.usuarioId.cidade

    def get_pontuacao(self, obj):
        return obj.usuarioId.pontuacao

    def get_sobremim(self, obj):
        return obj.usuarioId.sobremim

    def get_fotoURL(self, obj):
        return UsuarioUtils.get_fotoUrl(obj.usuarioId.email, self.context.get('request'))

    def get_totalAvaliacoes(self, obj):
        if hasattr(obj, 'qtd_avaliacoes_tutor'):
            return obj.qtd_avaliacoes_tutor
        return obj.avaliacoes_tutor.count()

class AreaSerializer(serializers.ModelSerializer):
    class Meta:
        model = AreaModel
        fields = '__all__'


class EspecialidadeSerializer(serializers.ModelSerializer):
    class Meta:
        model = EspecialidadeModel
        fields = ['id', 'nomeEspecialidade', 'areaId']


class ContemSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContemModel
        fields = '__all__'
