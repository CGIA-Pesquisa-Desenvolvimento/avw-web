from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.views.generic import TemplateView
import io
from pesquisa_banco_dados.calculo_rendimentos_total import calculo_rendimentos
from pesquisa_banco_dados.participacao_fii import participacao_fii
from chartjs.views.lines import BaseLineChartView
from django.http import FileResponse
# from reportlab.pdfgen import canvas
from pesquisa_banco_dados.periodo_registros import valor_mes
from random import randint
from pesquisa_banco_dados import calculo_rendimentos_total

from django.contrib.auth.mixins import LoginRequiredMixin


def relatorios(request):
    return render(request, 'relatorios/relatorios.html')


def ReportLab():
    pass

    # # response = HttpResponse(content_type='application/pdf')
    # # response['Content-Disposition'] = 'attachiment; filename="mypdf.pdf"'
    #
    # buffer = io.BytesIO()
    # p = canvas.Canvas(buffer)
    #
    # p.drawString(10, 810, 'hello word') #x, y
    #
    # # palavras = ['palavra1', 'palavra2', 'palavra3']
    # #
    # # y = 790
    # # for palavra in palavras:
    # #     p.drawString(10, y, palavra)
    # #     y -= 20
    #
    # p.showPage()
    # p.save()
    #
    # # pdf = buffer.getvalue()
    # # buffer.close()
    # # response.writable(pdf)
    #


#    return FileResponse(buffer, as_attachment=True, filename='hello.pdf')


class GraficoRendimentoMesView(LoginRequiredMixin, TemplateView):
    template_name = 'relatorios/grafo.html'


class Dados(LoginRequiredMixin, BaseLineChartView):
    def get_labels(self):
        """Retorna 12 labels para a representação do x"""
        ativos = calculo_rendimentos_total()
        labels = ativos[0]
        return labels

    def get_providers(self):
        """Retorna os nomes dos datasets."""
        datasets = [
           "Rendimentos"
        ]
        return datasets

    def get_data(self):
        """
        Retorna 6 datasets para plotar o gráfico.

        Cada linha representa um dataset.
        Cada coluna representa um label.

        A quantidade de dados precisa ser igual aos datasets/labels

        12 labels, então 12 colunas.
        6 datasets, então 6 linhas.
        """
        valores = calculo_rendimentos_total()
        #dados = []
        dados = valores[1]
        return dados


class GraficoparticipacaoView(LoginRequiredMixin, TemplateView):
    template_name = 'relatorios/grafo.html'


class DadosJSONView(LoginRequiredMixin, BaseLineChartView):

    def get_labels(self):
        """Retorna 12 labels para a representação do x"""
        labels = [
            "JaneiroA",
            "FevereiroA",
            "MarçoA",
            "AbrilA",
            "MaioA",
            "JunhoA",
            "JulhoA",
            "AgostoA",
            "SetembroA",
            "OutubroA",
            "NovembroA",
            "DezembroA"
        ]
        return labels

    def get_providers(self):
        """Retorna os nomes dos datasets."""
        datasets = [
            "Janeiro1",
            "Fevereiro1",
            "Março1",
            "Abril",
            "Maio1",
            "Junho1",
            "Julho1",
            "Agosto1",
            "Setembro1",
            "Dezembro1"
        ]

        return datasets

    def get_data(self):
        """
        Retorna 6 datasets para plotar o gráfico.

        Cada linha representa um dataset.
        Cada coluna representa um label.

        A quantidade de dados precisa ser igual aos datasets/labels

        12 labels, então 12 colunas.
        6 datasets, então 6 linhas.
        """
        valores = calculo_rendimentos()[1]
        dados = []
        contador = 0
        q_valores = len(valores)
        for l in range(q_valores):
            for c in range(1):
                dado = valores[contador]
                contador += 1
                # dado = [
                #     randint(1, 100),  # jan 1 linha 1 coluna
                #     randint(1, 100),  # fev 1 linha 2 coluna
                #     randint(1, 100),  # mar 1 linha 3 coluna
                #     randint(1, 100),  # abr
                #     randint(1, 100),  # mai
                #     randint(1, 100),  # jun
                #     randint(1, 100),  # jul
                #     randint(1, 100),  # ago
                #     randint(1, 100),  # set
                #     randint(1, 100),  # out
                #     randint(1, 100),  # nov
                #     randint(1, 100)  # dez
                # ]
            dados.append(dado['valor__sum'])
            s = dados[0]
            s1 = dados
        return dados


class GraficoDemonstacaoView(LoginRequiredMixin, TemplateView):
    template_name = 'relatorios/grafoD.html'


class DadosD(LoginRequiredMixin, BaseLineChartView):

    def get_labels(self):
        """Retorna 12 labels para a representação do x"""
        labels = [
            "Janeiro",
            "Fevereiro",
            "Março",
            "Abril",
            "Maio",
            "Junho",
            "Julho",
            "Agosto",
            "Setembro",
            "Outubro",
            "Novembro",
            "Dezembro"
        ]

        return labels

    def get_providers(self):
        """Retorna os nomes dos datasets."""
        datasets = [
            "Programação para Leigos",
            "Algoritmos e Lógica de Programação",
            "Programação em C",
            "Programação em Java",
            "Programação em Python",
            "Banco de Dados"
        ]
        return datasets

    def get_data(self):
        """
        Retorna 6 datasets para plotar o gráfico.

        Cada linha representa um dataset.
        Cada coluna representa um label.

        A quantidade de dados precisa ser igual aos datasets/labels

        12 labels, então 12 colunas.
        6 datasets, então 6 linhas.
        """
        dados = []
        for l in range(6):
            for c in range(1):
                dado = [
                    randint(1, 100),  # jan 1 linha 1 coluna
                    randint(1, 100),  # fev 1 linha 2 coluna
                    randint(1, 100),  # mar 1 linha 3 coluna
                    randint(1, 100),  # abr
                    randint(1, 100),  # mai
                    randint(1, 100),  # jun
                    randint(1, 100),  # jul
                    randint(1, 100),  # ago
                    randint(1, 100),  # set
                    randint(1, 100),  # out
                    randint(1, 100),  # nov
                    randint(1, 100)   # dez
                ]
            dados.append(dado)
        return dados