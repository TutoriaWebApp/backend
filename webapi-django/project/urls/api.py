from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from project.views import *

router = DefaultRouter()

router.register(r'usuarios', UsuarioViewSet, basename='usuario')

router.register(r'conquistas', ConquistaViewSet, basename='conquista')

router.register(r'consegue', consegueViewSet, basename='consegue')

router.register(r'tutores', TutorViewSet, basename='tutor')

router.register(r'sessoes', SessaoViewSet, basename='sessoes')

router.register(r'solicitacoes', SolicitacaoViewSet, basename='solicitacoes')

router.register(r'areas', AreaViewSet, basename='areas')

router.register(r'especialidades', EspecialidadeViewSet, basename='especialidades')

router.register(r'contem', ContemViewSet, basename='contem')

router.register(r'agendas', AgendaViewSet, basename='agendas')

router.register(r'solicitacoes/aceitar', AceitarSolicitacaoViewSet, basename='aceitar-solicitacao')
router.register(r'solicitacoes/recusar', RecusarSolicitacaoViewSet, basename='recusar-solicitacao')

urlpatterns = [
    path('', include(router.urls)),

	path('usuarios/novo', UsuarioRegistroView.as_view(), name='criar_novo_usuario'),
	path('usuarios/altera-senha', UsuarioAlteraSenhaView.as_view(), name='altera_a_senha'),

	path('login', LogInView.as_view(), name='logar_usuario'),
	path('login/refresh', LoginRefreshView.as_view(), name='refrescar_token_de_acesso'),
	path('logout', LogOutView.as_view(), name='deslogar_usuario'),
	path('reset-password/request', PasswordResetView.as_view(), name='resetar_senha'),
	path('reset-password/confirm', PasswordResetConfirmView.as_view(), name='confirmar_alteracao_de_senha'),
	path('perfil', UsuarioPerfilLogadoView.as_view(), name='perfil_do_usuario'),

	path('conquistas/usuario/<int:usuarioId>', Usuario_conseguiu_ConquistaView.as_view(), name='conquistas_do_usuario'),
]
