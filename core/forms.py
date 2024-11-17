#este es un archivo para poder cargar el formulario de registro 


from django import forms # type: ignore
from .models import User  # Importa el modelo User personalizado

class RegistroForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']  # Campos que deseas que tenga el formulario
