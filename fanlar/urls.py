from django.urls import path
from .views import homePageView, KurslarPageView, FanlarDetailView, AboutPageView, course_search, registerStudentView

urlpatterns = [
	path('kurs_search/', course_search, name='kurs_search'),
	path('register_student/', registerStudentView, name='register_student'),
	path('kurslar/', KurslarPageView, name='kurslar'),
	
	path('course/<slug:slug>/', FanlarDetailView, name='kurslar_item'),

	path('about/', AboutPageView.as_view(), name = 'about'),
	
	path('',homePageView, name='home'),

	
]