# Generated by Django 2.1.1 on 2018-12-18 02:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rutinas', '0009_auto_20181217_2322'),
    ]

    operations = [
        migrations.AddField(
            model_name='rutina',
            name='nombre',
            field=models.CharField(default='', max_length=30),
        ),
    ]
