# Generated by Django 5.0.4 on 2024-07-01 20:34

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('intercambios_caritas', '0056_remove_publicacion_filial_publicacion_filial'),
    ]

    operations = [
        migrations.AddField(
            model_name='intercambio',
            name='categoria_nueva',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='intercambios_caritas.categoria'),
        ),
        migrations.AddField(
            model_name='intercambio',
            name='filial',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='intercambios_caritas.filial'),
        ),
    ]