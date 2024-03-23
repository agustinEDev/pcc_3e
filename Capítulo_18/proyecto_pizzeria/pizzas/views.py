from django.shortcuts import render

def index(request):
    """Página de inicio para pizzas."""
    return render(request, 'pizzas/index.html')