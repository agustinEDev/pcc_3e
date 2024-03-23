from django.shortcuts import render
from .models import Pizza, Ingrediente

def index(request):
    """Página de inicio para pizzas."""
    return render(request, 'pizzas/index.html')

def pizzas(request):
    """Muestra todas las pizzas."""
    pizzas = Pizza.objects.order_by('date_added')
    context = {'pizzas': pizzas}
    return render(request, 'pizzas/pizzas.html', context)

def pizza(request, pizza_id):
    """Muestra una pizza y todos sus ingredientes."""
    pizza = Pizza.objects.get(id = pizza_id)
    ingredientes = pizza.ingrediente_set.order_by('-date_added')
    context = {'pizza': pizza, 'ingredientes': ingredientes}
    return render(request, 'pizzas/pizza.html', context)