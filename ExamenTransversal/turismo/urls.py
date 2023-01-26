from django.urls import path
from .views import inicio, sobrenosotros, galeria, formulario, calendario, apisismologia, crearviaje, mostrar, eliminar, modificar, crearcliente, mostrarcliente, eliminarcliente, modificarcliente


urlpatterns=[
    path('', inicio, name="inicio"),
    path('sobrenosotros/', sobrenosotros, name="sobrenosotros"),
    path('galeria/', galeria, name="galeria"),
    path('formulario/', formulario, name="formulario"),
    path('calendario/', calendario, name="calendario"),
    path('apisismologia/', apisismologia, name="apisismologia"),
    path('crearviaje/', crearviaje, name="crearviaje"),
    path('mostrar/', mostrar, name="mostrar"),
    path('eliminar/<id>', eliminar, name="eliminar"),
    path('modificar/<id>', modificar, name="modificar"),
    
    path('crearcliente/', crearcliente, name="crearcliente"),
    path('mostrarcliente/', mostrarcliente, name="mostrarcliente"),
    path('eliminarcliente/<id>', eliminarcliente, name="eliminarcliente"),
    path('modificarcliente/<id>', modificarcliente, name="modificarcliente"),
    
]

