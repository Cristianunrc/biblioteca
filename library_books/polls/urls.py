from django.urls import path
from . import views

urlpatterns = [
    # path(route name, function name, file html name)
    path("", views.index, name="index"),
    path("about/", views.about, name="about"),
    path("books/", views.books, name="books"),
    path("books/add", views.create_book, name="add"),
]