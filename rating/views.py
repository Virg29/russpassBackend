from django.shortcuts import render

class ActionHandler(generics.CreateAPIView):
	serializer_class = UserRegister
