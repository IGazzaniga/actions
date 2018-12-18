# Generated by Django 2.1.1 on 2018-12-13 16:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rutinas', '0003_auto_20181211_1455'),
    ]

    operations = [
        migrations.AddField(
            model_name='profesor',
            name='calificacion_promedio',
            field=models.DecimalField(decimal_places=1, default=0, max_digits=6),
            preserve_default=False,
        ),
        migrations.AlterUniqueTogether(
            name='profesor',
            unique_together=set(),
        ),
        migrations.RemoveField(
            model_name='profesor',
            name='average',
        ),
        migrations.RemoveField(
            model_name='profesor',
            name='content_type',
        ),
        migrations.RemoveField(
            model_name='profesor',
            name='count',
        ),
        migrations.RemoveField(
            model_name='profesor',
            name='object_id',
        ),
        migrations.RemoveField(
            model_name='profesor',
            name='total',
        ),
    ]
