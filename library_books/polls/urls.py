from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views


urlpatterns = [
    # path(route name, function name, file html name)
    path("", views.index, name="index"),
    path("about/", views.about, name="about"),
    path("books/", views.books, name="books"),
    path("books/add", views.create_book, name="add"),
    path("books/edit", views.edit_book, name="edit"),
    path("delete/<int:id>", views.delete_book, name="delete"),
    path("books/edit/<int:id>", views.edit_book, name="edit"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)