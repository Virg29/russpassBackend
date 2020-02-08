from django.db import models
from register.models import User
from django.utils.timezone import now
class Rating(models.Model):
	timestamp = models.DateTimeField(default=now(), verbose_name="Сейчас") 
	poiID = models.CharField(max_length=32, verbose_name="Пароль")
	type = models.CharField(max_length=100, verbose_name="Тип")
	user = models.ForeignKey(User, on_delete=models.CASCADE)

