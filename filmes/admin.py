from django.contrib import admin
from .models import Categoria, Diretor, Filme

# Register your models here.

@admin.register(Diretor)
class DiretorAdmin(admin.ModelAdmin):
    list_display = ("id", "nome")
    search_fields = ("nome",)

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ("id", "nome")
    search_fields = ("nome",)

@admin.register(Filme)
class FilmeAdmin(admin.ModelAdmin):
    list_display = ("id", "titulo", "diretor", "categoria", "ano_lancamento")
    list_filter = ("diretor", "categoria")
    search_fields = ("titulo", "diretor__nome", "categoria__nome")