# Generated by Django 2.1.1 on 2019-01-28 18:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rutinas', '0008_profesor_foto'),
    ]

    operations = [
        migrations.AddField(
            model_name='servicio',
            name='imagen',
            field=models.ImageField(default='', upload_to=''),
        ),
    ]
