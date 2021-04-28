from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.urls import reverse_lazy

from django.contrib.auth.mixins import LoginRequiredMixin

from .models import FatosRelevantes


def fatos(request):
    return render(request, 'fatos/fatos.html')


class RegistrarFato(LoginRequiredMixin, CreateView):
    model = FatosRelevantes
    fields = ['ativo', 'data', 'fato', 'solucionado', 'solucao']
    template_name = 'fatos/registrar_fato.html'

    def get_success_url(self):
        return 'fatos/fato.html'


class ListarFato(LoginRequiredMixin, ListView):
    paginate_by = 10
    ordering = 'ativo'
    model = FatosRelevantes
    fields = ['ativo', 'data', 'fato', 'solucionado', 'solucao']
    template_name = 'fatos/listar_fatos.html'


class DetalharFato(LoginRequiredMixin, DetailView):
    model = FatosRelevantes
    template_name = 'fatos/detalhar_fato.html'


class AtualizarFato(LoginRequiredMixin, UpdateView):
    model = FatosRelevantes
    fields = ['ativo', 'data', 'fato', 'solucao', 'solucionado']
    template_name = 'fatos/registrar_fato.html'

    def get_success_url(self):
        return reverse_lazy('listar_fato')


class ApagarFato(LoginRequiredMixin, DeleteView):
    model = FatosRelevantes
    template_name = 'fatos/apagar_fato.html'

    def get_success_url(self):
        return reverse_lazy('listar_fato')
