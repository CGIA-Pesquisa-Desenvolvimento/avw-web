from django.db import models
from ativos.models import Ativo


class VendaAtivo(models.Model):
    data_saida = models.DateField()
    valor_venda_cota = models.DecimalField(max_digits=7, decimal_places=2)
    quantidade_cotas = models.IntegerField("Quantidade de Cotas")
    valor_patrimonial_final = models.DecimalField(max_digits=14, decimal_places=2)
    valor_mercado_final = models.DecimalField(max_digits=14, decimal_places=2)
    motivo_venda = models.TextField()
    ativo = models.ForeignKey(Ativo, on_delete=models.CASCADE)