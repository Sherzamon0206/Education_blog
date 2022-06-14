from django.urls import path
from .views import *
urlpatterns = [
	
	

	path('news/',NewsView,name='yangiliklar'),
	path('news/<slug:slug>/', newsDetailView, name = 'news_detail')

]