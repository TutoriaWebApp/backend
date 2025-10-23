from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from project.models import *
from project.serializers import *

class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
    permission_classes = [IsAuthenticated]

class ConquistaViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Conquista.objects.all()
    serializer_class = ConquistaSerializer
    # permission_classes = [IsAuthenticated]

class consegueViewSet(viewsets.ModelViewSet):
	queryset = consegue.objects.all()
	serializer_class = consegueSerializer
	permission_classes = [IsAuthenticated]

class TutorViewSet(viewsets.ModelViewSet):
	queryset = Tutor.objects.all()
	serializer_class = TutorSerializer
	permission_classes = [IsAuthenticated]
