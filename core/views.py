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
