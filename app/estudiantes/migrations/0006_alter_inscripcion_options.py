# Generated by Django 4.1.7 on 2023-02-25 03:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('estudiantes', '0005_alter_inscripcion_unique_together_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='inscripcion',
            options={'ordering': ['matricula__estudiante__nombre', '-matricula__estudiante__apellido', 'seccion__clase__nombre']},
        ),
    ]
