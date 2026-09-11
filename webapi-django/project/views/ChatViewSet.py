from drf_spectacular.utils import extend_schema, OpenApiParameter
from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated
from django.db.models import Q
from rest_framework.exceptions import ValidationError
from rest_framework.pagination import PageNumberPagination
from rest_framework.decorators import action
from rest_framework.response import Response

from project.models import ChatModel, MensagemModel, TutorModel
from project.serializers.ChatSerializer import ChatSerializer, MensagemSerializer

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
        ).select_related('usuarioId', 'tutorId__usuarioId')

    def perform_create(self, serializer):
        user = self.request.user
        tutor_id = self.request.data.get('tutorId')

        if not tutor_id:
            raise ValidationError({"mensagem": "O campo tutorId é obrigatório."})

        try:
            tutor = TutorModel.objects.get(id=tutor_id)
            if tutor.usuarioId == user:
                raise ValidationError({"mensagem": "Você não pode iniciar um chat consigo mesmo."})
        except TutorModel.DoesNotExist:
            raise ValidationError({"mensagem": "Tutor não encontrado."})

        chat_existente = ChatModel.objects.filter(usuarioId=user, tutorId=tutor).first()
        if chat_existente:
            serializer.instance = chat_existente
            return

        serializer.save(usuarioId=user, tutorId=tutor)

class MensagemPagination(PageNumberPagination):
    page_size = 20
    page_size_query_param = 'page_size'
    max_page_size = 100

@extend_schema(
    summary="Mensagens do Chat",
    description="Este endpoint permite o envio e visualização de mensagens em um chat.",
    tags=['06. Chat'],
    parameters=[
        OpenApiParameter(
            name='chatId', 
            description='ID do Chat para filtrar apenas as mensagens daquela conversa', 
            required=False, 
            type=int
        ),
    ]
)
class MensagemViewSet(viewsets.ModelViewSet):
    serializer_class = MensagemSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = MensagemPagination
    # 1. Permite o método PATCH na viewset:
    http_method_names = ['get', 'post', 'patch']

    def get_queryset(self):
        user = self.request.user
        queryset = MensagemModel.objects.filter(
            Q(chatId__usuarioId=user) | Q(chatId__tutorId__usuarioId=user)
        ).select_related('usuarioId')

        chat_id = self.request.query_params.get('chatId') or self.request.query_params.get('chat')
        if chat_id is not None:
            queryset = queryset.filter(chatId=chat_id)

        return queryset.order_by('-horario', '-id')

    @extend_schema(
        summary="Marcar mensagens de um chat como lidas",
        description="Marca todas as mensagens recebidas em determinado chat como lidas pelo usuário autenticado.",
        request={
            'application/json': {
                'type': 'object',
                'properties': {
                    'chatId': {'type': 'integer', 'example': 1}
                },
                'required': ['chatId']
            }
        },
        responses={
            200: {
                'type': 'object',
                'properties': {
                    'mensagem': {'type': 'string', 'example': 'Mensagens marcadas como lidas.'}
                }
            },
            400: {
                'type': 'object',
                'properties': {
                    'mensagem': {'type': 'string', 'example': 'chatId é obrigatório.'}
                }
            }
        },
        tags=['06. Chat']
    )
    @action(detail=False, methods=['patch'], url_path='marcar-lidas')
    def marcar_como_lidas(self, request):
        chat_id = request.data.get('chatId')
        if not chat_id:
            return Response({"mensagem": "chatId é obrigatório."}, status=status.HTTP_400_BAD_REQUEST)

        MensagemModel.objects.filter(
            chatId=chat_id,
            lida=False
        ).exclude(usuarioId=request.user).update(lida=True)

        return Response({"mensagem": "Mensagens marcadas como lidas."}, status=status.HTTP_200_OK)

        return Response({"mensagem": "Mensagens marcadas como lidas."}, status=status.HTTP_200_OK)

    def list(self, request, *args, **kwargs):
        response = super().list(request, *args, **kwargs)
        if isinstance(response.data, dict) and 'results' in response.data:
            response.data['results'] = list(reversed(response.data['results']))
        return response

    def perform_create(self, serializer):
        chat_id = self.request.data.get('chatId')
        user = self.request.user

        try:
            chat = ChatModel.objects.get(id=chat_id)
            if chat.usuarioId != user and chat.tutorId.usuarioId != user:
                raise ValidationError({"mensagem": "Você não tem permissão para enviar mensagens neste chat."})
        except ChatModel.DoesNotExist:
            raise ValidationError({"mensagem": "Chat não encontrado."})

        serializer.save(usuarioId=user)
