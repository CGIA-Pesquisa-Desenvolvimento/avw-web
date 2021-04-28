from ativos.models import Ativo
from rendimentos.models import Rendimentos

from django.db.models import Sum

def periodo_registro():
    """
    Verifica a primeira e última datas registradas na tabela Movimentacoes
    :return: Tupla com a data do último registro [0] e a data do primeiro regidtro [1]
    """
    p = Rendimentos.objects.all().first() #TODO Verificar o não retorno das datas
    u = Rendimentos.objects.all().last()

    return u.data, p.data


def valor_mes(quantidade_meses): #TODO **1 Criar queryset que retorne a quantidade de cotas e os valores dos rendimentosvde cada fundo. Multiplicar e calcular o montante do mes
    d = ['2020-02-01', '2020-02-28']#TODO **2 realizar loop com as datas encontradas pelo periodo_registro e aplicar naqueryset acima **1
  #  valores = [] #TODO Colocar os resultado obtidos por **2 em uma lista **2
    for v in range(quantidade_meses):
        valores = Rendimentos.objects.all().filter(data__range=[d[0], d[1]]).aggregate(Sum('valor'))
    return valores['valor__sum']

