from django.shortcuts import render
from rest_framework import generics
from group.serializers import GroupSer
from group.models import Group
from register.models import User
from rest_framework.decorators import api_view

class getList(generics.ListAPIView):
	serializer_class = GroupSer
	queryset = Group.objects.all()
# Create your views here.
@api_view(http_method_names=['POST'])
def create(request):
	groupTitle = request.data.get("title")
	groupDescr = request.data.get("descr")
	invatedUsers = request.data.get("users")
	for i in invatedUsers:
		user = User.objects.filter(name=i)
		if(len(user)==1):
			a=Group(title=groupTitle,descr=groupDescr)
			a.save()
			a.Users.add(user)
			#user.Groups.add()
			return Response({"status": True})
		else:
			return Response({"status": False})

class join():
	pass
class getContent():
	pass