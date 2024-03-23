"""Define patrones URL para pizzas."""

from django.urls import path
from . import views

app_name = 'pizzas'
urlpatterns = [
    # Página de inicio
    path('', views.index, name='index'),
]