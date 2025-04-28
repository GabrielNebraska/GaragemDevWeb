from django import models
from django.forms import CharField 

class Cor(models.Model):
    nome = CharField(max_length=255)
    
    def __str__(self):
        return self