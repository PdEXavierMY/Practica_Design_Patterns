from django.shortcuts import render, HttpResponse

# Create your views here.

def index(request):
    return render(request, 'pizzeriawebapp/index.html')

def login(request):
    return render(request, 'pizzeriawebapp/login.html')

def register(request):
    return render(request, 'pizzeriawebapp/registro.html')

def crear_pizza(request):
    return render(request, 'pizzeriawebapp/crea_tu_pizza.html')
