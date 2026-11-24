from django.shortcuts import render
from .models import Filme

# Create your views here.

def lista_filmes(request):
    termo_busca = request.GET.get("q", "").strip()


    filmes = Filme.objects.select_related("diretor", "categoria").all()


    if termo_busca:
        filmes = filmes.filter(titulo__icontains=termo_busca)


    context = {
        "filmes": filmes,
        "termo_busca": termo_busca,
    }
    return render(request, "filmes/lista_filmes.html", context)