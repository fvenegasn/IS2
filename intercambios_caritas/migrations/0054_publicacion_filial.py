# Generated by Django 5.0.4 on 2024-06-30 22:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('intercambios_caritas', '0053_alter_publicacion_categoria_nueva'),
    ]

    operations = [
        migrations.AddField(
            model_name='publicacion',
            name='filial',
            field=models.ManyToManyField(blank=True, related_name='publicaciones', to='intercambios_caritas.filial'),
        ),
    ]