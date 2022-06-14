from django.urls import path
from .views import ict_workPageView

urlpatterns = [

	path('ictwork/', ict_workPageView.as_view(), name='ictwork'),

]