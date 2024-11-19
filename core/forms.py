#este es un archivo para poder cargar el formulario de registro 


from django import forms # type: ignore
from .models import User  # Importa el modelo User personalizado

class RegistroForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']  # Campos que deseas que tenga el formulario




##aqui cree el formulario para el modelo proyecto 
from django import forms # type: ignore
from .models import Proyecto

class ProyectoForm(forms.ModelForm):
    class Meta:
        model = Proyecto
        fields = ['nombre', 'descripcion', 'fecha_inicio', 'fecha_fin', 'estado', 'Contacto']
        widgets = {
            'fecha_inicio': forms.DateInput(attrs={'type': 'date'}),
            'fecha_fin': forms.DateInput(attrs={'type': 'date'}),
        }
