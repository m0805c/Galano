#este es un archivo creado manualmente por el administrador.
#en este archivo se configuran todas las vistas de la aplicación "core".
#estas urls se van a conectar con el urls.py del proyecto global



from django.urls import path # type: ignore
from . import views

urlpatterns = [
    path ('' , views.landing_page, name='landing_page'),
    path ('quienes_somos/' , views.quienes_somos, name ='quienes_somos'),
    path ('iniciosesion/' , views.iniciosesion, name='iniciosesion'),
    path ('tecnologias/' , views.tecnologias, name='tecnologias'),
    path ('constructora/', views.constructora, name='constructora'),
    path ('seguridad/', views.seguridad, name='seguridad'),
]