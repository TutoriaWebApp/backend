from rest_framework import viewsets, generics
from rest_framework.permissions import IsAuthenticated

from project.models import *
from project.serializers import *

class SessaoViewSet(viewsets.ModelViewSet):
	queryset = Sessao.objects.all()
	serializer_class = SessaoSerializer
	permission_classes = [IsAuthenticated]
