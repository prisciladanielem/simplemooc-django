# Generated by Django 2.0.10 on 2019-04-08 19:10

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_auto_20190220_1414'),
    ]

    operations = [
        migrations.AlterField(
            model_name='passwordreset',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime.now, verbose_name='Criado em'),
        ),
        migrations.AlterField(
            model_name='user',
            name='data_joined',
            field=models.DateTimeField(default=datetime.datetime.now, verbose_name='Data de entrada'),
        ),
    ]