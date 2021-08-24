from django.contrib import admin
from bibliotecaapp.models import Livros


class Livro(admin.ModelAdmin):
    list_display = ('id', 'nome', 'autor', 'categoria')
    list_display_links = ('id', 'nome', 'autor', 'categoria')
    search_fields = ('nome',)


admin.site.register(Livros)
