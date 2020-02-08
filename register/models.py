from django.db import models
#from group.models import Group
# Create your models here.
class User(models.Model):
	id = models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
	name = models.CharField(max_length=16, verbose_name="Имя пользователя", unique=True)
	password = models.CharField(max_length=16, verbose_name="Пароль")
	balance = models.IntegerField(verbose_name="Баланс пасскоинов", default=0)
	level = models.DecimalField(decimal_places=2, max_digits=5, verbose_name="Уровень", default=0)
	image = models.CharField(max_length=16, verbose_name="Название статической аватарки", default='0')
	def __str__(self):
		return "user_id: {}, level: {}, balance: {}, image: {}, password: {}"\
			.format(self.name, self.level, self.balance, self.image, self.password);
