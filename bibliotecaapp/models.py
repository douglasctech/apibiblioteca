from django.db import models
from django.db.models.fields import CharField

class Livros(models.Model):
    nome = CharField(max_length=90)
    autor = CharField(max_length=50)
    categoria = CharField(max_length=50)

    def __str__(self):
        return self.nome
