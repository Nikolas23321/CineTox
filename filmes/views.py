from urllib.parse import urlencode
from django.core.paginator import Paginator
from django.shortcuts import render
from .models import Categoria, Diretor, Filme

# Create your views here.

def lista_filmes(request):
    termo_busca = request.GET.get("q", "").strip()
    diretor_id = request.GET.get("diretor", "").strip()
    categoria_id = request.GET.get("categoria", "").strip()
    numero_pagina = request.GET.get("page")

    filmes = Filme.objects.select_related("diretor", "categoria").all()

    if termo_busca:
        filmes = filmes.filter(titulo__icontains=termo_busca)

    if diretor_id:
        filmes = filmes.filter(diretor_id=diretor_id)

    if categoria_id:
        filmes = filmes.filter(categoria_id=categoria_id)

    paginator = Paginator(filmes, 5)
    page_obj = paginator.get_page(numero_pagina)

    filtros_ativos = {}
    if termo_busca:
        filtros_ativos["q"] = termo_busca
    if diretor_id:
        filtros_ativos["diretor"] = diretor_id
    if categoria_id:
        filtros_ativos["categoria"] = categoria_id

    querystring = urlencode(filtros_ativos)

    diretores = Diretor.objects.all()
    categorias = Categoria.objects.all()

    context = {
        "filmes": page_obj,
        "page_obj": page_obj,
        "termo_busca": termo_busca,
        "diretores": diretores,
        "categorias": categorias,
        "diretor_selecionado": diretor_id,
        "categoria_selecionada": categoria_id,
        "querystring": querystring,
    }
    return render(request, "filmes/lista_filmes.html", context)