from rest_framework import serializers

from .models import Proyecto, Categoria, Tecnologia

class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = '__all__'

class TecnologiaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tecnologia
        fields = ['id', 'nombre'] # otra manera de especificar los campos

class ProyectoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Proyecto
        fields = '__all__'
        # fields = ['id', 'titulo', 'descripcion', 'categoria', 'tecnologias']

