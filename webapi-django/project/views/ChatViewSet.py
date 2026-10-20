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

class ChatViewSet(viewsets.ModelViewSet):
    serializer_class = ChatSerializer
    permission_classes = [IsAuthenticated]
    http_method_names = ['get', 'post', 'delete']

    @extend_schema(
        summary="Lista as conversas do usuário logado",
        description=(
            "Este endpoint retorna a lista de todas as conversas vinculadas ao usuário logado."
        ),
        responses={200: ChatSerializer(many=True)},
        tags=['09. Mensagens']
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @extend_schema(
        summary="Detalha uma conversa por ID",
        description="Recebe o ID de uma conversa e retorna suas informações detalhadas.",
        responses={200: ChatSerializer},
        tags=['09. Mensagens']
    )
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @extend_schema(
        summary="Inicia uma nova conversa com um tutor",
        description=(
            "Permite iniciar um novo chat informando o 'tutorId' no corpo da requisição.\n\n"
            "Se já existir um chat criado entre o aprendiz e o tutor fornecido, o endpoint "
            "reaproveita a conversa existente para evitar duplicidade."
        ),
        request=ChatSerializer,
        responses={201: ChatSerializer},
        tags=['09. Mensagens']
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @extend_schema(
        summary="Remove uma conversa por ID",
        description="Remove uma conversa dos registros do banco de dados a partir do ID de uma conversa fornecido.",
        responses={204: None},
        tags=['09. Mensagens']
    )
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)

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

class MensagemViewSet(viewsets.ModelViewSet):
    serializer_class = MensagemSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = MensagemPagination
    # 1. Permite o método PATCH na viewset:
    http_method_names = ['get', 'post', 'patch']

    @extend_schema(
        summary="Lista mensagens de uma conversa",
        description=(
            "Este endpoint lista as mensagens de conversas nos quais o usuário logado participa.\n\n"
            "Pode-se utilizar o parâmetro de query 'chatId' na URL para filtrar apenas o histórico de mensagens "
            "de uma conversa específica."
        ),
        responses={200: MensagemSerializer(many=True)},
        tags=['09. Mensagens'],
        parameters=[
            OpenApiParameter(
                name='chatId', 
                description='ID do Chat para filtrar as mensagens daquela conversa', 
                required=False, 
                type=int
            ),
        ]
    )
    def list(self, request, *args, **kwargs):
        response = super().list(request, *args, **kwargs)
        if isinstance(response.data, dict) and 'results' in response.data:
            response.data['results'] = list(reversed(response.data['results']))
        return response

    @extend_schema(
        summary="Detalha uma mensagem por ID",
        description="Recebe o ID de uma mensagem específica e retorna seus detalhes.",
        responses={200: MensagemSerializer},
        tags=['09. Mensagens'],
        parameters=[]  # Zera os parâmetros de query da busca geral no GET por ID
    )
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @extend_schema(
        summary="Envia uma nova mensagem no chat",
        description=(
            "Envia uma nova mensagem de texto em uma conversa.\n\n"
            "O remetente é associado automaticamente através do usuário autenticado."
        ),
        request=MensagemSerializer,
        responses={201: MensagemSerializer},
        tags=['09. Mensagens'],
        parameters=[]  # Zera os parâmetros de query no POST
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @extend_schema(
        summary="Atualiza parcialmente uma mensagem por ID",
        description="Permite a edição parcial do conteúdo de uma mensagem enviada anteriormente pelo ID especificado.",
        request=MensagemSerializer,
        responses={200: MensagemSerializer},
        tags=['09. Mensagens'],
        parameters=[]
    )
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)

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
        summary="Marca mensagens de um chat como lidas",
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
        tags=['09. Mensagens']
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
