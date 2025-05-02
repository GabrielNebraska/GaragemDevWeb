from email.policy import default
from django import models
from django.forms import CharField 

class Veiculo(models.Model):
    
    ano = IntegerField(null = True, default = 0)
    preco = DecimalField(decimal_places = 2)
    cor = ForeingKey(Cor, on_delete=models.CASCADE)
    modelo = ForeingKey(Modelo, on_delete=models.CASCADE)
    acessorio = ForeingKey(Acessorio, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.id}, {self.model}, {self.cor}"