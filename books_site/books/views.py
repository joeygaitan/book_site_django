from django.shortcuts import render
from .models import Book

# Create your views here.

# Home View
def home(request):
    context = {
        'books': Book.objects.all()
    }
    return render(request, 'home.html', context)


# Detail View
def detail(request, book_id):
    context = {
        'book': Book.objects.get(id=book_id)
    }
    return render(request, 'detail.html', context)