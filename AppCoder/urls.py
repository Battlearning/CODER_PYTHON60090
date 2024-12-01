from django.urls import path

from AppCoder.views import *

 
urlpatterns = [
    path('pagina inicio/', inicio),
    path('curso/', curso),
    path('profesores/', profesores),
    path('estudiantes/', estudiantes),
    path('entregables/', entregables),
 
]
   