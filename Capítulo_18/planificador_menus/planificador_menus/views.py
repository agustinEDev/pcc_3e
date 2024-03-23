from django.shortcuts import render

def index(request):
    """Página de inicio para planificador_menus."""
    return render(request, 'planificador_menus/index.html')
