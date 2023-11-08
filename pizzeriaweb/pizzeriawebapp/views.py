from django.shortcuts import render, 
from django import forms
from .models import Pizza

# Create your views here.

def index(request):
    return render(request, 'pizzeriawebapp/index.html')

def login(request):
    return render(request, 'pizzeriawebapp/login.html')

def register(request):
    return render(request, 'pizzeriawebapp/registro.html')

def crear_pizza(request):
    return render(request, 'pizzeriawebapp/crea_tu_pizza.html')

def crear_pizza(request):
    if request.method == 'POST':
        form = PizzaForm(request.POST)
        if form.is_valid():
            # Guarda la pizza u otros pasos que desees realizar
            pizza = form.save()
    else:
        form = PizzaForm()
    return render(request, 'tu_template.html', {'form': form})
