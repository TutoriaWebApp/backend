from rest_framework import viewsets
from project.models import Usuario, Conquista, consegue
from project.serializers import UsuarioSerializer, ConquistaSerializer, consegueSerializer
from rest_framework.permissions import IsAuthenticated

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
