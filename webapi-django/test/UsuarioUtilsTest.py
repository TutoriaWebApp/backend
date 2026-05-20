import io
import os
import shutil
import tempfile
import glob
from django.test import TestCase, override_settings, RequestFactory
from django.core.files.uploadedfile import SimpleUploadedFile
from django.conf import settings
from project.utils import UsuarioUtils

# Configuração de diretório temporário para mídia durante os testes
MEDIA_ROOT = tempfile.mkdtemp()

@override_settings(MEDIA_ROOT=MEDIA_ROOT)
class UsuarioUtilsTest(TestCase):
    @classmethod
    def tearDownClass(cls):
        shutil.rmtree(MEDIA_ROOT, ignore_errors=True)
        super().tearDownClass()

    def setUp(self):
        self.factory = RequestFactory()
        self.email = "testutils@example.com"
        # Garante que a pasta de perfis existe
        os.makedirs(os.path.join(MEDIA_ROOT, 'perfis'), exist_ok=True)

    def test_set_fotoUrl_success(self):
        """Testa se a foto é salva corretamente no disco."""
        file_content = b"fake image content"
        file = SimpleUploadedFile("perfil.jpg", file_content)
        
        foto_nova = UsuarioUtils.set_fotoUrl(self.email, file)
        
        self.assertEqual(foto_nova, f"{self.email.lower()}.jpg")
        caminho_esperado = os.path.join(MEDIA_ROOT, 'perfis', foto_nova)
        self.assertTrue(os.path.exists(caminho_esperado))
        
        with open(caminho_esperado, 'rb') as f:
            self.assertEqual(f.read(), file_content)

    def test_set_fotoUrl_removes_old_photos(self):
        """Testa se fotos antigas com diferentes extensões são removidas ao salvar uma nova."""
        # Cria uma foto antiga .png
        perfis_dir = os.path.join(MEDIA_ROOT, 'perfis')
        old_photo = os.path.join(perfis_dir, f"{self.email.lower()}.png")
        with open(old_photo, 'wb') as f:
            f.write(b"old content")
        
        self.assertTrue(os.path.exists(old_photo))
        
        # Salva nova foto .jpg
        file = SimpleUploadedFile("new.jpg", b"new content")
        UsuarioUtils.set_fotoUrl(self.email, file)
        
        # A antiga .png deve ter sido removida
        self.assertFalse(os.path.exists(old_photo))
        # A nova .jpg deve existir
        self.assertTrue(os.path.exists(os.path.join(perfis_dir, f"{self.email.lower()}.jpg")))

    def test_get_fotoUrl_with_request(self):
        """Testa se a URL absoluta é gerada corretamente quando há um request."""
        # Cria o arquivo primeiro
        perfis_dir = os.path.join(MEDIA_ROOT, 'perfis')
        foto_path = os.path.join(perfis_dir, f"{self.email.lower()}.png")
        with open(foto_path, 'wb') as f:
            f.write(b"content")
            
        request = self.factory.get('/')
        url = UsuarioUtils.get_fotoUrl(self.email, request)
        
        self.assertIsNotNone(url)
        self.assertTrue(url.startswith('http://testserver'))
        self.assertIn(f'/media/perfis/{self.email.lower()}.png', url)

    def test_get_fotoUrl_without_request(self):
        """Testa se retorna None ao tentar obter URL sem objeto de request (mesmo que arquivo exista)."""
        perfis_dir = os.path.join(MEDIA_ROOT, 'perfis')
        with open(os.path.join(perfis_dir, f"{self.email.lower()}.png"), 'wb') as f:
            f.write(b"content")
            
        url = UsuarioUtils.get_fotoUrl(self.email, None)
        self.assertIsNone(url)

    def test_get_fotoUrl_file_not_exists(self):
        """Testa se retorna None quando o arquivo não existe."""
        request = self.factory.get('/')
        url = UsuarioUtils.get_fotoUrl("nonexistent@example.com", request)
        self.assertIsNone(url)

    def test_get_fotoUrl_empty_email(self):
        """Testa se retorna None para email vazio ou nulo."""
        self.assertIsNone(UsuarioUtils.get_fotoUrl("", None))
        self.assertIsNone(UsuarioUtils.get_fotoUrl(None, None))
