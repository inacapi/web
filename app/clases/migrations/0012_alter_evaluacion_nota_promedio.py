# Generated by Django 4.1.7 on 2023-03-01 22:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clases', '0011_alter_evaluacion_seccion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='evaluacion',
            name='nota_promedio',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]
