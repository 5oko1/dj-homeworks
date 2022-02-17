from django.shortcuts import render, redirect

from phones.models import Phone


def index(request):
    return redirect('catalog')


def show_catalog(request):
    template = 'catalog.html'
    phone_objects = Phone.objects.all()
    sorted_phones = _sort_phone_obj(phone_objects, request.GET.get('sort'))
    context = {'phones': sorted_phones}
    return render(request, template, context)


def _sort_phone_obj(phones, sort_key):
    """Возвращает отсортированный список объектов телефонов

    :param phones: список объектов Phone
    :param sort_key: ключ сортировки (name/min_price/max_price)
    :return: отсортированный список
    """

    if sort_key == 'name':
        phone_objects = sorted(phones, key=lambda x: x.name)
    elif sort_key == 'min_price':
        phone_objects = sorted(phones, key=lambda x: x.price)
    elif sort_key == 'max_price':
        phone_objects = sorted(phones, key=lambda x: x.price, reverse=True)
    else:
        phone_objects = phones

    return phone_objects


def show_product(request, slug):
    template = 'product.html'
    phone_object = Phone.objects.filter(slug=slug)
    context = {'phone': phone_object[0]}
    return render(request, template, context)
