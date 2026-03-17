from datetime import timedelta
from django.utils import timezone
from django.shortcuts import get_object_or_404
from rest_framework import viewsets, generics
from rest_framework.permissions import IsAuthenticated

from project.models import *
from project.serializers import *

class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

class Usuario_conseguiu_Conquista(generics.ListAPIView):
	serializer_class = ConquistaUsuarioSerializer

	def get_queryset(self):
		usuarioId = self.kwargs['usuarioId']
		get_object_or_404(Usuario, pk=usuarioId)
		conquistas_list = Conquista.objects.filter(usuarios__pk=usuarioId)
		return conquistas_list

class ConquistaViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Conquista.objects.all()
    serializer_class = ConquistaSerializer

class consegueViewSet(viewsets.ModelViewSet):
	queryset = consegue.objects.all()
	serializer_class = consegueSerializer
	permission_classes = [IsAuthenticated]

class TutorViewSet(viewsets.ModelViewSet):
	queryset = Tutor.objects.all()
	serializer_class = TutorSerializer
	permission_classes = [IsAuthenticated]

class SessaoViewSet(viewsets.ModelViewSet):
	queryset = Sessao.objects.all()
	serializer_class = SessaoSerializer
	permission_classes = [IsAuthenticated]

class SolicitacaoViewSet(viewsets.ModelViewSet):
	queryset = Solicitacao.objects.all()
	serializer_class = SolicitacaoSerializer
	permission_classes = [IsAuthenticated]

	def perform_create(self, serializer):
		logged_user = self.request.user
		dataCriacao = timezone.now()
		validade = dataCriacao + timedelta(hours=24)
		serializer.save(
			usuarioId=logged_user,
			dataCriacao=dataCriacao,
			validade=validade,
			estado=Solicitacao.EstadoSolicitacao.PENDENTE
		)
