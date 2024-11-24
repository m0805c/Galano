from django.contrib import admin # type: ignore
#aqui se esta registrando el modelo del usuario con clase predeterminada de administrador
from django.contrib.auth.admin import UserAdmin # type: ignore
from .models import User

class CustomUserAdmin(UserAdmin):
    model = User
    list_display = ['username', 'email', 'rol', 'is_staff', 'is_superuser', 'is_active']
    list_filter =  ['is_staff', 'is_superuser', 'is_active']
    search_fields = ['username', 'email']

    #definir campos de formularios 

    add_fieldsets = (
        (None, {
            'classes':('wide',),
        'fields':('username', 'email', 'password1', 'password2', 'rol', 'is_active', 'is_staff', 'is_superuser')}
        ),
    )
    fieldsets = (
        (None,{
            'fields': ('username', 'email', 'rol', 'password', 'is_active', 'is_staff', 'is_superuser')
        }),
        ('Fecha de Creación', {'fields': ('created_at', 'updated_at')}),
    )

    admin.site.register(User, CustomUserAdmin) # type: ignore