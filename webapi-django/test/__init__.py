# Model Tests
from test.models.UsuarioModelTest import UsuarioModelTest
from test.models.ConquistaModelTest import ConquistaModelTest
from test.models.TutorModelTest import TutorModelTest
from test.models.AreaEspecialidadeModelTest import AreaEspecialidadeModelTest
from test.models.SessaoSolicitacaoModelTest import SessaoSolicitacaoModelTest

# Serializer Tests
from test.serializers.UsuarioSerializerTest import UsuarioSerializerTest
from test.serializers.ConquistaSerializerTest import ConquistaSerializerTest
from test.serializers.TutorAreaSerializerTest import TutorAreaSerializerTest
from test.serializers.SessaoSolicitacaoSerializerTest import SessaoSolicitacaoSerializerTest

__all__ = [
    # Model Tests
	'UsuarioModelTest',
    'ConquistaModelTest',
    'TutorModelTest',
    'AreaEspecialidadeModelTest',
    'SessaoSolicitacaoModelTest',
    # Serializer Tests
    'UsuarioSerializerTest',
    'ConquistaSerializerTest',
    'TutorAreaSerializerTest',
    'SessaoSolicitacaoSerializerTest',
]
