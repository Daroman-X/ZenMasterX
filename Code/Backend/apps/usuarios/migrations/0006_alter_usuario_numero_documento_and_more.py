# Generated by Django 5.1.4 on 2024-12-26 16:23

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0005_alter_usuario_fecha_nacimiento_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='numero_documento',
            field=models.CharField(blank=True, max_length=200, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='tipo_documento',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='usuarios.tipodocumento', verbose_name='Tipo de Documento'),
        ),
    ]
