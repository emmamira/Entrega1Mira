from django.shortcuts import render
from django.http import HttpResponse
from django.template import Template, Context
from django.template import loader
from AppEntrega1.models import *
from AppEntrega1.forms import LigaFormulario

# Create your views here.
def inicio(request):
    return render(request,"AppEntrega1/inicio.html")

def liga(request):
    return render(request,"AppEntrega1/liga.html")

def equipo(request):
    return render(request,"AppEntrega1/equipo.html")

def partido(request):
    return render(request,"AppEntrega1/partido.html")

def goleador(request):
    return render(request,"AppEntrega1/goleador.html")

def liga_formulario(request):
    if request.method == "POST":

        miFormulario = LigaFormulario(request.POST)
        print(miFormulario)

        if miFormulario.is_valid:

            informacion = miFormulario.cleaned_data
            
            r_nombre= informacion ['nombre']
            r_cantidadEquipos=informacion ['cantidadEquipos']

            liga = Liga(nombre=r_nombre, cantidadEquipos=r_cantidadEquipos)
            
            liga.save()
    
    else:

        miFormulario= LigaFormulario()
    
    return render (request, "AppEntrega1/liga_formulario.html", {"miFormulario": miFormulario})

def busquedaCantidadEquipos(request):

    return render(request,"AppEntrega1/busquedaCantidadEquipos.html")

def buscar(request):

    if request.GET["cantidadEquipos"]:

        cantidadEquipos=request.GET['cantidadEquipos']
        ligas= Liga.objects.filter (cantidadEquipos__icontains=cantidadEquipos)

        return render (request, "AppEntrega1/resultadoBusqueda.html", {"ligas":ligas, "cantidadEquipos":cantidadEquipos})

    else:

        respuesta = "No enviaste datos"
    
    return HttpResponse(respuesta)