from rest_framework import serializers
from group.models import Group

class GroupSer(serializers.ModelSerializer):
	class Meta:
		model = Group
		fields = "__all__"