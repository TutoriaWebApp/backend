from drf_spectacular.utils import extend_schema
from rest_framework import viewsets, generics
from rest_framework.permissions import IsAuthenticated

from project.models import *
from project.serializers import *

@extend_schema(
	summary="Usuario tutor",
	description="Este endpoint retorna uma lista com todas as conquistas exibidas na plataforma",
	request=ConquistaSerializer,
	responses=ConquistaSerializer,
	tags=['03. Tutor']
)
class TutorViewSet(viewsets.ModelViewSet):
	queryset = TutorModel.objects.all()
	serializer_class = TutorSerializer
	permission_classes = [IsAuthenticated]
	http_method_names = ['get', 'post']
