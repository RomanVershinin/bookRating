from django.shortcuts import render

# Create your views here.
from .models import Books

def index(request):
    books = Books.objects.all()
    content = {
            "books" :   books
        }
    return render(request, './portal/index.html', content)

def detail(request, id):
    print(id)
    book = Books.objects.get(id=id)
    content = {
            "book" :   book
        }
    return render(request, './portal/detail.html', content)
