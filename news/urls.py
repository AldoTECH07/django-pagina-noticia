from django.urls import path
from .views import NoticiaListView, NoticiaDetailView

urlpatterns = [
    path('', NoticiaListView.as_view(), name='home'),
    path('noticia/<int:pk>/', NoticiaDetailView.as_view(), name='noticia_detalhe'),
]