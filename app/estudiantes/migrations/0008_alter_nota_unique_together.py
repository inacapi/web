# Generated by Django 4.1.7 on 2023-03-02 00:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clases', '0012_alter_evaluacion_nota_promedio'),
        ('estudiantes', '0007_alter_matricula_options'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='nota',
            unique_together={('inscripcion', 'evaluacion')},
        ),
    ]