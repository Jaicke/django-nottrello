# Generated by Django 2.1.2 on 2018-10-24 06:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_remove_projeto_descricao'),
    ]

    operations = [
        migrations.AddField(
            model_name='projeto',
            name='descricao',
            field=models.CharField(default='', max_length=200, verbose_name='Descrição'),
        ),
    ]
