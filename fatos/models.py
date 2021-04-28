from django.db import models
from ativos.views import Ativo


class FatosRelevantes(models.Model):
    data = models.DateField()
    fato = models.TextField("Fato Relevante", max_length=200)
    solucao =  models.TextField("Solução", max_length=200, null=True, blank=True)
    solucionado = models.BooleanField("Solucionado")
    ativo = models.ForeignKey(Ativo, on_delete=models.CASCADE)

    def __str__(self):
        return self.fato

