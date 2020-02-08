from django.shortcuts import render
from rest_framework import generics
from rating.serializers import RatingSer
from register.models import User

class ActionHandler(generics.ListAPIView):
	serializer_class = RatingSer
	queryset = User.objects.all()
