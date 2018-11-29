from rest_framework import serializers
from .models import Perro, Cliente

class PerroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Perro
        fields = ('id', 'nombre', 'raza', 'descripciom', 'img',)

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = ('id', 'nombre', 'apellido', 'email', 'password',)