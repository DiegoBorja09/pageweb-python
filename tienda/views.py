from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def inicio(request):
    return render(request,"paginas/inicio.html")
def lenguajes(request):
    return render(request, 'paginas/lenguajes.html')
def desarrollo(request):
    return render(request, 'paginas/desarrollo.html')
def librerias(request):
    return render(request, 'paginas/librerias.html')
def rutas(request):
    return render(request, 'paginas/rutas.html')