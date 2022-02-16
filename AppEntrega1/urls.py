from django.contrib import admin
from django.urls import path, include
from AppEntrega1 import views
from AppEntrega1.views import *

urlpatterns = [
    path('', views.inicio, name="Inicio"),
    path('ligas/', views.liga, name="Ligas"),
    path('equipos/', views.equipo, name="Equipos"),
    path('partidos/', views.partido, name="Partidos"),
    path('goleadores/', views.goleador, name="Goleadores"),
    path('liga_formulario/', liga_formulario, name="AppEntrega1LigaFormulario"),
    path('busquedaCantidadEquipos/', views.busquedaCantidadEquipos, name="busquedaCantidadEquipos"),
    path('buscar/', views.buscar),        
]