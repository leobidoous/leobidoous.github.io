from django.db import models
from django.contrib.auth.models import AbstractBaseUser, UserManager, PermissionsMixin
from django.core import validators
import re


# Create your models here.
class UserModel(AbstractBaseUser, PermissionsMixin):
    genres = (('M', 'Masculino'),
              ('F', 'Feminino'),
              ('O', 'Outro'))

    username = models.CharField(
        'Username', max_length=30, unique=True, validators=[
            validators.RegexValidator(
                re.compile('^[\w.@+-]+$'),
                'Informe um nome de usuário válido. '
                'Este valor deve conter apenas letras, números '
                'e os caracteres: @/./+/-/_ .'
                , 'invalid'
            )
        ], help_text='Um nome curto que será usado para identificá-lo de forma única na plataforma'
    )
    name = models.CharField('Nome', max_length=255, blank=False)
    cpf = models.CharField('CPF', max_length=14, unique=True)
    genre = models.CharField('Gênero', max_length=10, choices=genres, blank=True)
    email = models.EmailField('E-mail', unique=True)
    password = models.CharField("Senha", max_length=255)
    telephone = models.CharField("Telefone", max_length=14)
    birth = models.DateTimeField('Nascimento')
    is_staff = models.BooleanField('Team', default=False)
    is_active = models.BooleanField('Active', default=True)
    date_joined = models.DateTimeField('Criado em:', auto_now_add=True)
    last_update = models.DateTimeField('Atualizado em:', auto_now=True)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['name', 'cpf', 'genre', 'email', 'telephone', 'birth']

    objects = UserManager()

    class Meta:
        verbose_name = 'Usuário'
        verbose_name_plural = 'Usuários'

    def __str__(self):
        return self.name or self.email

    def get_full_name(self):
        return str(self)

    def get_short_name(self):
        return str(self).split(" ")[0]
