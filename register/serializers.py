from rest_framework import serializers
from register.models import User

class UserRegister(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = ["name", "password"]