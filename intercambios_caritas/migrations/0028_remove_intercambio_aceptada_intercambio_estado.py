# Generated by Django 5.0.4 on 2024-06-07 16:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('intercambios_caritas', '0027_alter_usuario_rol'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='intercambio',
            name='aceptada',
        ),
        migrations.AddField(
            model_name='intercambio',
            name='estado',
            field=models.CharField(choices=[('PENDIENTE', 'Pendiente'), ('ACEPTADA', 'Aceptada'), ('RECHAZADA', 'Rechazada'), ('CANCELADA', 'Cancelada')], default='PENDIENTE', max_length=10),
        ),
    ]
