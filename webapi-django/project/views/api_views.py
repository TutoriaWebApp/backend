from rest_framework import viewsets
from project.models import Usuario
from project.serializers import UsuarioSerializer
# Adicione suas permissões aqui, ex: from rest_framework.permissions import IsAuthenticated

class UsuarioViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint que permite que usuários sejam visualizados.
    """
    queryset = Usuario.objects.all().order_by('-date_joined')
    serializer_class = UsuarioSerializer
    # permission_classes = [IsAuthenticated]
