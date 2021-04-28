from django.urls import path

from .views import ativos
from .views import RegistrarAtivo
from .views import ListarAtivo
from .views import DetalharAtivo
from .views import AtualizarAtivo
from .views import ApagarAtivo
from .views import Pdf

urlpatterns = [
    path('', ativos, name='ativos'),
    path('registrar/', RegistrarAtivo.as_view(), name='registrar_ativo'),
    path('listar/', ListarAtivo.as_view(), name='listar_ativo'),
    path('detalhar/<int:pk>', DetalharAtivo.as_view(), name='detalhar_ativo'),
    path('atualizar/<int:pk>', AtualizarAtivo.as_view(), name='atualizar_ativo'),
    path('apagar/<int:pk>', ApagarAtivo.as_view(), name='apagar_ativo'),
    path('teste_html/', Pdf.as_view(), name='teste_html'),

]

