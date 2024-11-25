from django.contrib import admin # type: ignore
#aqui se esta registrando el modelo del usuario con clase predeterminada de administrador
from django.contrib.auth.admin import UserAdmin # type: ignore
from .models import User

class CustomUserAdmin(UserAdmin):
    model = User
    list_display = ['username', 'email', 'rol', 'is_staff', 'is_superuser', 'is_active']
    list_filter = ['is_staff', 'is_superuser', 'is_active']
    search_fields = ['username', 'email']
    ordering = ['username']

    # Configuración de los campos de creación
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2', 'rol', 'is_active', 'is_staff', 'is_superuser')}
        ),
    )
    fieldsets = (
        (None, {
            'fields': ('username', 'email', 'rol', 'password', 'is_active', 'is_staff', 'is_superuser')
        }),
        ('Fecha de Creación', {'fields': ('created_at', 'updated_at')}),
    )

#ahora hay que crear el modelo para desplegar las citas y los proyectos 

from django.contrib import admin # type: ignore
from .models import Cita  # Asegúrate de importar tu modelo de Cita

class CitaAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'fecha', 'estado', 'descripcion', 'created_at', 'updated_at')
    search_fields = ('usuario__username', 'descripcion')
    list_filter = ('estado',)

admin.site.register(Cita, CitaAdmin)

from .models import Proyecto  

class ProyectoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'descripcion', 'cliente', 'fecha_inicio', 'fecha_fin')
    search_fields = ('nombre', 'descripcion', 'cliente__username')  # Asumiendo que 'cliente' es un FK a User
    list_filter = ('estado',)

admin.site.register(Proyecto, ProyectoAdmin)


    