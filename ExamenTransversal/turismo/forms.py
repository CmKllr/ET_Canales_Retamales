from django import forms
from django.forms import ModelForm 
from django.forms import widgets #permite definir la configuración de los datos de entrada del form
from django.forms.models import ModelChoiceField
from django.forms.widgets import Widget
from .models import Viaje
from .models import Cliente

class ViajeForm(forms.ModelForm):
    
    class Meta: #permite configurar el form 
        model = Viaje 
        fields = ['codigo', 'destino', 'cantidadPasajero', 'distanciaRecorrer']
        labels = {
            'codigo': 'Codigo',
            'destino': 'Destino',
            'cantidadPasajero': 'CantidadPasajero',
            'distanciaRecorrer': 'DistanciaRecorrer',
        }
        widgets={
            'codigo': forms.TextInput(
                attrs = {
                    'class': 'form-control',
                    'placeholder': 'Digite un codigo',
                    'id': 'codigo'
                }
            ),
            'destino': forms.TextInput(
                attrs = {
                    'class': 'form-control',
                    'placeholder':'Ingrese el destino',
                    'id': 'destino'
                }
            ),
            'cantidadPasajero': forms.TextInput(
                attrs = {
                    'class' : 'form-control',
                    'placeholder': 'Ingrese cantidad',
                    'id': 'cantidadPasajero'
                }
            ),
            'distanciaRecorrer':forms.TextInput(
                attrs = {
                    'class': 'form-control',
                    'placeholder': 'Digite distancia a recorrer',
                    'id': 'distanciaRecorrer'
                }
            ),
        }




class ClienteForm(forms.ModelForm):
    
    class Meta: #permite configurar el form 
        model = Cliente 
        fields = ['rut', 'nombre', 'edad', 'correo', 'imagen']
        labels = {
            'rut': 'Rut',
            'nombre': 'Nombre',
            'edad': 'Edad',
            'correo': 'Correo',
            'imagen': 'Imagen',
        }
        widgets={
            'rut': forms.TextInput(
                attrs = {
                    'class': 'form-control',
                    'placeholder': 'Digite su rut',
                    'id': 'rut'
                }
            ),
            'nombre': forms.TextInput(
                attrs = {
                    'class': 'form-control',
                    'placeholder':'Ingrese su nombre',
                    'id': 'nombre'
                }
            ),
            'edad': forms.NumberInput(
                attrs = {
                    'class' : 'form-control',
                    'placeholder': 'Ingrese su edad',
                    'id': 'edad'
                }
            ),
            'correo':forms.EmailInput(
                attrs = {
                    'class': 'form-control',
                    'placeholder': 'Ingrese su Correo Electronico',
                    'id': 'correo'
                }
            ),
            'imagen': forms.FileInput(
                attrs={
                    'class': 'form-control',
                    'id': 'imagen',
                }
            )
        }