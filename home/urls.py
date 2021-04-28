from django.urls import path

from .views import home
from .views import logout


urlpatterns = [
    path('', home, name='home'),
    path('logout/', logout, name='logout'),
]
