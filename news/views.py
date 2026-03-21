from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Noticia

class NoticiaListView(ListView):
    model = Noticia
    template_name = 'news/index.html'
    context_object_name = 'noticias'
    paginate_by = 6 # Critério 7 (Paginação)

class NoticiaDetailView(DetailView):
    model = Noticia
    template_name = 'news/detalhe.html'
    context_object_name = 'noticia'