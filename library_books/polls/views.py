from django.shortcuts import render, redirect
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
    form = BookForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect("books")
    return render(request, "books/add.html", {'form': form})

def edit_book(request):
    return render(request, "books/edit.html")

def delete_book(request, id):
    book = Book.objects.get(id=id)
    book.delete()
    return redirect("books")