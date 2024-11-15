from django.shortcuts import render # type: ignore  
from django.http import HttpResponse # type: ignore

def landing_page  (request):
    return render (request, 'core/landing_page.html')

def quienes_somos (request):
    return render (request, 'core/quienes_somos.html')

def servicios (request):
    return render (request, 'core/servicios.html')

def iniciosesion (request):
    return render (request, 'core/iniciosesion.html')

