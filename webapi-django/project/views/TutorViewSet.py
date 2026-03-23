from rest_framework import viewsets, generics
from rest_framework.permissions import IsAuthenticated

from project.models import *
from project.serializers import *

class TutorViewSet(viewsets.ModelViewSet):
	queryset = TutorModel.objects.all()
	serializer_class = TutorSerializer
	permission_classes = [IsAuthenticated]
