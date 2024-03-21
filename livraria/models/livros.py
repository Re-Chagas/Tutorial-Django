from django.db import models

from livraria.models import Categoria, Editora
       
class Livro(models.Model):
    titulo = models.CharField(max_length=255)
    isbn = models.CharField(max_length=32, null=True, blank=True)
    quantidade = models.IntegerField(default=0, null=True, blank=True)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    Categoria = models.ForeignKey(                                      
        Categoria, on_delete=models.PROTECT, related_name="livros"
    )
    Editora = models.ForeignKey(
        Editora, on_delete=models.PROTECT, related_name="livros"
    )
    
    def __str__(self):
        return f"{self.titulo} {self.quantidade}"