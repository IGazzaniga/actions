# Generated by Django 2.1.1 on 2018-09-26 01:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rutinas', '0004_rutina_ejercicios'),
    ]

    operations = [
        migrations.AddField(
            model_name='rutina',
            name='numero',
            field=models.IntegerField(default=0),
        ),
    ]
