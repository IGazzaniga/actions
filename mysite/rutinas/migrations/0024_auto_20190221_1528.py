# Generated by Django 2.1.1 on 2019-02-21 18:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rutinas', '0023_auto_20190221_1524'),
    ]

    operations = [
        migrations.AlterField(
            model_name='semana',
            name='rutina_cliente',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='rutinas.RutinaCliente'),
        ),
    ]
