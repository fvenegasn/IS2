# Generated by Django 5.0.4 on 2024-06-30 23:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('intercambios_caritas', '0055_remove_publicacion_filial_publicacion_filial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='publicacion',
            name='filial',
        ),
        migrations.AddField(
            model_name='publicacion',
            name='filial',
            field=models.ManyToManyField(blank=True, related_name='publicaciones', to='intercambios_caritas.filial'),
        ),
    ]
