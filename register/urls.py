from django.urls import path, include
from register.views import *

urlpatterns = [
	path('register/', RegisterNewUser.as_view()),
	path('login/', Login),
]