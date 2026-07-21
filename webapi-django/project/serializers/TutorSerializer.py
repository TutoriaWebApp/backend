from rest_framework import serializers
from project.models import *
from project.utils import UsuarioUtils, GeoLocalizacaoUtil


class TutorSerializer(serializers.ModelSerializer):
    especialidades = serializers.SerializerMethodField()
    areas = serializers.SerializerMethodField()
    nomePerfil = serializers.SerializerMethodField()
    estado = serializers.SerializerMethodField()
    cidade = serializers.SerializerMethodField()
    localizacao = serializers.SerializerMethodField()
    distancia_km = serializers.SerializerMethodField()
    pontuacao = serializers.SerializerMethodField()
    fotoURL = serializers.SerializerMethodField()
    sobremim = serializers.SerializerMethodField()
    totalAvaliacoes = serializers.SerializerMethodField()

    class Meta:
        model = TutorModel
        fields = ['id', 'usuarioId', 'nomePerfil', 'estado', 'cidade', 'localizacao', 'distancia_km', 'pontuacao', 'fotoURL', 'sobremim', 'notaAvaliacao', 'totalAvaliacoes', 'especialidades', 'areas']
        read_only_fields = ['usuarioId', 'nomePerfil', 'estado', 'cidade', 'localizacao', 'distancia_km', 'pontuacao',
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

    def get_localizacao(self, obj):
        loc = obj.usuarioId.localizacao
        if loc is None:
            return None
        if hasattr(loc, 'x') and hasattr(loc, 'y'):
            return {'longitude': loc.x, 'latitude': loc.y}
        return str(loc)

    def get_distancia_km(self, obj):
        request = self.context.get('request')
        if request and hasattr(request, 'user') and request.user and request.user.is_authenticated:
            user_loc = getattr(request.user, 'localizacao', None)
            tutor_loc = getattr(obj.usuarioId, 'localizacao', None)
            if user_loc and tutor_loc:
                dist = GeoLocalizacaoUtil.haversine_distance(user_loc, tutor_loc)
                if dist != float('inf'):
                    return round(dist, 2)
        return None

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
