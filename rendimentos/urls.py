from django.urls import path
from .views import rendimentos
from .views import RegistrarRendimento
from .views import ListarRendimento
from .views import DetalharRendimento
from .views import AtualizarRendimento
from .views import ApagarRendimento
#from .views import relatorio_rendimentos

urlpatterns = [
    path('', rendimentos, name='rendimentos'),
    path('registrar/', RegistrarRendimento.as_view(), name='registrar_rendimento'),
    path('listar/', ListarRendimento.as_view(), name='listar_rendimento'),
    path('detalhar/<int:pk>', DetalharRendimento.as_view(), name='detalhar_rendimento'),
    path('atualizar/<int:pk>', AtualizarRendimento.as_view(), name='atualizar_rendimento'),
    path('apagar/<int:pk>', ApagarRendimento.as_view(), name='apagar_rendimento'),
   # path('relatorio/', relatorio_rendimentos, name='relatorio'),

]

