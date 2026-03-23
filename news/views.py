from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Noticia
from .models import Categoria

class NoticiaListView(ListView):
    model = Noticia
    template_name = 'news/index.html'
    context_object_name = 'noticias'
    paginate_by = 6

    def get_queryset(self):
        queryset = super().get_queryset()

        search = self.request.GET.get('search')
        if search:
            queryset = queryset.filter(titulo__icontains=search)

        categoria = self.request.GET.get('categoria')
        if categoria:
            queryset = queryset.filter(categoria__id=categoria)

        order = self.request.GET.get('order')
        if order == 'recent':
            queryset = queryset.order_by('-id')
        elif order == 'old':
            queryset = queryset.order_by('id')

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categorias'] = Categoria.objects.all()
        return context

class NoticiaDetailView(DetailView):
    model = Noticia
    template_name = 'news/detalhe.html'
    context_object_name = 'noticia'