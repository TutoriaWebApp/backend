from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from drf_spectacular.utils import extend_schema
from django.db.models import Q
from django.utils import timezone

from project.models import MensagemModel, SolicitacaoModel
from project.views.SessaoViewSet import processar_solicitacoes_expiradas
from project.serializers.NotificacoesSerializer import ResumoNotificacoesResponseSerializer

@extend_schema(
    summary="Resumo de Notificações para o Header",
    description="Retorna em uma única chamada: contagem de mensagens não lidas, contagem de solicitações pendentes e lista resumida de solicitações resolvidas para avisos.",
    responses={200: ResumoNotificacoesResponseSerializer},
    tags=['08. Notificações']
)
class ResumoNotificacoesViewSet(viewsets.ViewSet):
    permission_classes = [IsAuthenticated]

    def list(self, request):
        user = request.user
        processar_solicitacoes_expiradas()
        agora = timezone.localtime(timezone.now())

        mensagens_nao_lidas = MensagemModel.objects.filter(
            Q(chatId__usuarioId=user) | Q(chatId__tutorId__usuarioId=user),
            lida=False
        ).exclude(usuarioId=user).count()

        solicitacoes_tutor_pendentes = SolicitacaoModel.objects.filter(
            agendaId__tutorId__usuarioId=user,
            estado=SolicitacaoModel.EstadoSolicitacao.PENDENTE
        ).filter(
            Q(dataPretendida__gt=agora.date()) |
            Q(dataPretendida=agora.date(), agendaId__horarioInicio__gt=agora.time())
        ).count()

        solicitacoes_resolvidas_aprendiz = SolicitacaoModel.objects.filter(
            usuarioId=user,
            dataPretendida__gte = agora.date(),
            estado__in=[
                SolicitacaoModel.EstadoSolicitacao.ACEITO,
                SolicitacaoModel.EstadoSolicitacao.RECUSADO
            ]
        ).select_related('agendaId__tutorId__usuarioId', 'areaId').values(
            'id',
            'estado',
            'areaId__nomeArea',
            'agendaId__tutorId__usuarioId__nomePerfil'
        )

        lista_resolvidas = [
            {
                "id": s['id'],
                "estado": s['estado'],
                "nomeArea": s['areaId__nomeArea'],
                "nomeTutor": s['agendaId__tutorId__usuarioId__nomePerfil'] or "Tutor",
            }
            for s in solicitacoes_resolvidas_aprendiz
        ]

        return Response({
            "mensagensNaoLidas": mensagens_nao_lidas,
            "solicitacoesTutorPendentes": solicitacoes_tutor_pendentes,
            "solicitacoesResolvidasAprendiz": lista_resolvidas
        })
