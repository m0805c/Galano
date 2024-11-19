#este archivo esta dedicado a los servicios que realiza la pagina

from .models import Proyecto
from .forms import ProyectoForm

def crear_proyecto_servicio(request, form_data):
#logica para crear un proyecto
    form = ProyectoForm(form_data)
    if form.is_valid():
        proyecto = form.save(commit=False)
        proyecto.usuario = request.user  # Asigna el usuario actual
        proyecto.save()
        return proyecto
    return None
