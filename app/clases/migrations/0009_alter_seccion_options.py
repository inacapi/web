# Generated by Django 4.1.7 on 2023-02-26 21:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clases', '0008_alter_seccion_unique_together'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='seccion',
            options={'ordering': ['clase__nombre', 'id', 'docente__nombre', 'docente__apellido']},
        ),
    ]
