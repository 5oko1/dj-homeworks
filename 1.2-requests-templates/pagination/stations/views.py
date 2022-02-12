from csv import DictReader

from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.urls import reverse

from pagination import settings


def index(request):
    return redirect(reverse('bus_stations'))


DATA = list()
with open(settings.BUS_STATION_CSV, encoding='utf-8') as csvfile:
    reader = DictReader(csvfile)
    for row in reader:
        DATA.append(row)


def bus_stations(request):

    page_number = int(request.GET.get('page', 1))
    paginator = Paginator(DATA, 15)
    page = paginator.get_page(page_number)

    context = {
        'bus_stations': page.object_list,
        'page': page,
    }
    return render(request, 'stations/index.html', context)
