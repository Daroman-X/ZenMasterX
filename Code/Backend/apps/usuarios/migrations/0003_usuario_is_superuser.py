# Generated by Django 5.1.4 on 2024-12-26 16:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0002_usuario_is_active_usuario_is_staff'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='is_superuser',
            field=models.BooleanField(default=False, verbose_name='Superusuario'),
        ),
    ]
