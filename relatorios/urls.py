from django.urls import path

from .views import ReportLab
from .views import relatorios, Dados, GraficoRendimentoMesView, GraficoparticipacaoView, GraficoDemonstacaoView, DadosD, DadosJSONView


urlpatterns = [
    path('', relatorios, name='relatorios'),
  #  path('dados/', Dados.as_view(), name='dados'),
 #   path('grafico/', GraficoRendimentoMesView.as_view(), name='grafico'),
    path('grafico_demonstracao/', GraficoDemonstacaoView.as_view(), name='grafico_demonstracao'),
    path('dadosD/', DadosD.as_view(), name='dadosD'),
    path('grafico_participacao/', GraficoparticipacaoView.as_view(), name='grafico_participacao'),
    path('grafico/', GraficoRendimentoMesView.as_view(), name='grafico'),
    path('dados/', DadosJSONView.as_view(), name='dados'),


]
