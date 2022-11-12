from cgitb import html
from urllib import request
from django.shortcuts import render
from web.formularios.formularioPlatos import FormularioPlatos
from web.formularios.formularioEmpleados import FormularioEmpleados
from web.models import Platos, Empleados


# Create your views here.
#Todas las vistas son funciones de python
#Estas funciones son especiales porque son vistas, por lo tanto la incial será en mayúscula

def Home(request):
    return render(request, 'home.html')

def PlatosVista(request):
    #Esta vista va a utilizar un formulario de django, debo crear entonces un objeto de la clase formulario platos()
    formulario=FormularioPlatos()
    
    #creamos un  diccionario para enviar el formulario al html, es decir al template
    
    data = {
        'formulario': formulario
    }
    
    #Recibimos los datos del formulario
    if request.method=="POST":
        datosFormulario = FormularioPlatos(request.POST)
        if datosFormulario.is_valid():
            datosLimpios = datosFormulario.cleaned_data
            print(datosLimpios)
            #construir un diccionario de envio de datos hacia la bd
            platoNuevo = Platos(
                nombre = datosLimpios["nombre"],
                descripcion = datosLimpios["descripcion"],
                fotografia = datosLimpios["fotografia"],
                precio = datosLimpios["precio"],
                tipo = datosLimpios["tipo"]
            )
            #Lleva datos a la bd
            try:
                platoNuevo.save()
                print("Exito guardando...")
            except Exception as error:
                print("Error guardando", error)
    
    return render(request, 'menuplatos.html', data)

def EmpleadosVista(request):
    
    formulario = FormularioEmpleados()
    
    data = {
        'formulario': formulario
    }
        #Recibimos los datos del formulario
    if request.method=="POST":
        datosFormulario = FormularioEmpleados(request.POST)
        if datosFormulario.is_valid():
            datosLimpios = datosFormulario.cleaned_data
            print(datosLimpios)
            #construir un diccionario de envio de datos hacia la bd
            empleadoNuevo = Empleados(
                nombres = datosLimpios["nombres"],
                apellidos = datosLimpios["apellidos"],
                fotografia = datosLimpios["fotografia"],
                cargos = datosLimpios["cargos"],
                salario = datosLimpios["salario"],
                contacto = datosLimpios["contacto"]
            )
            #Lleva datos a la bd
            try:
                empleadoNuevo.save()
                print("Exito guardando...")
            except Exception as error:
                print("Error guardando", error)
                    
    return render(request, 'menuempleados.html', data)