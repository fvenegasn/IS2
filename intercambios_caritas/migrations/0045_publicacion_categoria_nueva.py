# Generated by Django 5.0.4 on 2024-06-17 22:47

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('intercambios_caritas', '0044_categoria_alter_usuario_email_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='publicacion',
            name='categoria_nueva',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='intercambios_caritas.categoria'),
        ),
    ]
