from django.shortcuts import render
from django.shortcuts import redirect
from rendimentos.views import Rendimentos
from ativos.views import Ativo
from django.db.models import Sum
# Create your views here.


def home(request):
    dado = {}
    sub_total = 0
    aux1 = Rendimentos.objects.aggregate(total=Sum('valor'))
    registros = Ativo.objects.all()
    for registro in registros:
        v = registro.valor_cota_adquirida
        c = registro.numero_cotas_adquiridas
        sub_total = sub_total + (v * c)
    # aux3 = Ativo.objects.aggregate(total_investido=Sum('valor_cota_adquirida'))
    # #quantidade_ativos = Ativo.objects.filcount()
    dado['total'] = aux1['total']
    dado['teste'] = round(sub_total, 2)
    return render(request, 'home.html', dado)


def logout(request):
    logout(request)
    return redirect('home')


def Relatorio(request):
    pass
