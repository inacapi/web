# Generated by Django 4.1.4 on 2023-01-05 21:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('clases', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Evaluacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('porcentaje', models.FloatField()),
                ('numero', models.PositiveIntegerField()),
                ('clase', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='clases.clase')),
            ],
        ),
    ]
