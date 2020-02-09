# Generated by Django 3.0.3 on 2020-02-08 18:29

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('register', '0004_auto_20200208_1042'),
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('groupID', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128, verbose_name='Название')),
                ('descr', models.CharField(max_length=128, verbose_name='Описание')),
                ('timestamp', models.DateTimeField(default=datetime.datetime(2020, 2, 8, 18, 29, 41, 497110, tzinfo=utc), verbose_name='Сейчас')),
                ('Users', models.ManyToManyField(to='register.User')),
            ],
        ),
    ]
