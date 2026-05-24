from drf_spectacular.utils import extend_schema
from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.db.models import Q
from rest_framework.exceptions import ValidationError

from project.models import ChatModel, MensagemModel, TutorModel
from project.serializers import ChatSerializer, MensagemSerializer

@extend_schema(
    summary="Chat entre Aluno e Tutor",
    description="Este endpoint gerencia os chats entre alunos e tutores.",
    tags=['06. Chat']
)
class ChatViewSet(viewsets.ModelViewSet):
    serializer_class = ChatSerializer
    permission_classes = [IsAuthenticated]
    http_method_names = ['get', 'post', 'delete']

    def get_queryset(self):
        user = self.request.user
        return ChatModel.objects.filter(
            Q(usuarioId=user) | Q(tutorId__usuarioId=user)
        )

    def perform_create(self, serializer):
        user = self.request.user
        tutor_id = self.request.data.get('tutorId')

        try:
            tutor = TutorModel.objects.get(id=tutor_id)
            if tutor.usuarioId == user:
                raise ValidationError({"mensagem": "Você não pode iniciar um chat consigo mesmo."})
        except TutorModel.DoesNotExist:
            raise ValidationError({"mensagem": "Tutor não encontrado."})

        serializer.save(usuarioId=user)

@extend_schema(
    summary="Mensagens do Chat",
    description="Este endpoint permite o envio e visualização de mensagens em um chat.",
    tags=['06. Chat']
)
class MensagemViewSet(viewsets.ModelViewSet):
    serializer_class = MensagemSerializer
    permission_classes = [IsAuthenticated]
    http_method_names = ['get', 'post']

    def get_queryset(self):
        user = self.request.user
        return MensagemModel.objects.filter(
            Q(chatId__usuarioId=user) | Q(chatId__tutorId__usuarioId=user)
        )

    def perform_create(self, serializer):
        chat_id = self.request.data.get('chatId')
        try:
            chat = ChatModel.objects.get(id=chat_id)
            user = self.request.user
            if chat.usuarioId != user and chat.tutorId.usuarioId != user:
                raise ValidationError({"mensagem": "Você não tem permissão para enviar mensagens neste chat."})
        except ChatModel.DoesNotExist:
            raise ValidationError({"mensagem": "Chat não encontrado."})

        serializer.save()
