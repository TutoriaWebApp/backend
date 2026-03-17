from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from project.views.api_views import *
from project.views.AuthViewSet import *

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
	path('login', LogInView.as_view(), name='logar_usuario'),
	path('login/refresh', loginRefreshView.as_view(), name='refrescar_token_de_acesso'),
	path('logout', LogOutView.as_view(), name='deslogar_usuario'),
	path('reset-password/request', PasswordResetView.as_view(), name='resetar_senha'),
	path('reset-password/confirm', PasswordResetConfirmView.as_view(), name='confirmar_alteracao_de_senha'),
]
