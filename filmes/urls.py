from django.urls import path
from . import views

app_name = "filmes"

urlpatterns = [
    path("", views.lista_filmes, name="lista_filmes"),
]