# Generated by Django 4.1.7 on 2023-03-06 22:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clases', '0012_alter_evaluacion_nota_promedio'),
    ]

    operations = [
        migrations.AddField(
            model_name='clase',
            name='codigo',
            field=models.CharField(blank=True, max_length=6, null=True, unique=True),
        ),
    ]