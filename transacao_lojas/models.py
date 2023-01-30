from django.db import models
from lojas.models import Lojas

# Create your models here.
class TransacaoLojas(models.Model):
    tipo = models.IntegerField()
    data = models.CharField(max_length=100)
    valor = models.IntegerField()
    cpf = models.CharField(max_length=20)
    cartao = models.CharField(max_length=20)
    hora = models.CharField(max_length=100)
    loja = models.ForeignKey(Lojas, on_delete=models.CASCADE, related_name="lojas_transacao")