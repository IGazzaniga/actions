# Generated by Django 2.1.1 on 2019-01-09 18:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rutinas', '0002_auto_20190109_1453'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='diaejercicio',
            name='dia',
        ),
        migrations.RemoveField(
            model_name='diaejercicio',
            name='ejercicio',
        ),
        migrations.DeleteModel(
            name='DiaEjercicio',
        ),
    ]