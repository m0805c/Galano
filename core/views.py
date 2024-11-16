from django.shortcuts import render # type: ignore  
from django.http import HttpResponse # type: ignore

def landing_page  (request):
    return render (request, 'core/landing_page.html' )

def quienes_somos (request):
    return render (request, 'core/quienes_somos.html')

def iniciosesion (request):
    return render (request, 'core/iniciosesion.html')

def tecnologias (request):
    return render (request, 'core/tecnologias.html')

def constructora (request):
    return render (request, 'core/constructora.html')

def seguridad (request):
    return render (request, 'core/seguridad.html')