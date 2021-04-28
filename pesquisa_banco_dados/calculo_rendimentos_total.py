
"""
Calcula o total de rendimentos do período
"""
from utils.datas import periodo_meses
from rendimentos.models import Rendimentos

import datetime
from django.db.models import Sum


def calculo_rendimentos():
    periodo = periodo_meses()
    c = len(periodo[2])
    mes = []
    rendimento = []
    for x in range(c):
        d2 = periodo[2]
        maux = d2[x]
        data_inicial = maux[0]
        data_final = maux[1]
        m = data_inicial.split('-')
        a1 = m[0]
        a2 = m[1]
        # data_inicial = periodo[2, mes, 0]
        # data_final = periodo[2, mes, 1]
        # m = m[2]
        # if

        mes.append(m[1])

        r = Rendimentos.objects.filter(data__range=(data_inicial, data_final)).aggregate(Sum('valor'))
        rendimento.append(r)
    return mes, rendimento





