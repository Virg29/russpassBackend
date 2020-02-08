from django.db import models

# Create your models here.
class POI(models.Model):
	id = models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
	type = models.CharField(max_length=16, unique=False)
	address = models.CharField(max_length=16, unique=False)
	latit = models.CharField(max_length=16, unique=False)
	longit = models.CharField(max_length=16, unique=False)
	description = models.CharField(max_length=150, unique=False, default="Отличное место, чтобы посетить")
	title = models.CharField(max_length=150, unique=False)
	def __str__(self):
		return "POI_id: {}, type: {}, address: {}, lat: {}, long: {}"\
			.format(self.id, self.type, self.address, self.lat, self.long);