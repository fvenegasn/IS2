# Generated by Django 5.0.6 on 2024-06-16 05:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('intercambios_caritas', '0037_alter_usuario_direccion_alter_usuario_email_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='direccion',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='telefono',
            field=models.CharField(blank=True, max_length=20),
        ),
    ]
