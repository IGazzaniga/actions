# Generated by Django 2.1.1 on 2018-09-24 22:19

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('rutinas', '0002_auto_20180924_1906'),
    ]

    operations = [
        migrations.AddField(
            model_name='fichamedica',
            name='fecha_nacimiento',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='pago',
            name='fecha',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='fichamedica',
            name='altura',
            field=models.IntegerField(),
        ),
    ]
