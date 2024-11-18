#este es un archivo para poder cargar el formulario de registro 


from django import forms # type: ignore
from .models import User  # Importa el modelo User personalizado

class RegistroForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']  # Campos que deseas que tenga el formulario




##aqui cree el formulario para el modelo proyecto 

from django import forms  # type: ignore
from .models import Proyecto 
class ProyectoForm(forms.ModelForm):#crrar formularios basados en el modelo de los proyectos 
    class Meta:
        model = Proyecto        #datos que va a recibir 
        fields = ['nombre' , 'descripción' , 'cliente' , 'fecha_inicio' , 'fecha_fin' , 'estado']


        #widget para los campos de fecha para que se vuelvan selectores 

        'fecha_inicio': forms.DateInput(attrs={'type': 'date'}) # type: ignore
        'fecha_fin': forms.DateInput(attrs={'type': 'date'}) # type: ignore