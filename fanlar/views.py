from os import name
from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from .models import Kurslar, Section, Cantact, AboutPage,Teachers, Registered_students
from django.http import HttpResponse
from django.http import JsonResponse
import json

def homePageView(request):
    teachers = Teachers.objects.all()
    return render(request, 'home.html', {'Kurslar':Kurslar.objects.all(), 'Teachers':teachers})


class HomePageView(ListView):
    model = Kurslar
    template_name = 'home.html'


# class FanlarPageView(ListView):
#     model = Fanlar
#     template_name = 'kurslar.html'
def course_search(request):
    if request.method == "POST":

        data = json.loads(request.body)['name']
        kurslar = Kurslar.objects.all()
        datas = {}
        response = []
        for i in kurslar:
            if data in i.name:
                datas['name'] = i.name
                datas['slug'] = i.slug
                response.append(datas)
                datas = {}



        return JsonResponse({'data': response})
def registerStudentView(request):
    if request.method == "POST":
        data = json.loads(request.body)
        print(data)
        Registered_students.objects.create(name=data['student_name'], kurs=data['kurs_name'], phone=data['student_phone']).save()





        return JsonResponse({'data': 'ok'})


def KurslarPageView(request):
    if request.method == "POST":
        print(request.POST.data)
        return {'data': 'ok'}
    return render(request=request, template_name='kurslar.html', context={"Kurslar": Kurslar.objects.all()})


def FanlarDetailView(request, slug):
    kurs = Kurslar.objects.get(slug=slug)
    Sections = Section.objects.filter(course=kurs)
    return render(request=request, template_name='kurslar_item.html', context={"kurs": kurs, 'Sections': Sections})


# class FanlarDetailView(DetailView):
#     model = Kurslar
#     template_name = 'kurslar_item.html'


class AboutPageView(ListView):
    model = AboutPage
    template_name = 'about.html'


def cantact(request):
    if request.method == 'POST':
        contact = Cantact()
        name = request.POST.get('name')
        tell = request.POST.get('tell')
        contact.name = name
        contact.tell = tell
        contact.save()
        # return HttpResponse('<h1>Raxmad</h1>')
    return render(request, 'kurslar_item.html')
