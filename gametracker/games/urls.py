from django.urls import path

from . import views

urlpatterns = [
    path("add_game", views.add_game),
    path("list_games", views.list_games),
    path("delete_game", views.delete_game)
]
