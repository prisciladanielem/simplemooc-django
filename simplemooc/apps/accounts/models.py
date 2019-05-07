from datetime import datetime
from django.core.validators import RegexValidator
from django.db import models
from django.core import validators
from django.conf import settings
from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin, UserManager

class User(AbstractBaseUser,PermissionsMixin):
    username = models.CharField('Usuário',
                                max_length=30,
                                unique=True,
                                validators=[RegexValidator(r'^[\w.@+-]+$', #Valida se existe catacter inválido no nome de usuário
                                message='O nome de usuário pode ser somente letras, números e os caracteres @/ ./ -/ _/',
                                code='invalid'
                                )])
    email = models.EmailField('E-mail', unique=True)
    name = models.CharField('Nome', max_length=100, blank=True)
    image = models.ImageField(upload_to='accounts/images', 
                              verbose_name='Imagem',
                              null=True,
                              blank=True
                              )
    is_active = models.BooleanField('Está ativo?', blank=True, default=True)
    is_staff = models.BooleanField('É da equipe?', blank=True, default=False)
    data_joined = models.DateTimeField('Data de entrada',default=datetime.now)
 
    objects = UserManager()
 
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']
 
    def __str__(self):
        return self.name or self.username
 
    def get_short_name(self):
        return self.username
 
    def get_full_name(self):
        return str(self)
 
    class Meta:
        verbose_name = 'Usuário'
        verbose_name_plural = 'Usuários'

class PasswordReset(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, 
                             verbose_name='Usuário',
                             related_name='resets',
                             on_delete=models.CASCADE
                            )
    key = models.CharField('Chave', max_length=100, unique=True)
    created_at = models.DateTimeField('Criado em', default=datetime.now)
    confirmed = models.BooleanField('Confirmado?', default=False, blank=True)

    def __str__(self):
        return '{0} - {1}'.format(self.user, self.created_at)

    class Meta:
        verbose_name = 'Nova senha'
        verbose_name_plural = 'Novas senhas'
        ordering = ['-created_at']