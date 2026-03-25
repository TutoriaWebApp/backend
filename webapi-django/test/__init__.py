# from TestConquistaSerializer import *
from test.UsuarioTest import UsuarioModelTest, UsuarioViewSetTest, UsuarioRegistroSerializerTest
from test.AuthTest import LogInViewTest, LogOutViewTest, LoginRefreshViewTest, PasswordResetViewTest, PasswordResetConfirmViewTest
from test.ConquistaTest import ConquistaSerializerTest, ConquistaUsuarioSerializerTest, consegueSerializerTest

__all__ = [
	'UsuarioModelTest'
	'UsuarioRegistroSerializerTest',
	'UsuarioViewSetTest',
	'LogInViewTest',
	'LoginRefreshViewTest',
	'LogOutViewTest',
	'PasswordResetViewTest',
	'PasswordResetConfirmViewTest',
	'ConquistaSerializerTest',
	'ConquistaUsuarioSerializerTest',
	'consegueSerializerTest',
]
