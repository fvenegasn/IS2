# Generated by Django 5.0.4 on 2024-06-17 22:48

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('intercambios_caritas', '0045_publicacion_categoria_nueva'),
    ]

    operations = [
        migrations.AlterField(
            model_name='publicacion',
            name='categoria_nueva',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='intercambios_caritas.categoria'),
        ),
    ]
