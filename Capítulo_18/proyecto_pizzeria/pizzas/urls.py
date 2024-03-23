"""Define patrones URL para pizzas."""

from django.urls import path
from . import views

app_name = 'pizzas'
urlpatterns = [
    # Página de inicio
    path('', views.index, name='index'),
    # Página que muestra todas las pizzas
    path('pizzas/', views.pizzas, name='pizzas'),
    # Página de detalles para una pizza individual
    path('pizzas/<int:pizza_id>/', views.pizza, name='pizza'),
]