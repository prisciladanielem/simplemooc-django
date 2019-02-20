# Generated by Django 2.0.10 on 2019-02-19 14:54

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_user_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='PasswordReset',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key', models.CharField(max_length=100, unique=True, verbose_name='Chave')),
                ('created_at', models.TimeField(auto_now_add=True, verbose_name='Criado em')),
                ('confirmed', models.BooleanField(default=False, verbose_name='Confirmado?')),
            ],
            options={
                'verbose_name': 'Nova senha',
                'verbose_name_plural': 'Novas senhas',
                'ordering': ['-created_at'],
            },
        ),
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(max_length=30, unique=True, validators=[django.core.validators.RegexValidator('^[\\w.@+-]+$', code='invalid', message='O nome de usuário pode ser somente letras, números e os caracteres @/ ./ -/ _/')], verbose_name='Usuário'),
        ),
        migrations.AddField(
            model_name='passwordreset',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Usuário'),
        ),
    ]