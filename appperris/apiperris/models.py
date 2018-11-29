from django.db import models

class Perro(models.Model):
    nombre = models.TextField(max_length=100)
    raza = models.TextField(max_length=100)
    descripciom = models.TextField(max_length=100)
    img = models.FileField(null=True, blank=True)

class Cliente(models.Model):
    nombre = models.TextField(max_length=100)
    apellido = models.TextField(max_length=100)
    email = models.TextField(max_length=100)
    password = models.TextField(max_length=100)