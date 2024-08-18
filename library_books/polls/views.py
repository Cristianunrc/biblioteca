from django.shortcuts import render
from .models import Book
from .forms import BookForm

def index(request):
    return render(request, "views/index.html")

def about(request):
    return render(request, "views/about.html")

def books(request):
    books = Book.objects.all()
    return render(request, "books/index.html", {'books': books})

def create_book(request):
    form = BookForm(request.POST or None)
    return render(request, "books/add.html", {'form': form})

def edit_book(request):
    return render(request, "books/edit.html")