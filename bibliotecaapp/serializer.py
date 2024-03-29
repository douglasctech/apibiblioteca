from rest_framework import serializers
from bibliotecaapp.models import Livros


class LivrosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Livros
        fields = ['id', 'nome', 'autor', 'categoria']