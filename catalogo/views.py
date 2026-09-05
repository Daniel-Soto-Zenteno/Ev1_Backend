from django.shortcuts import render

# Create your views here.

def lista_perfumes(request):
    contexto = {
        'titulo': 'Catálogo de Fragancias',
        'hay_ofertas': True,
        'perfumes': [
            {'nombre': 'Perfume Dulce Noche', 'categoria': 'Femenino', 'precio': 15000},
            {'nombre': 'Citrus Fresh', 'categoria': 'Unisex', 'precio': 12000},
            {'nombre': 'Woody Intense', 'categoria': 'Masculino', 'precio': 18000},
        ]
    }
    return render(request, 'catalogo/lista.html', contexto)