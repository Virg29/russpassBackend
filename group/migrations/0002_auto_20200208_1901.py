# Generated by Django 3.0.3 on 2020-02-08 19:01

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('group', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='group',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2020, 2, 8, 19, 1, 29, 117628, tzinfo=utc), verbose_name='Сейчас'),
        ),
    ]
