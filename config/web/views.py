from cgitb import html
from django.shortcuts import render

# Create your views here.
#Todas las vistas son funciones de python
#Estas funciones son especiales porque son vistas, por lo tanto la incial será en mayúscula

def Home(request):
    return render(request, 'home.html')