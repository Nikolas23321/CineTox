from django.shortcuts import render
from .models import Categoria, Diretor, Filme

# Create your views here.

def lista_filmes(request):
    termo_busca = request.GET.get("q", "").strip()
    diretor_id = request.GET.get("diretor", "").strip()
    categoria_id = request.GET.get("categoria", "").strip()

    filmes = Filme.objects.select_related("diretor", "categoria").all()

    if termo_busca:
        filmes = filmes.filter(titulo__icontains=termo_busca)

    if diretor_id:
        filmes = filmes.filter(diretor_id=diretor_id)

    if categoria_id:
        filmes = filmes.filter(categoria_id=categoria_id)

    diretores = Diretor.objects.all()
    categorias = Categoria.objects.all()

    context = {
        "filmes": filmes,
        "termo_busca": termo_busca,
        "diretores": diretores,
        "categorias": categorias,
        "diretor_selecionado": diretor_id,
        "categoria_selecionada": categoria_id,
    }
    return render(request, "filmes/lista_filmes.html", context)