from datetime import timedelta
from django.utils import timezone
from django.shortcuts import get_object_or_404
from rest_framework import viewsets, generics
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from project.models import *
from project.serializers import *

class UsuarioViewSet(viewsets.ModelViewSet):
	queryset = UsuarioModel.objects.all()
	serializer_class = UsuarioSerializer
	permission_classes = [IsAuthenticated]
	http_method_names = ['get', 'put']

class UsuarioRegistroView(generics.CreateAPIView):
	queryset = UsuarioModel.objects.all()
	serializer_class = UsuarioRegistroSerializer
	permission_classes = [AllowAny]
	http_method_names = ['post']

class UsuarioAlteraSenhaView(APIView):
	permission_classes = [IsAuthenticated] # Obrigatório estar logado

	def post(self, request, *args, **kwargs):
		serializer = UsuarioAlteraSenhaSerializer(data=request.data, context={'request': request})

		if not serializer.is_valid():
			return Response(serializer.errors, status=400)

		user = request.user
		user.set_password(serializer.validated_data['senhaAtual'])
		user.save()

		return Response({"message": "Senha alterada com sucesso!"}, status=200)

