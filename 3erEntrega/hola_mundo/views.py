from django.shortcuts import render
from django.http import HttpResponse
from hola_mundo.models import *
from hola_mundo.forms import PersonaForm, BuscarPersonasForm
from django.views.generic import ListView


def mostrar_personas(request):
    
    personas = Persona.objects.all()
    total_personas = len(personas)
    context = {
        "personas": personas, 
        "total_personas":total_personas,
        "form": PersonaForm(),
    }
    return render(request, "hola_mundo/personas.html", context)


def crear_persona(request):

    f = PersonaForm(request.POST)
    context = {
        "form": f
    } 
    if f.is_valid():
        Persona(nombre=f.data["nombre"], apellido=f.data["apellido"], fecha_nacimiento=f.data["fecha_nacimiento"]).save()
        context['form'] = PersonaForm()

    context["personas"] = Persona.objects.all()
    context["total_personas"] = len(Persona.objects.all())
         
    return render(request, "hola_mundo/personas.html", context)


def mostrar_Productos(request):
        Productos = Producto.objects.all()
        return render(request, "hola_mundo/productos.html", {"Productos": Producto})

def mostrar_mis_ventas(request):
        ProductoVenta = Venta.objects.all()
        return render(request, "hola_mundo/ventas.html", {"ProductoVenta": Venta})

class BuscarPersonas(ListView):
    model = Persona
    context_object_name = "personas"

    def get_queryset(self):
        f = BuscarPersonasForm(self.request.GET)
        if f.is_valid():
           return Persona.objects.filter(nombre__icontains=f.data["criterio_nombre"]).all()
        return Persona.objects.none()
    
   
    