from django.urls import path
from .views import XizmatlarPageView

urlpatterns = [

	path('xizmatlar/', XizmatlarPageView.as_view(), name='xizmatlar'),
	


]