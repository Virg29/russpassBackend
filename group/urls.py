from django.urls import path, include
from group.views import *

urlpatterns = [
	path('create/', create),
	path('list/', getList.as_view()),
	#path('content/', getContent.as_view()),
	#path('join/', join.as_view()),
]