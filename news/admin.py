from django.contrib import admin
from .models import Categoria, Noticia

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('nome',)

@admin.register(Noticia)
class NoticiaAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'categoria', 'data_publicacao')
    search_fields = ('titulo', 'resumo')
    list_filter = ('categoria', 'data_publicacao')