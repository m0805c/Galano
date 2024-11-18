from typing import Self
from django.db import models  # type: ignore
from django.contrib.auth.models import User # type: ignore # type : ignore
# Create your models here.



class Rol(models.Model):        #modelo de el rol en el proyecto
    rolname = models.CharField(max_length=255, unique=True)
    descripcion = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.rolname 
    


class Contacto (models.Model):      #modelo del contacto
    email = models.EmailField(max_length=255)
    telefono = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.email
    

#######===========

from django.contrib.auth.models import AbstractBaseUser, BaseUserManager # type: ignore

class CustomUserManager(BaseUserManager):
    def create_user(self, username, email, password=None, rol=None):
        if not email:
            raise ValueError("El email debe ser proporcionado")
        email = self.normalize_email(email)
        user = self.model(username=username, email=email, rol=rol)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password=None, rol=None):
        user = self.create_user(username, email, password, rol)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

class User(AbstractBaseUser):
    username = models.CharField(max_length=255, unique=True)
    email = models.EmailField(unique=True)
    rol = models.ForeignKey('Rol', on_delete=models.SET_NULL, null=True, blank=True)  # No obligatorio
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # Campos de autenticación
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    objects = CustomUserManager()

    # Requerir estos campos para superusuario
    REQUIRED_FIELDS = ['email']  # no es necesario incluir rol
    USERNAME_FIELD = 'username'  # El campo que usaremos como nombre de usuario

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'



from django.contrib.auth import login # type: ignore
from django.shortcuts import render,  redirect # type: ignore
from django.contrib import messages # type: ignore
from .forms import RegistroForm

def registro(request):
    if request.method == "POST":
        form = RegistroForm(request.POST)
        if form.is_valid():
            # Crear usuario usando el formulario
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])  # Asegurarse de encriptar la contraseña
            user.save()

            # Hacer login automáticamente después de crear el usuario
            login(request, user)

            # Mostrar mensaje de éxito
            messages.success(request, 'Cuenta creada con éxito')

            # Redirigir al dashboard
            return redirect('dashboard')  # Redirige directamente al dashboard

    else:
        form = RegistroForm()

    return render (request, 'core/registro.html', {'form': form})






## a partir de aqui se definen los modelos para trabajar con clientes 



class Cliente(models.Model):
    nombre = models.CharField(max_length=255)
    direccion = models.CharField(max_length=255)
    telefono = models.CharField(max_length=20, null= True, blank = True)
    email = models.EmailField(max_length=255, unique= True)
    usuario = models.ForeignKey('User' , on_delete=models.CASCADE, related_name='clientes', null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.nombre
    
    class Meta: 
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'




class Proyecto(models.Model):
    nombre = models.CharField(max_length=255)
    descripcion = models.CharField(max_length=1000)
    cliente = models.ForeignKey('Cliente', on_delete=models.CASCADE, related_name='proyectos')
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField(null=True, blank=True)
    estado = models.CharField(max_length=50, choices=[
        ('activo', 'Activo'),
        ('finalizado', 'Finalizado'),
        ('pendiente', 'Pendiente'),
    ], default='activo')

    usuario = models.ForeignKey('User', on_delete=models.CASCADE, related_name='proyectos')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        
        ordering = ['-created_at']  # IMPORTANTE ordena la fecha de creación de manera descendente
        verbose_name = 'Proyecto'
        verbose_name_plural = 'Proyectos'

    def __str__(self):
        return self.nombre






