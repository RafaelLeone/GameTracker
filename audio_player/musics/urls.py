from django.urls import path

from . import views

urlpatterns = [
    path("add_song", views.add_song),
    path("edit_song", views.edit_song),
    path("list_songs", views.list_songs),
]
