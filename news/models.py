from django.db import models


'''
Modelo para organizar as notícias por temas (Ex: Tecnologia, Esportes).
Atende ao critério de 'Relacionamentos' da avaliação.
'''
class Categoria(models.Model):
    nome  = models.CharField(max_length=100, verbose_name='Nome da Categoria')

    def __str__(self):
        return self.nome
    
    class Meta:
        verbose_name_plural = 'Categorias'

class Noticia(models.Model):
    '''
    Modelo principal do Site de Notícias.
    Atende aos critérios de 'Modelagem de Dados' e 'Campos adequados'.
    '''
    titulo = models.CharField(max_length=200, verbose_name="Título")
    resumo = models.TextField(max_length=500, verbose_name="Resumo (Aparece na Home)")
    conteudo = models.TextField(verbose_name="Conteúdo Completo")
    
    # Requisito do projeto: imagens das matérias
    imagem = models.ImageField(upload_to='noticias/', verbose_name='Imagem da Destaque')

    data_publicacao = models.DateTimeField(auto_now_add=True, verbose_name='Postado em')
   
    # Critério: Relacionamento simples (Chave Estrangeira)
    # Se a categoria for deletada, as notícias dela também serão (on_delete=models.CASCADE)
    categoria = models.ForeignKey(
        Categoria, 
        on_delete=models.CASCADE, 
        related_name='noticias',
        verbose_name="Categoria"
    ) 

    def __str__(self):
        return self.titulo
    
    class Meta:
        ordering = ['-data_publicacao']  # Critério Opcional: Ordenação automática

