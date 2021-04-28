from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import CreateView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.urls import reverse_lazy

from django.shortcuts import HttpResponse
import io
#from reportlab.pdfgen import canvas
import sqlite3

from .models import Rendimentos

from django.contrib.auth.mixins import LoginRequiredMixin

def rendimentos(request):
    return render(request, 'rendimentos/rendimentos.html')


class RegistrarRendimento(LoginRequiredMixin, CreateView):
    model = Rendimentos
    fields = ['ativo', 'data', 'valor', 'obs']
    template_name = 'rendimentos/registrar_rendimento.html'

    def get_success_url(self):
        return '/rendimentos/listar'


class AtualizarRendimento(LoginRequiredMixin, UpdateView):
    model = Rendimentos
    fields = ['ativo', 'data', 'valor', 'obs']
    template_name = 'rendimentos/atualizar_rendimento.html'

    def get_success_url(self):
        return reverse_lazy('listar_rendimento')


class DetalharRendimento(LoginRequiredMixin, DetailView):
    model = Rendimentos
    template_name = 'rendimentos/detalhar_rendimentos.html'


class ListarRendimento(LoginRequiredMixin, ListView):
    paginate_by = 10
    ordering = 'ativo'
    model = Rendimentos
    fields = ['ativo', 'data', 'valor']
    template_name = 'rendimentos/listar_rendimentos.html'


class ApagarRendimento(LoginRequiredMixin, DeleteView):
    model = Rendimentos
    template_name = 'rendimentos/apagar_rendimento.html'

    def get_success_url(self):
        return reverse_lazy('listar_rendimento')


# def sql_dividendos(self):
#     with connection.cursor() as c:
#         c.execute("SELECT a.nome_amigavel as 'ativo', sum(r.valor) as 'Total' FROM rendimentos_rendimentos as r, ativos_ativo as a WHERE r.ativo_id = a.id GROUP by a.nome_amigavel")
#         row = c.fetchall()


# def relatorio_rendimentos(request):
#     response = HttpResponse(content_type='application/pdf')
#     response['Content-Disposition'] = 'attachment; filename="fornecedores.pdf"'
#     # Create a file-like buffer to receive PDF data.
#     buffer = io.BytesIO()
#
#     # Create the PDF object, using the buffer as its "file."
#     p = canvas.Canvas(buffer)
#
#     # Draw things on the PDF. Here's where the PDF generation happens.
#     # See the ReportLab documentation for the full list of functionality.
#     p.drawString(250, 810, "Relatório de Rendimentos")
#     p.drawString(0, 800, '_' * 150)
#
#     total = 0.0
#     y = 780
#     conn = sqlite3.connect('db_orig.sqlite3')
#     c = conn.cursor()
#     c.execute("SELECT a.nome_amigavel as 'ativo', sum(r.valor) as 'Total' FROM rendimentos_rendimentos as r, ativos_ativo as a WHERE r.ativo_id = a.id GROUP by a.nome_amigavel")
#
#     rendimentos = c.fetchall()
#     str_ = 'Nome: %s - Valor R$%6.2f'
#     vlt = 'Total: R$ %.2f'
#     powered = 'Powered By CGIT'
#
#     for r in rendimentos:
#         p.drawString(10, y, str_ % (r[0], r[1]))
#         y -= 20
#         total += r[1]
#
#     p.drawString(0, 65, '_' * 150)
#     p.drawString(10, 50, vlt % total)
#     p.drawString(10, 35, powered)
#
#     # Close the PDF object cleanly, and we're done.
#     p.showPage()
#     p.save()
#
#     pdf = buffer.getvalue()
#     buffer.close()
#     response.write(pdf)
#     # FileResponse sets the Content-Disposition header so that browsers
#     # present the option to save the file.
#     # return FileResponse(buffer, as_attachment=True, filename='hello.pdf')
#     conn.close()
#     return response
