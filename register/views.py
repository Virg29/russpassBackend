from django.shortcuts import render
from rest_framework import generics
from register.serializers import UserRegister
from register.models import User 
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.
class RegisterNewUser(generics.CreateAPIView):
	serializer_class = UserRegister

@api_view(http_method_names=['POST'])
def Login(request):
	userLogin = request.data.get("login")
	password = request.data.get("password")
	user = User.objects.filter(name=userLogin)
	if(len(user)==1):
		user = user.filter(password=password)
		if(len(user)==1):
			return Response({"status": True})
		else:
			return Response({"status": False})
	else:
		return Response({"status": False})
	#passwordFromDb = user.get(password)
	#print(password)
	
	#return Response(request)