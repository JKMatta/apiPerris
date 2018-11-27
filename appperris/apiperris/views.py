from .models import Perro, Cliente
from .serializers import PerroSerializer, ClienteSerializer
from rest_framework import viewsets

class PerroViewSet(viewsets.ModelViewSet):
 
    serializer_class = PerroSerializer
    queryset = Perro.objects.all()

class ClienteViewSet(viewsets.ModelViewSet):
 
    serializer_class = ClienteSerializer
    queryset = Cliente.objects.all()
