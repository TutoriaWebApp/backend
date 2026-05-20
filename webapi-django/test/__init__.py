# Model Tests
from test.models.UsuarioModelTest import UsuarioModelTest
from test.models.ConquistaModelTest import ConquistaModelTest
from test.models.TutorModelTest import TutorModelTest
from test.models.AreaEspecialidadeModelTest import AreaEspecialidadeModelTest
from test.models.SessaoSolicitacaoModelTest import SessaoSolicitacaoModelTest
from test.models.AvaliacaoModelTest import AvaliacaoModelTest

# Serializer Tests
from test.serializers.UsuarioSerializerTest import UsuarioSerializerTest
from test.serializers.ConquistaSerializerTest import ConquistaSerializerTest
from test.serializers.TutorAreaSerializerTest import TutorAreaSerializerTest
from test.serializers.SessaoSolicitacaoSerializerTest import SessaoSolicitacaoSerializerTest
from test.serializers.AvaliacaoSerializerTest import AvaliacaoSerializerTest

# ViewSet Tests
from test.views.UsuarioViewSetTest import UsuarioViewSetTest
from test.views.ConquistaViewSetTest import ConquistaViewSetTest
from test.views.SessaoViewSetTest import SessaoViewSetTest
from test.views.TutorViewSetTest import TutorViewSetTest
from test.views.AvaliacaoViewSetTest import AvaliacaoViewSetTest

# Auth and Utils
from test.AuthTest import *
from test.UsuarioUtilsTest import UsuarioUtilsTest

__all__ = [
    # Model Tests
	'UsuarioModelTest',
    'ConquistaModelTest',
    'TutorModelTest',
    'AreaEspecialidadeModelTest',
    'SessaoSolicitacaoModelTest',
	'AvaliacaoModelTest',

    # Serializer Tests
    'UsuarioSerializerTest',
    'ConquistaSerializerTest',
    'TutorAreaSerializerTest',
    'SessaoSolicitacaoSerializerTest',
	'AvaliacaoSerializerTest',

    # ViewSet Tests
    'UsuarioViewSetTest',
    'ConquistaViewSetTest',
    'SessaoViewSetTest',
    'TutorViewSetTest',
	'AvaliacaoViewSetTest',

    # Auth and Utils
    'LogInViewTest',
    'LoginRefreshViewTest',
    'LogOutViewTest',
    'PasswordResetViewTest',
    'PasswordResetConfirmViewTest',
    'UsuarioUtilsTest',
]
