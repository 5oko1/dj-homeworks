import datetime
import os

from django.http import HttpResponse
from django.shortcuts import render, reverse


def home_view(request):
    template_name = 'app/home.html'
    pages = {
        'Главная страница': reverse('home'),
        'Показать текущее время': reverse('time'),
        'Показать содержимое рабочей директории': reverse('workdir')
    }
    
    # context и параметры render менять не нужно
    # подбробнее о них мы поговорим на следующих лекциях
    context = {
        'pages': pages
    }
    return render(request, template_name, context)


def time_view(request):
    now = datetime.datetime.now()
    msg = f'Текущее время: {now.strftime("%H:%M:%S")} <br><a href={reverse("home")}>На главную</a>'
    return HttpResponse(msg)


def workdir_view(request):
    files = '<br>'.join(os.listdir())
    msg = f'Список файлов в текущей директории: <br>{files} <br><a href={reverse("home")}>На главную</a>'
    return HttpResponse(msg)
