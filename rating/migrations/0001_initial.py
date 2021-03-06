# Generated by Django 3.0.2 on 2020-02-08 17:50

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('register', '0004_auto_20200208_1042'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(default=datetime.datetime(2020, 2, 8, 17, 50, 31, 82176, tzinfo=utc), verbose_name='Сейчас')),
                ('poiID', models.CharField(max_length=32, verbose_name='Пароль')),
                ('type', models.CharField(max_length=100, verbose_name='Тип')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='register.User')),
            ],
        ),
    ]
