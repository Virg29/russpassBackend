from django.db import models
from register.models import User
from django.utils.timezone import now
class Rating(models.Model):
	timestamp = models.DateTimeField(default=now(), verbose_name="Сейчас") 
	poiID = models.CharField(max_length=32, verbose_name="Пароль")
	value = models.DecimalField(decimal_places=4, max_digits=5, verbose_name="Значение", default=0)

