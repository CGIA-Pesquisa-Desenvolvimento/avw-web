from django.urls import path
from .views import fatos
from .views import RegistrarFato
from .views import ListarFato
from .views import DetalharFato
from .views import AtualizarFato
from .views import ApagarFato

urlpatterns = [
    path('', fatos, name='fatos'),
    path('registrar/', RegistrarFato.as_view(), name='registrar_fato'),
    path('listar/', ListarFato.as_view(), name='listar_fato'),
    path('detalhar/<int:pk>', DetalharFato.as_view(), name='detalhar_fato'),
    path('atualizar/<int:pk>', AtualizarFato.as_view(), name='atualizar_fato'),
    path('apagar/<int:pk>', ApagarFato.as_view(), name='apagar_fato'),
]
