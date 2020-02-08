from django.urls import path, include
from rating.views import *

urlpatterns = [
	path('actionhandler/', ActionHandler.as_view()),
]