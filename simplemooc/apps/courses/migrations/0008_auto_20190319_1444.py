# Generated by Django 2.0.10 on 2019-03-19 14:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0007_auto_20190319_1428'),
    ]

    operations = [
        migrations.AlterField(
            model_name='material',
            name='lesson',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='materiais', to='courses.Lesson', verbose_name='Aulas'),
        ),
    ]
