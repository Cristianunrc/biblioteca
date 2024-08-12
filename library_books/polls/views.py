from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
  return render(request, "views/index.html")

def about(request):
  return render(request, "views/about.html")

def books(request):
  return render(request, "books/index.html")

def create_book(request):
  return render(request, "books/add.html")