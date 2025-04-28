from django import models
from django.forms import CharField 

class Modelo(models.Model):
    nome = CharField(max_length=80)
    marca = CharField(max_length=80, null=True)
    categoria = CharField(max_length=80, null=True)
    
    def __str__(self):
        return self