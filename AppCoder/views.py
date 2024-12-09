from django.shortcuts import render, redirect
from .models import Curso
from django.http import HttpResponse
from .forms import CursoFormulario


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
    query = request.GET.get('q')
    if query:
        curso = Curso.objects.filter(nombre__icontains=query)
    else:
        curso = Curso.objects.all()
    return render(request, "AppCoder/curso.html", {"curso": curso, "query": query})

def profesores(request):
    return render(request, "AppCoder/profesores.html")

def estudiantes(request):
    return render(request, "AppCoder/estudiantes.html")

def entregables(request):
    return render(request, "AppCoder/entregables.html")


def formulario_curso(request):

    if request.method == "POST":
        curso = Curso(nombre=request.POST["curso"], camada=request.POST["comision"])
        print(curso)
        curso.save()
        return redirect("curso")
    else:
     return render(request, "AppCoder/forms/curso-formulario.html")


def formulario_curso_api(request):

     if request.method == "POST":
        curso_form = CursoFormulario(request.POST) 

        if curso_form. is_valid():
            informacion_limpia = curso_form.cleaned_data
            curso = Curso(nombre=informacion_limpia["nombre"], camada=informacion_limpia["camada"])
            curso.save()
            return redirect("curso")
     
     else:    
      curso_form = CursoFormulario()

     contexto = {"form": curso_form}


     return render(request, "AppCoder/forms/curso-formulario.html", contexto)
