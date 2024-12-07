from django.urls import path

from AppCoder.views import *

 
urlpatterns = [
    path('pagina-inicio/', inicio, name="inicio"),
    path('curso/', curso, name="curso"),
    path('profesores/', profesores, name="profesores"),
    path('estudiantes/', estudiantes,name="estudiantes"),
    path('entregables/', entregables,name="entregables"),
 
] 
   