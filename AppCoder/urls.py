from django.urls import path

from AppCoder.views import *

 
urlpatterns = [
    path("", inicio, name="inicio"),
    path('curso/', curso, name="curso"),
    path('profesores/', profesores, name="profesores"),
    path('estudiantes/', estudiantes,name="estudiantes"),
    path('entregables/', entregables,name="entregables"),

    path('curso-formulario',formulario_curso_api,name="curso-formulario"),
     
] 

