from django.shortcuts import render, redirect
from django.shortcuts import redirect
from django.contrib import messages
from .forms import PizzaCreationForm, UsuarioForms, LoginForms
from .models import Usuario, UsuarioLogin, PizzaBuilder, Director
from .csv_controller import CSV
import pandas as pd
# Create your views here.

def index(request):
    pizzas = CSV().leer_pizzas()
    return render(request, 'pizzeriawebapp/index.html', {'pizzas':pizzas})

def login(request):
    return render(request, 'pizzeriawebapp/login.html')

def register(request):
    return render(request, 'pizzeriawebapp/registro.html')

def crear_pizza(request):
    return render(request, 'pizzeriawebapp/crea_tu_pizza.html')

def comprobacion(request):
    return render(request, 'pizzeriawebapp/comprobacion.html')

def crear_pizza(request):
    if request.method == 'POST':
        form = PizzaCreationForm(request.POST)
        if form.is_valid():
            campos = ['nombre', 'masa', 'salsa', 'ingredientes', 'tecnica', 'presentacion', 'maridaje', 'extras']
            pizza = []
            for campo in campos:
                pizza.append(form.cleaned_data[campo])
            director = Director()
            builder = PizzaBuilder()
            director.builder = builder
            director.construir_pizza_completa(pizza)
            pizza_completa = builder.product
            id_usuario = None
            with open('logs.txt', 'r') as logs_file:
                id_usuario = logs_file.read()
            CSV().guardar_pizzas(pizza_completa, id_usuario)

            return redirect('Comprobacion')
        else:
            pass
    else:
        form = PizzaCreationForm() # aquí iniciamos un formulario vacío para que lo pinte cuando request.method sea distinto de POST
    return render(request, 'pizzeriawebapp/crea_tu_pizza.html', {'form':form})


def register(request):
    if request.method == 'POST':
        form = UsuarioForms(request.POST)
        if form.is_valid():
            usuario = Usuario(
                usuario=form.cleaned_data['usuario'],
                contraseña=form.cleaned_data['contraseña'],
                email=form.cleaned_data['email'],
                nombre=form.cleaned_data['nombre'],
                apellidos=form.cleaned_data['apellidos'],
            )
            
            campos_usuario = usuario.to_csv()
            filas = CSV().leer_usuarios()
            id_repetido = None

            for row in filas:
                if campos_usuario[0].split(';')[0:] == row[0].split(';')[1:]:
                    id_repetido = row[0]
                    break

            if id_repetido:
                messages.error(request, f"El usuario ya existe")
                return redirect('Login')
            
            else:
                # Obtener el último ID y determinar el próximo ID único
                if filas:
                    print(filas[-1][0].split(';')[0])
                    ultimo_id = int(filas[-1][0].split(';')[0])
                    nuevo_id = ultimo_id + 1
                else:
                    nuevo_id = 1

                # Agregar el nuevo ID a los campos del usuario
                campos_usuario[0] = str(nuevo_id) + ';' + campos_usuario[0]

                # Guardar el usuario en el CSV
                CSV().guardar_usuarios(campos_usuario)

                return redirect('Home')
        else:
            pass
    else:
        form = UsuarioForms()
        
    return render(request, 'pizzeriawebapp/registro.html', {'form': form})

def login(request):
    if request.method == 'POST':
        form = LoginForms(request.POST)
        if form.is_valid():
            usuario = UsuarioLogin(
                usuario=form.cleaned_data['usuario'],
                contraseña=form.cleaned_data['contraseña'],
            )
            filas = CSV().leer_usuarios()
            for fila in filas:
                if (
                    usuario.to_csv()[0].split(';')[0] == fila[0].split(';')[1]
                    and fila[0].split(';')[5] == usuario.to_csv()[0].split(';')[1]
                ):
                    # Obtener el ID del usuario recién creado
                    id_usuario = fila[0].split(';')[0]

                    # Escribir el ID en el archivo logs.txt
                    with open('logs.txt', 'w') as logs_file:
                        logs_file.write(id_usuario)
                    return redirect('Home')

            messages.error(request, "El usuario no existe o la contraseña es incorrecta")
            return redirect('Login')
    else:
        form = LoginForms()

    return render(request, 'pizzeriawebapp/login.html', {'form': form})