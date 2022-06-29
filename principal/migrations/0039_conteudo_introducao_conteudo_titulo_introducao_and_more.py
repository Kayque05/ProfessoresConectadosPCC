# Generated by Django 4.0.1 on 2022-06-07 23:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('principal', '0038_material_decimo_passo_material_doze_passo_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='conteudo',
            name='introducao',
            field=models.CharField(default=5, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='conteudo',
            name='titulo_introducao',
            field=models.CharField(default=5, max_length=255),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='material',
        ),
    ]
