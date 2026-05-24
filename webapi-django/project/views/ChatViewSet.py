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

@extend_schema(
    summary="Mensagens do Chat",
    description="Este endpoint permite o envio e visualização de mensagens em um chat.",
    tags=['06. Chat']
)
class MensagemViewSet(viewsets.ModelViewSet):
    serializer_class = MensagemSerializer
    permission_classes = [IsAuthenticated]
    http_method_names = ['get', 'post']
