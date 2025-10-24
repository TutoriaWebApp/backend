from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from project.forms import UsuarioCreateForm, UsuarioUpdateForm
from project.models import *

class UsuarioAdmin(UserAdmin):
	model = Usuario

	"""
	Listagem de Usuários na página de Admin
	"""
	list_display = ('email', 'nomePerfil', 'cidade', 'estado', 'is_staff', 'date_joined')
	readonly_fields = ('last_login', 'date_joined')
	search_fields = ('email', 'nomePerfil')
	ordering = ('-date_joined',)
	filter_horizontal = ()
	list_filter = ()

	"""
	Formulário de CADASTRO
	"""
	add_form = UsuarioCreateForm

	add_fieldsets = (
        (None, {
			'classes': ('wide',),
			'fields': (
				'email',
				'nomePerfil',
				'cidade',
				'estado',
				'urlFoto',
				'password1',
				'password2'
			),
		}),
	)

	"""
	Formunlário e EDIÇÃO
	"""
	form     = UsuarioUpdateForm
	fieldsets = (
        (None, {
            'fields': ('email', 'password')
		}),
        ('Informações Pessoais', {
            'fields': (
                'nomePerfil',
                'pontuacao',
                'cidade',
                'estado',
                'urlFoto'
			)
		}),
        ('Permissões', {
            'fields': (
                'is_active',
                'is_staff',
                'is_superuser',
                'groups',
                'user_permissions'
			)
		}),
        ('Datas Importantes', {
            'fields': ('last_login', 'date_joined')
		}),
    )


# Registrando os modelos
admin.site.register(Usuario, UsuarioAdmin)
admin.site.register(Conquista)
admin.site.register(consegue)
admin.site.register(Tutor)
admin.site.register(Sessao)
admin.site.register(Solicitacao)
