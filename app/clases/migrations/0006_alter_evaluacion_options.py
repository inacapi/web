# Generated by Django 4.1.5 on 2023-02-03 20:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("clases", "0005_alter_seccion_unique_together"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="evaluacion",
            options={"ordering": ["clase__nombre", "numero"]},
        ),
    ]
