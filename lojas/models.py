from django.db import models

# Create your models here.
class Lojas(models.Model):
    nome_loja = models.CharField(max_length=100)
    dono_da_loja = models.CharField(max_length=100)
    saldo_loja = models.IntegerField(default=0)
    data_criacao = models.DateTimeField(auto_now_add=True)
    data_atualizacao = models.DateTimeField(auto_now=True)