# Generated by Django 4.1.7 on 2023-03-01 21:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('clases', '0009_alter_seccion_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='evaluacion',
            options={'ordering': ['seccion__clase__nombre', 'numero']},
        ),
        migrations.AlterUniqueTogether(
            name='evaluacion',
            unique_together=set(),
        ),
        migrations.AddField(
            model_name='evaluacion',
            name='fecha',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='evaluacion',
            name='nota_promedio',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='evaluacion',
            name='seccion',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.RESTRICT, related_name='evaluaciones', to='clases.seccion'),
        ),
        migrations.AlterUniqueTogether(
            name='evaluacion',
            unique_together={('seccion', 'numero')},
        ),
        migrations.RemoveField(
            model_name='evaluacion',
            name='clase',
        ),
    ]
