# Generated by Django 5.0.6 on 2024-07-03 04:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('intercambios_caritas', '0061_intercambio_calificacion_demandante_a_ofertante_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='filial',
            name='direccion',
            field=models.CharField(default='Direccion no especificada', max_length=100, verbose_name='Dirección'),
        ),
        migrations.AlterField(
            model_name='filial',
            name='nombre',
            field=models.CharField(max_length=100, unique=True, verbose_name='Nombre'),
        ),
    ]
