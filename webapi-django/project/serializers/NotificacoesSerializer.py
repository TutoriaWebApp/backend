from rest_framework import serializers
from drf_spectacular.utils import extend_schema_serializer, OpenApiExample

@extend_schema_serializer(
    examples=[
        OpenApiExample(
            'Exemplo de Resumo de Notificações',
            value={
                "mensagensNaoLidas": 3,
                "solicitacoesTutorPendentes": 1,
                "solicitacoesResolvidasAprendiz": [
                    {
                        "id": 1,
                        "estado": "ACEITO",
                        "nomeArea": "Matemática",
                        "nomeTutor": "Igor Gomes"
                    }
                ]
            },
            response_only=True,
        )
    ]
)
class ResumoNotificacoesResponseSerializer(serializers.Serializer):
    mensagensNaoLidas = serializers.IntegerField()
    solicitacoesTutorPendentes = serializers.IntegerField()
    solicitacoesResolvidasAprendiz = serializers.ListField(
        child=serializers.DictField()
    )


class SolicitacaoResolvidaItemSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    estado = serializers.ChoiceField(choices=["ACEITO", "RECUSADO"])
    nomeArea = serializers.CharField()
    nomeTutor = serializers.CharField()