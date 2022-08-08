from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('lenguajes',views.lenguajes, name='lenguajes'),
    path('desarrollo',views.desarrollo, name='desarrollo'),
    path('librerias',views.librerias, name='librerias'),
    path('rutas',views.rutas, name='rutas'),
]