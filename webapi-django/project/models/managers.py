from django.contrib.auth.models import BaseUserManager

class UsuarioManager(BaseUserManager):
    """
    Manager customizado para o nosso modelo Usuario,
    onde o email é o identificador único para autenticação.
    """
    def create_user(self, email, nomePerfil, cidade, estado, aniversario, password=None, **extra_fields):
        """
        Cria e salva um Usuário com o email e senha fornecidos.
        """
        if not email:
            raise ValueError('O campo Email é obrigatório')

        email = self.normalize_email(email)
        user = self.model(
            email=email,
            nomePerfil=nomePerfil,
            cidade=cidade,
            estado=estado,
            aniversario=aniversario,
            **extra_fields
        )

        user.set_password(password) # Armazena o hash da senha
        user.save(using=self._db)
        return user

    def create_superuser(self, email, nomePerfil, cidade, estado, aniversario, password=None, **extra_fields):
        """
        Cria e salva um Superusuário.
        """
        # Adiciona os campos de staff/superuser que não estão no seu SQL,
        # mas são necessários para o Django Admin.
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        # Para o superuser, alguns campos podem ser fakes
        return self.create_user(
            email,
            nomePerfil,
            cidade,
            estado,
            aniversario,
            urlFoto='N/A',
            password=password,
            **extra_fields
        )
