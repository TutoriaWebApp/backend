from django.urls import path
from project.views import template_views

app_name = 'dashboard'

urlpatterns = [
    path('usuarios/', template_views.UsuarioListView.as_view(), name='usuario_list'),
	path('usuarios/add', template_views.UsuarioCreateView.as_view(), name='usuario_add'),
]
