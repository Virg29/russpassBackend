from django.shortcuts import render
from builder.similirity import Predictions
from rest_framework import generics
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rating.serializers import RatingSer
from rating.models import Rating
from register.models import User

@api_view(http_method_names=['GET'])
def getSimilar(request):
	# Заглушка 
	childs = Rating.objects.all()
	print(childs)
	return Response({"status": Predictions.getPrediction(1)})

class ActionHandler(generics.ListAPIView):
	serializer_class = RatingSer
	queryset = User.objects.select_related().all()