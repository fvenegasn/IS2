# Generated by Django 5.0.4 on 2024-05-12 17:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('intercambios_caritas', '0005_publicacion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='publicacion',
            name='categoria',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='publicacion',
            name='nombre',
            field=models.CharField(max_length=50),
        ),
    ]
