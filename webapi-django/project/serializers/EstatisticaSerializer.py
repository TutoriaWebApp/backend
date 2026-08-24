from rest_framework import serializers

class EstatisticaProgressoSerializer(serializers.Serializer):
    sessoesConcluidas = serializers.IntegerField(
        help_text="Quantidade total de sessões já concluídas pelo usuário"
    )
    conquistasDesbloqueadas = serializers.IntegerField(
        help_text="Quantidade total de conquistas obtidas"
    )
    pontos = serializers.IntegerField(
        help_text="Pontuação total acumulada"
    )