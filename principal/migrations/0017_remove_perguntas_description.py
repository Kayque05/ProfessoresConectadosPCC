# Generated by Django 4.0.1 on 2022-05-14 17:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('principal', '0016_rename_curso_perguntas_cursos'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='perguntas',
            name='description',
        ),
    ]
