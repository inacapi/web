# Generated by Django 4.1.5 on 2023-02-03 20:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("usuarios", "0002_rename_usuario_usuario_nombre"),
    ]

    operations = [
        migrations.DeleteModel(
            name="Usuario",
        ),
    ]
