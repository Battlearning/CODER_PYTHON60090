from django.shortcuts import render
from .models import Curso
from django.http import HttpResponse


# Create your views here.

# CLASE 18
# def curso(request):
#     curso = Curso(nombre='Python', camada=2022)
#     curso.save()
    
#     return HttpResponse(f'Curso creado con id {curso.id}, nombre {curso.nombre} y camada {curso.camada}')



#CLASE 19 -------------------------------------------------------------

def inicio(request):
      return render(request, "AppCoder/index.html")

def curso(request):
    curso = Curso.objects.all()
    print(curso)
    return render(request, "AppCoder/curso.html", {"curso": curso})

def profesores(request):
    return render(request, "AppCoder/profesores.html")

def estudiantes(request):
    return render(request, "AppCoder/estudiantes.html")

def entregables(request):
    return render(request, "AppCoder/entregables.html")


 