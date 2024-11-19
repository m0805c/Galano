from urllib import request
from django.shortcuts import render, redirect # type: ignore  
from django.shortcuts import render # type: ignore  
from django.http import HttpResponse # type: ignore
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm # type:ignore
from django.contrib.auth import login, authenticate # type: ignore
from django.contrib import messages # type: ignore #type : ignore
from .forms import RegistroForm
from core.models import User # type: ignore # type : ignore
from django.contrib.auth.decorators import login_required  # type: ignore
#vista para registrar nuevos usuarios

def registro(request):
    if request.method == "POST":
        form = RegistroForm(request.POST) # type: ignore
        if form.is_valid():
            # Crear usuario usando el modelo personalizado
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])  # Asegúrate de encriptar la contraseña
            user.save()
            messages.success(request, 'Cuenta creada con éxito')
            return redirect('iniciosesion')  # Redirigir al login o dashboard

    else:
        form = RegistroForm() # type: ignore

    return render(request, 'core/registro.html', {'form': form})


from django.shortcuts import render, redirect # type: ignore
from django.contrib.auth import authenticate, login # type: ignore
from django.contrib import messages # type: ignore








from django.contrib.auth.forms import AuthenticationForm  # type: ignore
from django.shortcuts import render, redirect  # type: ignore
from django.contrib import messages  # type: ignore
from django.contrib.auth import login  # type: ignore # Asegúrate de importar 'login'

def iniciosesion(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()  # Recupera al usuario autenticado
            login(request, user)  # Inicia la sesión del usuario
            return redirect('dashboard')  # Redirige al dashboard
        else:
            messages.error(request, 'Usuario o contraseña incorrectos.')  # Si hay error
    else:
        form = AuthenticationForm()  # Si es GET, mostramos el formulario vacío

    return render(request, 'core/iniciosesion.html', {'form': form})





def landing_page  (request):
    return render (request, 'core/landing_page.html' )


def landing_page (request):
    return render (request, 'core/landing_page.html')

def quienes_somos (request):
    return render (request, 'core/quienes_somos.html')


def tecnologias (request):
    return render (request, 'core/tecnologias.html')

def constructora (request):
    return render (request, 'core/constructora.html')

def seguridad (request):
    return render (request, 'core/seguridad.html')






##vista para el dash board 


from django.shortcuts import render # type: ignore # type : ignore 
from django.contrib.auth.decorators import login_required # type: ignore
from .models import Cliente, Proyecto  

@login_required
def dashboard(request):
    try:
        # Obtenemos el cliente asociado al usuario logueado
        cliente = Cliente.objects.get(usuario=request.user)

        # Filtramos los proyectos que están relacionados con ese cliente
        proyectos = Proyecto.objects.filter(cliente=cliente)
    except Cliente.DoesNotExist:
        # Si no existe el cliente, asignamos una lista vacía
        proyectos = []

    return render(request, 'core/dashboard.html', {'proyectos': proyectos})




## vista para cuando se quiere crear proyecto: inicio de sesion - crear proyecto 

from .forms import ProyectoForm # type: ignore
from django.contrib.auth.decorators import login_required # type: ignore # type : ignore
from core.services import crear_proyecto_servicio
from django.contrib.auth.decorators import login_required # type: ignore
from django.shortcuts import render, redirect # type: ignore
from django.contrib import messages # type: ignore
from .forms import ProyectoForm
from .models import Proyecto, Cliente

@login_required
def crear_proyecto(request):
    """
    Vista para crear un nuevo proyecto con los datos del formulario.
    """
    if request.method == 'POST':
        form = ProyectoForm(request.POST)

        # Validamos el formulario
        if form.is_valid():
            # Intentamos obtener el cliente asociado al usuario logueado
            cliente = Cliente.objects.filter(usuario=request.user).first()  # Usamos `filter()` y `first()` para evitar excepción

            if not cliente:
                # Si el usuario no tiene un cliente, lo creamos
                cliente = Cliente.objects.create(
                    nombre=request.user.username,  # O algún valor por defecto
                    direccion='Dirección por definir',  # Puedes ajustar esto
                    telefono='0000000000',  # Valor por defecto
                    email=request.user.email,  # Asociar el email del usuario al cliente
                    usuario=request.user,  # Asocia el usuario al cliente
                )

            # Ahora asociamos el cliente y el usuario al proyecto
            proyecto = form.save(commit=False)  # No guardamos aún
            proyecto.cliente = cliente  # Asociamos el cliente
            proyecto.usuario = request.user  # Asociamos el usuario logueado
            proyecto.save()  # Guardamos el proyecto

            # Mensaje de éxito
            messages.success(request, 'Proyecto creado con éxito')

            # Redirigimos al dashboard (o donde desees)
            return redirect('dashboard')
        else:
            # Si no es válido, mostramos los errores en el formulario
            messages.error(request, 'Hubo un error al crear el proyecto. Intenta nuevamente.')
    else:
        # Si es una solicitud GET, creamos un formulario vacío
        form = ProyectoForm()

    # Renderizamos el formulario para crear el proyecto
    return render(request, 'core/crear_proyecto.html', {'form': form})



##vista para eliminar un proyecto 

from django.shortcuts import render, get_object_or_404, redirect # type: ignore
from django.contrib import messages # type: ignore
from django.contrib.auth.decorators import login_required # type: ignore
from .models import Proyecto

@login_required
def eliminar_proyecto(request, proyecto_id):
    """
    Vista para que el cliente pueda eliminar un proyecto.
    Verifica que el proyecto pertenece al cliente logueado antes de eliminarlo.
    """
    # Obtener el proyecto (con una validación de que pertenece al usuario logueado)
    proyecto = get_object_or_404(Proyecto, id=proyecto_id, cliente__usuario=request.user)

    # El proyecto debe estar asociado al usuario logueado
    if proyecto.cliente.usuario == request.user:
        # Eliminar el proyecto
        proyecto.delete()
        messages.success(request, 'Proyecto eliminado correctamente.')
    else:
        # Si el proyecto no pertenece al usuario, mostramos un error
        messages.error(request, 'No tienes permiso para eliminar este proyecto.')

    # Redirigir a la lista de proyectos del cliente o a otra página
    return redirect('dashboard')  # O cualquier otra vista a la que quieras redirigir
