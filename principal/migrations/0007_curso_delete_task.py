# Generated by Django 4.0.1 on 2022-05-05 03:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('principal', '0006_comentarios'),
    ]

    operations = [
        migrations.CreateModel(
            name='Curso',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_curso', models.CharField(max_length=255)),
            ],
        ),
        migrations.DeleteModel(
            name='Task',
        ),
    ]
