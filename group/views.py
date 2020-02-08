from django.shortcuts import render
from rest_framework import generics
from group.serializers import GroupSer
from group.models import Group
class getList(generics.ListAPIView):
	serializer_class = GroupSer
	queryset = Group.objects.all()
# Create your views here.
class create():
	pass
class join():
	pass
class getContent():
	pass