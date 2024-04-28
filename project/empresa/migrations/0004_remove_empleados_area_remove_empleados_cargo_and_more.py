# Generated by Django 5.0.4 on 2024-04-27 23:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('empresa', '0003_alter_areas_options_alter_empleados_options_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='empleados',
            name='area',
        ),
        migrations.RemoveField(
            model_name='empleados',
            name='cargo',
        ),
        migrations.AddField(
            model_name='areas',
            name='empleados',
            field=models.ManyToManyField(to='empresa.empleados'),
        ),
        migrations.AlterField(
            model_name='areas',
            name='nombre',
            field=models.CharField(max_length=100, verbose_name='área'),
        ),
    ]