from django.db import models
from ativos.views import Ativo


class Rendimentos(models.Model):
    data = models.DateField()
    valor = models.DecimalField(max_digits=6, decimal_places=2)
    obs = models.TextField(blank=True)
    ativo = models.ForeignKey(Ativo, on_delete=models.CASCADE)

    def __str__(self):
        return self.ativo

