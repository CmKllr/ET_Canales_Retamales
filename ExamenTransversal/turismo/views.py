from django.shortcuts import render, redirect
from .models import Viaje
from .models import Cliente
from .forms import ViajeForm
from .forms import ClienteForm

# Create your views here.
def inicio(request):
    return render(request, 'inicio.html')


def sobrenosotros(request):
    return render(request, 'sobrenosotros.html')


def galeria(request):
    return render(request, 'galeria.html')


def formulario(request):
    return render(request, 'formulario.html')


def calendario(request):
    return render(request, 'calendario.html')


def apisismologia(request):
    return render(request, 'apisismologia.html')






def crearviaje(request):
    if request.method=='POST': 
        viajeform = ViajeForm(request.POST)
        if viajeform.is_valid():
            viajeform.save()     #similar al insert
            return redirect('mostrar')
    else:
        viajeform=ViajeForm()
    return render(request, 'crearviaje.html', {'viajeform': viajeform})


def mostrar(request):
    #obtenemos todos los vehiculos almacenados en la clase
    viajes = Viaje.objects.all()
    #creamos un diccionario
    datos={
        'carros':viajes
    }
    #devolvemos a un template el diccionario y su contenido
    return render(request, 'mostrar.html', datos)


def eliminar(request, id):
    viaje = Viaje.objects.get(codigo=id)
    viaje.delete()
    return redirect('mostrar')


def modificar(request, id):
    viaje = Viaje.objects.get(codigo=id) #buscamos el objeto x patente = id
    datos ={
        'form': ViajeForm(instance=viaje) #instanciamos el obj. en un obj. de tipo formulario
    }
    #el siguiente bloque modifica el contenido del objeto almacenado
    if request.method=='POST':
        formulario = ViajeForm(data=request.POST, instance=viaje)
        if formulario.is_valid:
            formulario.save()
            return redirect('mostrar')
    
    return render(request, 'modificar.html', datos)













def crearcliente(request):
    if request.method=='POST': 
        clienteform = ClienteForm(request.POST, request.FILES)
        if clienteform.is_valid():
            clienteform.save()     #similar al insert
            return redirect('mostrarcliente')
    else:
        clienteform=ClienteForm()
    return render(request, 'crearcliente.html', {'clienteform': clienteform})


def mostrarcliente(request):
    #obtenemos todos los vehiculos almacenados en la clase
    clientes = Cliente.objects.all()
    #creamos un diccionario
    datos={
        'personas':clientes
    }
    #devolvemos a un template el diccionario y su contenido
    return render(request, 'mostrarcliente.html', datos)


def eliminarcliente(request, id):
    cliente = Cliente.objects.get(rut=id)
    cliente.delete()
    return redirect('mostrarcliente')


def modificarcliente(request, id):
    cliente = Cliente.objects.get(rut=id) #buscamos el objeto x patente = id
    datos ={
        'form': ClienteForm(instance=cliente) #instanciamos el obj. en un obj. de tipo formulario
    }
    #el siguiente bloque modifica el contenido del objeto almacenado
    if request.method=='POST':
        formulario = ClienteForm(data=request.POST, instance=cliente)
        if formulario.is_valid:
            formulario.save()
            return redirect('mostrarcliente')
    
    return render(request, 'modificarcliente.html', datos)

