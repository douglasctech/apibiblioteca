from bibliotecaapp.serializer import LivrosSerializer
from rest_framework import viewsets
from bibliotecaapp.models import Livros


class LivrosViewSet(viewsets.ModelViewSet):
    queryset = Livros.objects.all()
    serializer_class = LivrosSerializer