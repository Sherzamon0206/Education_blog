from django.shortcuts import render

from django.views.generic import TemplateView


# Create your views here.

class ict_workPageView(TemplateView):
    template_name = 'ict_work.html'
