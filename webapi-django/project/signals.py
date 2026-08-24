import datetime
from django.db.models import Avg, Q
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.utils import timezone

from project.models.AvaliacaoModel import AvaliacaoAprendizModel, AvaliacaoTutorModel


def atualizar_nota_aprendiz(usuario):
    agora = timezone.now()
    limite_48h = agora - datetime.timedelta(hours=48)

    sessoes_com_resposta = AvaliacaoTutorModel.objects.values_list('sessaoId', flat=True)

    avaliacoes_validas = AvaliacaoAprendizModel.objects.filter(
        usuarioId=usuario
    ).filter(
        Q(dataCriacao__lte=limite_48h) | Q(sessaoId__in=sessoes_com_resposta)
    )

    media = avaliacoes_validas.aggregate(Avg('nota'))['nota__avg']
    
    usuario.notaAvaliacao = round(float(media), 1) if media is not None else 5.0
    usuario.save(update_fields=['notaAvaliacao'])


def atualizar_nota_tutor(tutor):
    agora = timezone.now()
    limite_48h = agora - datetime.timedelta(hours=48)

    sessoes_com_resposta = AvaliacaoAprendizModel.objects.values_list('sessaoId', flat=True)

    avaliacoes_validas = AvaliacaoTutorModel.objects.filter(
        tutorId=tutor
    ).filter(
        Q(dataCriacao__lte=limite_48h) | Q(sessaoId__in=sessoes_com_resposta)
    )

    media = avaliacoes_validas.aggregate(Avg('nota'))['nota__avg']
    nova_nota = round(float(media), 1) if media is not None else 5.0

    tutor.notaAvaliacao = nova_nota
    tutor.save(update_fields=['notaAvaliacao'])


@receiver([post_save, post_delete], sender=AvaliacaoAprendizModel)
def ao_salvar_avaliacao_aprendiz(sender, instance, **kwargs):
    atualizar_nota_aprendiz(instance.usuarioId)
    
    if instance.sessaoId and instance.sessaoId.tutorId:
        atualizar_nota_tutor(instance.sessaoId.tutorId)


@receiver([post_save, post_delete], sender=AvaliacaoTutorModel)
def ao_salvar_avaliacao_tutor(sender, instance, **kwargs):
    atualizar_nota_tutor(instance.tutorId)
    
    if instance.sessaoId and instance.sessaoId.usuarioId:
        atualizar_nota_aprendiz(instance.sessaoId.usuarioId)