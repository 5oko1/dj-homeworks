import datetime

from django.shortcuts import render

from books.models import Book


def books_view(request):
    template = 'books/books_list.html'
    all_books = Book.objects.all()
    context = {'books': all_books}
    return render(request, template, context)


def pub_date_view(request, date):
    template = 'books/publish_catalog.html'
    date_params = date.split('-')
    date_params = [int(d) for d in date_params]
    user_date = datetime.date(*date_params)
    published_books = Book.objects.filter(pub_date=user_date)

    prev_date = user_date - datetime.timedelta(days=1)
    future_date = user_date + datetime.timedelta(days=1)
    context = {'books': published_books,
               'previous_date': prev_date.strftime('%Y-%m-%d'),
               'future_date': future_date.strftime('%Y-%m-%d')}
    return render(request, template, context)
