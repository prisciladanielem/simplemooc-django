# Generated by Django 2.0.10 on 2019-04-08 19:10

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0009_auto_20190322_1719'),
    ]

    operations = [
        migrations.AlterField(
            model_name='announcement',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime.now, verbose_name='Criado em'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime.now, verbose_name='Criado em'),
        ),
        migrations.AlterField(
            model_name='course',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime.now, verbose_name='Criado em'),
        ),
        migrations.AlterField(
            model_name='enrollment',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime.now, verbose_name='Criado em'),
        ),
        migrations.AlterField(
            model_name='lesson',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime.now, verbose_name='Criado em'),
        ),
        migrations.AlterField(
            model_name='material',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime.now, verbose_name='Criado em'),
        ),
    ]