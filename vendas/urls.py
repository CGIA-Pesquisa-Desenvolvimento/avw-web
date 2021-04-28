from django.urls import path
from .views import vendas

urlpatterns = [
    path('', vendas, name='vendas')

]