from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
  return HttpResponse("Hello to the library books!")

def about(request):
  return render(request, "views/about.html")

def books(request):
  return render(request, "books/index.html")