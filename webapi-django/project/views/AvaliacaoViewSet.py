from drf_spectacular.utils import extend_schema
from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from django.utils import timezone

from project.models import *
from project.serializers import *

@extend_schema(
	summary="Avaliação do Aprendiz",
	description="Este endpoint permite gerenciar as avaliações feitas pelos aprendizes sobre as sessões.",
	request=AvaliacaoAprendizSerializer,
	responses=AvaliacaoAprendizSerializer,
	tags=['06. Avaliações']
)
class AvaliacaoAprendizViewSet(viewsets.ModelViewSet):
	queryset = AvaliacaoAprendizModel.objects.all()
	serializer_class = AvaliacaoAprendizSerializer
	permission_classes = [IsAuthenticated]
	http_method_names = ['get', 'post']

@extend_schema(
	summary="Avaliação do Tutor",
	description="Este endpoint permite gerenciar as avaliações feitas sobre os tutores após as sessões.",
	request=AvaliacaoTutorSerializer,
	responses=AvaliacaoTutorSerializer,
	tags=['06. Avaliações']
)
class AvaliacaoTutorViewSet(viewsets.ModelViewSet):
	queryset = AvaliacaoTutorModel.objects.all()
	serializer_class = AvaliacaoTutorSerializer
	permission_classes = [IsAuthenticated]
	http_method_names = ['get', 'post']



@extend_schema(
	summary="Sessões Pendentes de Avaliação",
	description="Retorna as sessões que o usuário participou (como aprendiz ou tutor) e que ainda não foram avaliadas por ele.",
	responses={200: SessaoPendenteAvaliacaoSerializer(many=True)},
	tags=['06. Avaliações']
)
class PendenteAvaliacaoView(APIView):
	permission_classes = [IsAuthenticated]

	def get(self, request):
		usuario = request.user
		hoje = timezone.now().date()
		agora = timezone.now().time()

		sessoes_como_aprendiz = SessaoModel.objects.filter(
			usuarioId=usuario,
		).exclude(
			avaliacoes_aprendiz_sessao__usuarioId=usuario
		)

		try:
			tutor = TutorModel.objects.get(usuarioId=usuario)
			sessoes_como_tutor = SessaoModel.objects.filter(
				tutorId=tutor,
			).exclude(
				avaliacoes_tutor_sessao__tutorId=tutor
			)
		except TutorModel.DoesNotExist:
			sessoes_como_tutor = SessaoModel.objects.none()

		pendentes = []

		for s in sessoes_como_aprendiz:
			# Só alertar se a sessão já terminou (simplificando por data, mas poderia checar hora)
			if s.dataSessao < hoje or (s.dataSessao == hoje and s.horarioFim <= agora):
				s.tipoPendente = 'APRENDIZ' # Ele precisa avaliar como aprendiz
				pendentes.append(s)

		for s in sessoes_como_tutor:
			if s.dataSessao < hoje or (s.dataSessao == hoje and s.horarioFim <= agora):
				s.tipoPendente = 'TUTOR' # Ele precisa avaliar como tutor
				pendentes.append(s)

		serializer = SessaoPendenteAvaliacaoSerializer(pendentes, many=True)
		return Response(serializer.data, status=status.HTTP_200_OK)
