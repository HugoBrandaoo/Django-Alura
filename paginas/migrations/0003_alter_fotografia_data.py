# Generated by Django 5.0.7 on 2024-07-17 00:00

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('paginas', '0002_fotografia_publicada'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fotografia',
            name='data',
            field=models.DateField(blank=True, default=datetime.datetime.now),
        ),
    ]