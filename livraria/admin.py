from django.contrib import admin

from .models import Autor, Editora, Categoria, Livro

admin.site.register(Autor)
admin.site.register(Editora)
admin.site.register(Categoria)
admin.site.register(Livro)


