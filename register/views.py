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

@api_view(['POST'])
def Login(request):
	userLogin = request.data.get("login")
	password = request.data.get("password")
	user = User.objects.filter(name=userLogin);
	#password = user.get(password)
	#print(password)
	return Response({"status": True})
	#return Response(request)