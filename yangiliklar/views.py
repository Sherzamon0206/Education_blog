from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from .models import News

def NewsView(request):
    return render(request=request, template_name='yangiliklar.html', context={"News": News.objects.all()})


def newsDetailView(request, slug):

    Last_news = News.objects.all().order_by('created_data')[:7]
    News_detail = News.objects.get(slug=slug)

    News_detail.views+=1
    News_detail.save()

    data = News_detail.text.split('.')
    text1 = ''
    text2 = ''
    for i in range(len(data)-3):
        text1+=data[i]+'.'
    text2=data[-3]+'.'+data[-2]+'.'

    return render(request, 'news_detail.html', {'News_detail': News_detail, 'txt1':text1, 'txt2':text2, 'Last_News': Last_news})

