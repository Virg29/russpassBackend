from rest_framework import serializers
from rating.models import Rating

class RatingSer(serializers.ModelSerializer):
	class Meta:
		model = Rating
		fields = ["user","poiID","type"]