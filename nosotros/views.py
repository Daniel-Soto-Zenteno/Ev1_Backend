from django.shortcuts import render

# Create your views here.

def historia_y_guia(request):
    contexto = {
        'anio_fundacion': 2024,
        'valores': ['Calidad', 'Atención cercana', 'Perfumes replica'],
    }
    return render(request, 'nosotros/nosotros.html', contexto)