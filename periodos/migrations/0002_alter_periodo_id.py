# Generated by Django 4.1.4 on 2023-01-07 21:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('periodos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='periodo',
            name='id',
            field=models.PositiveIntegerField(primary_key=True, serialize=False),
        ),
    ]
