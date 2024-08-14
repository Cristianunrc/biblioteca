from django.shortcuts import render

def index(request):
    return render(request, "views/index.html")

def about(request):
    return render(request, "views/about.html")

def books(request):
    return render(request, "books/index.html")

def create_book(request):
    return render(request, "books/add.html")

def edit_book(request):
    return render(request, "books/edit.html")