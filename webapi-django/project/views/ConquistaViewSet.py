from datetime import timedelta
from django.utils import timezone
from django.shortcuts import get_object_or_404
from rest_framework import viewsets, generics
from rest_framework.permissions import IsAuthenticated

from project.models import *
from project.serializers import *

class ConquistaViewSet(viewsets.ReadOnlyModelViewSet):
	queryset = Conquista.objects.all()
	serializer_class = ConquistaSerializer

class consegueViewSet(viewsets.ModelViewSet):
	queryset = consegue.objects.all()
	serializer_class = consegueSerializer
	permission_classes = [IsAuthenticated]

class Usuario_conseguiu_Conquista(generics.ListAPIView):
	serializer_class = ConquistaUsuarioSerializer
	permission_classes = [IsAuthenticated]
	def get_queryset(self):
		usuarioId = self.kwargs['usuarioId']
		get_object_or_404(Usuario, pk=usuarioId)
		conquistas_list = Conquista.objects.filter(usuarios__pk=usuarioId)
		return conquistas_list

