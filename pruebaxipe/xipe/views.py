from django.shortcuts import render

# Create your views here.
def inicio(request):
    return render(request, "inicio.html")

def apertura(request):
    return render(request, "apertura.html")

def merma(request):
    return render(request, "merma.html")

def cierre(request):
    return render(request, "cierre.html")