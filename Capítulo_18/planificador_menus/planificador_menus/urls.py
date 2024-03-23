"""Define patrones de URL para planificador_menus."""

from django.urls import path
from . import views

app_name = 'planificador_menus'
urlpatterns = [
    # Página de inicio
    path('', views.index, name='index'),
]