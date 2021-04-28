from datetime import (datetime,
                      date)
from calendar import monthrange

from pesquisa_banco_dados.periodo_registros import periodo_registro

#from pesquisa_banco_dados.pesquisa_periodo import periodo_registro
from dateutil.relativedelta import *


def convertep_aa_mm_dd(data):
    """
    Converte uma string no padrão dd/mm/aaaa em aaaa-mm-dd
    :param data:
    :return:
    """
    temp = data.split('/')
    dia = temp[0]
    mes = temp[1]
    ano = temp[2]

    return ano + '-' + mes + '-' + dia


def retorna_primeiro_ultimo_dia_mes(data):
    """
    Recede string com formatação dd/mm/aaaa e retorna duas string indormando o primeiro dia e o último dia do mês
    :param data: string no formato de data dd/mm/aaaa
    :return: Retorna string no padrão aaaa-mm-dd do primeiro dia e o último dia do mês
    """
    #final = datetime.strptime(data, '%d/%m/%Y').date()
    data_split = data.split('/')
    mes = data_split[1]
    ano = data_split[2]
    ultimo_dia = monthrange(int(ano), int(mes))
    str_data_inicial = ano + '-' + mes + '-' + '1'
    str_data_final = ano + '-' + mes + '-' + str(ultimo_dia[1])
    primeiro_ultimo_dia_mes = (str_data_inicial, str_data_final)
    return primeiro_ultimo_dia_mes


def retorna_dia_correntet():
    """
    Retorna o dia de hoje no formato aaaa-mm-dd
    :return:
    """
    class_data_atual = date.today()
    str_data_atual = '{}-{}-{}'.format(class_data_atual.year, class_data_atual.month, class_data_atual.day)
    data_class_str = (class_data_atual, str_data_atual)
    return data_class_str


def retorna_dia_correnteb():
    """
    Retorna o dia de hoje no formato aaaa-mm-dd
    :return: class datatime e string no formato aaaa-mm-dd
    """
    class_data_atual = date.today()
    str_data_atual = '{}/{}/{}'.format(class_data_atual.day, class_data_atual.month, class_data_atual.year)
    data_class_str = (class_data_atual, str_data_atual)
    return data_class_str


def converteb_dd_mm_yy(data):
    """
    converte uma string no padrão
    :param data:
    :return:
    """
    temp = data.split('/')
    dia = temp[0]
    mes = temp[1]
    ano = temp[2]

    return dia + '/' + mes + '/' + ano


def gera_string_data(data):
    dataFormatada = data.strftime('%d/%m/%Y')
    return dataFormatada


def convertet_dd_mm_aaaa(data):
    temp = data.split('-')
    ano = temp[0]
    mes = temp[1]
    dia = temp[2]

    return dia + '/' + mes + '/' + ano


def completa_formatacao_mes(mes, ano):
    conjunto_meses_inicial_final = []
    for contador in range(len(mes)):
        m = mes[contador]
        a = ano[contador]
        data = '1' + '/' + str(m) + '/' + str(a)
        conjunto_meses_inicial_final.append(retorna_primeiro_ultimo_dia_mes(data))

    return conjunto_meses_inicial_final


def periodo_meses():
    """
    Gera os meses e anos anteriores a data do último registro
    :param data_atual: data corrente
    :param num_meses: numero de meses qu serão retrocedidos
    :return: Tupla do tipo int com os meses[0]e anos[1] registrados
    """
    meses_registrados = []
    anos_registrados = []

    hoje = retorna_dia_correntet()
    #periodo_mes = retorna_primeiro_ultimo_dia_mes(hoje)
    data_maior_menor = periodo_registro()
    d_maior = data_maior_menor[0]
    d_menor = data_maior_menor[1]
    intevalo_tempo = d_maior.month - d_menor.month
    for contador in range(intevalo_tempo + 1):
        dado = data_maior_menor[0] - relativedelta(months=contador)
        meses_registrados.append(dado.month)
        anos_registrados.append(dado.year)
    data_completas = completa_formatacao_mes(meses_registrados, anos_registrados)
    return meses_registrados, anos_registrados, data_completas


