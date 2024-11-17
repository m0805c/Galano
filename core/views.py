from urllib import request
from django.shortcuts import render, redirect # type: ignore  
from django.shortcuts import render # type: ignore  
from django.http import HttpResponse # type: ignore
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm # type:ignore
from django.contrib.auth import login, authenticate # type: ignore
from django.contrib import messages # type: ignore #type : ignore
from .forms import RegistroForm
from core.models import User # type: ignore # type : ignore
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

def login_view(request):
    if request.user.is_authenticated:
        return redirect('dashboard')  # Si ya está autenticado, redirigir al dashboard

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            messages.success(request, 'Has iniciado sesión correctamente.')
            return redirect('dashboard')  # Redirigir al dashboard después de iniciar sesión
        else:
            messages.error(request, 'Usuario o contraseña incorrectos.')
    
    return render(request, 'core/iniciosesion.html')






def landing_page  (request):
    return render (request, 'core/landing_page.html' )


def landing_page (request):
    return render (request, 'core/landing_page.html')

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






##vista para el dash board 


from django.shortcuts import render # type: ignore # type : ignore 
from django.contrib.auth.decorators import login_required # type: ignore
from .models import Proyecto  

@login_required
def dashboard(request):

    proyectos = Proyecto.objects.filter(cliente__user=request.user)

    return render(request, 'dashboard.html', {'proyectos': proyectos})
