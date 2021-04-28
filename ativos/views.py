from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.urls import reverse_lazy
from django.shortcuts import HttpResponse

from django.template.loader import get_template
#import xhtml2pdf.pisa as pisa
from django.views.generic.base import View

import io
from django.http import FileResponse
#from reportlab.pdfgen import canvas

from .models import Ativo


def ativos(request):
    return render(request, 'ativos/ativos.html')


def logout(request):
    logout(request)
    return redirect('home')


class RegistrarAtivo(LoginRequiredMixin, CreateView):
    model = Ativo
    fields = ['codigo', 'nome_amigavel', 'tipo_ativo', 'gestor', 'data_ipo', 'valor_ipo', 'segmento', 'data_entrada'
              , 'valor_patrimonial_inicial', 'valor_mercado_inicial', 'valor_cota_adquirida', 'numero_cotas_adquiridas'
              , 'taxa_b3', 'taxa_liquidacao', 'emolumentos', 'motivo_compra', 'regulamento', 'obs']
    template_name = 'ativos/registrar_ativo.html'

    def get_success_url(self):
        return '/ativos/listar'


class AtualizarAtivo(LoginRequiredMixin, UpdateView):
    model = Ativo
    fields = ['codigo', 'nome_amigavel', 'tipo_ativo', 'gestor', 'data_ipo', 'valor_ipo', 'segmento', 'data_entrada'
              , 'valor_patrimonial_inicial', 'valor_mercado_inicial', 'valor_cota_adquirida', 'numero_cotas_adquiridas'
              , 'taxa_b3', 'taxa_liquidacao', 'emolumentos', 'motivo_compra', 'regulamento', 'obs']

    template_name = 'ativos/registrar_ativo.html'
    success_url = reverse_lazy('listar_ativo')

    def get_success_url(self):
        return reverse_lazy('listar_ativo')


class ListarAtivo(LoginRequiredMixin, ListView):
    model = Ativo
    paginate_by = 10
    ordering = 'nome_amigavel'
    fields = ['codigo', 'nome_amigavel', 'gestor', 'segmento', 'numero_cotas_adquiridas']
    template_name = 'ativos/listar_ativos.html'


class DetalharAtivo(LoginRequiredMixin, DetailView):
    model = Ativo

    template_name = 'ativos/detalhar_ativo.html'


class ApagarAtivo(LoginRequiredMixin, DeleteView):
    model = Ativo

    template_name = 'ativos/apagar_ativo.html'
   # success_url = reverse_lazy('listar_ativo')

    def get_success_url(self):
        return reverse_lazy('listar_ativo')


class Render:
    @staticmethod
    def render(path: str, params: dict, filename: str):
        template = get_template(path)
        html = template.render(params)
        response = io.BytesIO()
        pdf = pisa.pisaDocument(io.BytesIO(html.encode("UTF-8")), response)
        if not pdf.err:
            response = HttpResponse(response.getvalue(), content_type='application/pdf')
            response['Content-Disposition'] = 'attachment; filename=%s.pdf' % filename
            return response
        else:
            return HttpResponse("Error Rendering PDF", status=400)


class Pdf(LoginRequiredMixin, View):
    def get(self, request):
        x = 1
        params = {}
        ativos = Ativo.objects.all() #Ativo.objects.filter(tipo_ativo='F').values('nome_amigavel', 'numero_cotas_adquiridas')

        for ativo in ativos:
            params[x] = ativo
            x += 1
        x += 1
        params[x] = '------------------------------------------------------------------------------'
        # params = {
        #     'today': 'Variavel Today',
        #     'sales': 'Variavel sales',
        #     'request': request,
        # }
        return Render.render('ativos/teste.html', params, 'myfile')





