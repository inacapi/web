# Generated by Django 4.1.5 on 2023-01-19 00:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("clases", "0004_alter_evaluacion_numero_and_more"),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name="seccion",
            unique_together={("clase", "periodo", "docente")},
        ),
    ]