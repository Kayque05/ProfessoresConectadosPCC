# Generated by Django 4.0.1 on 2022-06-24 19:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('principal', '0042_alter_conteudo_introducao'),
    ]

    operations = [
        migrations.AddField(
            model_name='conteudo',
            name='link',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
    ]
