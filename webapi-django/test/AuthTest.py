from datetime import date
from django.test import TestCase
from django.contrib.auth import get_user_model
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from unittest.mock import patch

Usuario = get_user_model()

class LogInViewTest(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = Usuario.objects.create_user(
            email='test@example.com',
            nomePerfil='Test User',
            cidade='Test City',
            estado='TS',
            aniversario=date(1990, 1, 1),
            password='testpass123'
        )

    def test_login_success(self):
        """Testa login com credenciais válidas"""
        url = '/api/login/'
        data = {'username': 'test@example.com', 'password': 'testpass123'}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('mensagem', response.data)
        self.assertIn('access_token', response.cookies)
        self.assertIn('refresh_token', response.cookies)

    def test_login_invalid_credentials(self):
        """Testa login com credenciais inválidas"""
        url = '/api/login/'
        data = {'username': 'test@example.com', 'password': 'wrongpass'}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)


class LoginRefreshViewTest(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = Usuario.objects.create_user(
            email='test@example.com',
            nomePerfil='Test User',
            cidade='Test City',
            estado='TS',
            aniversario=date(1990, 1, 1),
            password='testpass123'
        )

    def test_refresh_valid_token(self):
        """Testa refresh com token válido"""
        # Primeiro, fazer login para obter o refresh token
        login_url = '/api/login/'
        data = {'username': 'test@example.com', 'password': 'testpass123'}
        login_response = self.client.post(login_url, data)
        self.assertEqual(login_response.status_code, status.HTTP_200_OK)

        # Agora, refresh
        url = '/api/login/refresh/'
        response = self.client.post(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('mensagem', response.data)
        self.assertIn('access_token', response.cookies)

    def test_refresh_no_token(self):
        """Testa refresh sem token"""
        url = '/api/login/refresh/'
        response = self.client.post(url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertIn('mensagem', response.data)

    def test_refresh_invalid_token(self):
        """Testa refresh com token inválido"""
        url = '/api/login/refresh/'
        self.client.cookies['refresh_token'] = 'invalid_token'
        response = self.client.post(url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertIn('mensagem', response.data)


class LogOutViewTest(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = Usuario.objects.create_user(
            email='test@example.com',
            nomePerfil='Test User',
            cidade='Test City',
            estado='TS',
            aniversario=date(1990, 1, 1),
            password='testpass123'
        )

    def test_logout(self):
        """Testa logout"""
        # Primeiro, fazer login
        login_url = '/api/login/'
        data = {'username': 'test@example.com', 'password': 'testpass123'}
        login_response = self.client.post(login_url, data)
        self.assertEqual(login_response.status_code, status.HTTP_200_OK)

        # Verificar se cookies estão setados
        self.assertIn('access_token', self.client.cookies)
        self.assertIn('refresh_token', self.client.cookies)

        # Agora, logout
        url = '/api/logout/'
        response = self.client.post(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('mensagem', response.data)

        # Verificar se cookies foram deletados
        self.assertNotIn('access_token', response.cookies)
        self.assertNotIn('refresh_token', response.cookies)


class PasswordResetViewTest(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = Usuario.objects.create_user(
            email='test@example.com',
            nomePerfil='Test User',
            cidade='Test City',
            estado='TS',
            aniversario=date(1990, 1, 1),
            password='testpass123'
        )

    @patch('project.views.AuthViewSet.send_mail')
    def test_password_reset_existing_email(self, mock_send_mail):
        """Testa reset de senha com email existente"""
        url = '/api/reset-password/request/'
        data = {'email': 'test@example.com'}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('mensagem', response.data)
        mock_send_mail.assert_called_once()

    @patch('project.views.AuthViewSet.send_mail')
    def test_password_reset_non_existing_email(self, mock_send_mail):
        """Testa reset de senha com email não existente"""
        url = '/api/reset-password/request/'
        data = {'email': 'nonexistent@example.com'}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('mensagem', response.data)
        # Mesmo assim, send_mail é chamado? No código, if user: send_mail
        mock_send_mail.assert_not_called()


class PasswordResetConfirmViewTest(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = Usuario.objects.create_user(
            email='test@example.com',
            nomePerfil='Test User',
            cidade='Test City',
            estado='TS',
            aniversario=date(1990, 1, 1),
            password='testpass123'
        )

    def test_password_reset_confirm_valid(self):
        """Testa confirmação de reset com uid e token válidos"""
        token = default_token_generator.make_token(self.user)
        uid = urlsafe_base64_encode(force_bytes(self.user.pk))
        url = '/api/reset-password/confirm/'
        data = {'uid': uid, 'token': token, 'new_password': 'newpass123'}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('mensagem', response.data)
        self.user.refresh_from_db()
        self.assertTrue(self.user.check_password('newpass123'))

    def test_password_reset_confirm_invalid_uid(self):
        """Testa confirmação de reset com uid inválido"""
        token = default_token_generator.make_token(self.user)
        uid = urlsafe_base64_encode(force_bytes(999))  # ID inválido
        url = '/api/reset-password/confirm/'
        data = {'uid': uid, 'token': token, 'new_password': 'newpass123'}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('mensagem', response.data)

    def test_password_reset_confirm_invalid_token(self):
        """Testa confirmação de reset com token inválido"""
        uid = urlsafe_base64_encode(force_bytes(self.user.pk))
        url = '/api/reset-password/confirm/'
        data = {'uid': uid, 'token': 'invalid-token', 'new_password': 'newpass123'}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('mensagem', response.data)
