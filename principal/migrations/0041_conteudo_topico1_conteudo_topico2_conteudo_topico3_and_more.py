# Generated by Django 4.0.1 on 2022-06-07 23:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('principal', '0040_conteudo_titulo_topico1_conteudo_titulo_topico2_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='conteudo',
            name='topico1',
            field=models.TextField(default=6),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='conteudo',
            name='topico2',
            field=models.TextField(default=6),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='conteudo',
            name='topico3',
            field=models.TextField(default=6),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='conteudo',
            name='topico4',
            field=models.TextField(default=6),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='conteudo',
            name='topico5',
            field=models.TextField(default=6),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='conteudo',
            name='topico6',
            field=models.TextField(default=6),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='conteudo',
            name='topico7',
            field=models.TextField(default=6),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='conteudo',
            name='topico8',
            field=models.TextField(default=6),
            preserve_default=False,
        ),
    ]