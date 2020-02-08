from django.db import models
from register.models import User
from django.utils.timezone import now
class Group(models.Model):
    title = models.CharField(max_length=128, verbose_name='Название')
    groupID = models.AutoField(auto_created=True, primary_key=True, serialize=True, verbose_name='ID')
    descr = models.CharField(max_length=128, verbose_name='Описание')
    timestamp = models.DateTimeField(default=now(), verbose_name="Сейчас")
    Users = models.ManyToManyField(
        User,
    )

