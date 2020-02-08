from django.shortcuts import render
from rest_framework import generics
from group.serializers import GroupSer
from group.models import Group
from register.models import User
class getList(generics.ListAPIView):
	serializer_class = GroupSer
	queryset = Group.objects.all()
# Create your views here.
@api_view(http_method_names=['POST'])
def create(request):
	groupTitle = request.data.get("title")
	groupDescr = request.data.get("descr")
	invatedUsers = request.data.get("Users")
	for i in invatedUsers:
		user = User.objects.filter(name=i)
		if(len(user)==1):
			user = user.filter(password=password)
			user.Groups.add()
			return Response({"status": True})
		else:
			return Response({"status": False})

class join():
	pass
class getContent():
	pass