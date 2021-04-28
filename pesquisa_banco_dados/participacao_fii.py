from ativos.models import Ativo

from django.db.models import Sum


def participacao_fii():
    fii = []
    n_cotas = []
    dados1 = Ativo.objects.all()
    aux = ''
    contador = len(dados1)
    for c in range(contador):


        codigo = dados1[c].codigo
       # n_cotas.append(dados2[c].numero_cotas_adquiridas)
        if codigo != aux:
            total = Ativo.objects.filter(codigo=dados1[c].codigo).aggregate(Sum('numero_cotas_adquiridas'))
            n_cotas.append(total['numero_cotas_adquiridas__sum'])
            fii.append(dados1[c].codigo)
            aux = codigo
    return fii, n_cotas
