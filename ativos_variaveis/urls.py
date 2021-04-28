"""ativos_variaveis URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from django.urls import include
from home import urls as home_urls
from ativos import urls as ativos_urls
from rendimentos import urls as rendimentos_urls
from fatos import urls as fatos_urls
from vendas import urls as vendas_urls
from relatorios import urls as relatorios_urls


urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('', include(home_urls)),
    path('ativos/', include(ativos_urls)),
    path('rendimentos/', include(rendimentos_urls)),
    path('fatos/', include(fatos_urls)),
    path('vendas/', include(vendas_urls)),
    path('relatorios/', include(relatorios_urls)),
    path('accounts/', include('django.contrib.auth.urls')),
]

admin.AdminSite.site_header = 'Sistema de Controle de Ativos Variaveis'
admin.AdminSite.site_title = 'Powered By CGIA'
admin.AdminSite.index_title = 'SCAV'
