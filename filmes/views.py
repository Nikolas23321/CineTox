from django.shortcuts import render
from .models import Filme

# Create your views here.

def lista_filmes(request):
    filmes = Filme.objects.select_related("diretor", "categoria").all()

    context = {
        "filmes": filmes,
    }
    return render(request, "filmes/lista_filmes.html", context)