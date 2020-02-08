# Generated by Django 3.0.2 on 2020-02-08 09:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=16, unique=True, verbose_name='Имя пользователя')),
                ('password', models.CharField(max_length=16, verbose_name='Пароль')),
                ('balance', models.IntegerField(verbose_name='Баланс пасскоинов')),
                ('level', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='Уровень')),
                ('image', models.CharField(max_length=16, verbose_name='Название статической аватарки')),
            ],
        ),
    ]