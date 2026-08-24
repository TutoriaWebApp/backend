from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.utils import timezone
from django.db.models import Q
from drf_spectacular.utils import extend_schema

from project.models import SessaoModel
from project.serializers import EstatisticaProgressoSerializer

class ProgressoUsuarioView(APIView):
    permission_classes = [IsAuthenticated]

    @extend_schema(
        summary="Progresso e Estatísticas do Usuário",
        description="Retorna o consolidado de sessões concluídas, conquistas desbloqueadas e pontuação total.",
        responses={200: EstatisticaProgressoSerializer},
        tags=['01. Usuário']
    )
    def get(self, request):
        user = request.user
        agora = timezone.localtime(timezone.now())
        hoje = agora.date()
        hora_atual = agora.time()

        sessoes_concluidas = SessaoModel.objects.filter(
            Q(usuarioId=user) | Q(tutorId__usuarioId=user)
        ).filter(
            Q(dataSessao__lt=hoje) | 
            Q(dataSessao=hoje, horarioFim__lte=hora_atual)
        ).count()

        conquistas_desbloqueadas = user.conquistas.count() if hasattr(user, 'conquistas') else 0

        pontos = getattr(user, 'pontuacao', 0)


        return Response({
            "sessoesConcluidas": sessoes_concluidas,
            "conquistasDesbloqueadas": conquistas_desbloqueadas,
            "pontos": pontos,
        })