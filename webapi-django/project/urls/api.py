from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from project.views.api_views import *

router = DefaultRouter()

router.register(r'usuarios', UsuarioViewSet, basename='usuario')

router.register(r'conquistas', ConquistaViewSet, basename='conquista')

router.register(r'consegue', consegueViewSet, basename='consegue')

router.register(r'tutores', TutorViewSet, basename='tutor')

router.register(r'sessoes', SessaoViewSet, basename='sessoes')

router.register(r'solicitacao', SolicitacaoViewSet, basename='solicitacoes')

urlpatterns = [
    path('', include(router.urls)),
	path('conquistas/usuario/<int:usuarioId>', Usuario_conseguiu_Conquista.as_view(), name='conquistas_do_usuario'),
	path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
	path('token/refresh', TokenRefreshView.as_view(), name='token_refresh')
]
