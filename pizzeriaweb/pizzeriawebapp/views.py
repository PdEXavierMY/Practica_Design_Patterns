from django.shortcuts import render, redirect
from django.shortcuts import redirect
from django.contrib import messages
from .forms import PizzaCreationForm, UsuarioForms, LoginForms
from .models import Usuario, UsuarioLogin, PizzaBuilder, Director
from .csv_controller import CSV
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

def crear_pizza(request):
    if request.method == 'POST':
        form = PizzaCreationForm(request.POST)
        if form.is_valid():
            campos = ['masa', 'salsa', 'tecnica', 'presentacion', 'maridaje']
            pizza = []
            ingredientes_generales = ['Queso', 'Pepperoni', 'Champiñones', 'Pimientos', 'Aceitunas', 'Pollo', 'Jamón', 'Anchoas', 'Atún', 'Tomate Cherry', 'Mozzarrella', 'Albahaca', 'Piña', 'Cebolla', 'Salchichas']
            extras_generales = ['Salsa_Picante', 'Ajo_Asado', 'Queso_Azul', 'Aceite_de_Trufa', 'Huevo', 'Piña', 'Chiles_Rojos', 'Nueces', 'Jalapeños', 'Tomate_Secado_al_Sol']
            ingredientes = []
            extras = []
            for campo in campos:
                pizza.append(form.cleaned_data[campo])
            for ingrediente in ingredientes_generales:
                if ingrediente in request.POST:
                    ingredientes.append(ingrediente)
            for extra in extras_generales:
                if extra in request.POST:
                    extras.append(extra)
            pizza.append(ingredientes); pizza.append(extras)
            director = Director()
            builder = PizzaBuilder()
            director.builder = builder
            director.construir_pizza_completa(pizza)
            pizza_completa = builder.product
            CSV().guardar_pizzas(pizza_completa)

            return redirect('Home')
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
                usuario = form.cleaned_data['usuario'],
                contraseña = form.cleaned_data['contraseña'],
                email = form.cleaned_data['email'],
                nombre = form.cleaned_data['nombre'],
                apellidos = form.cleaned_data['apellidos'],
            )
            filas = CSV().leer_usuarios()
            campos_usuario = usuario.to_csv()
            if campos_usuario in filas:
                messages.error(request, "El usuario ya existe")
                return redirect('Login')
            else:
                CSV().guardar_usuarios(usuario)
                return redirect('Home')
        else:
            pass
    else:
        form = UsuarioForms() # aquí iniciamos un formulario vacío para que lo pinte cuando request.method sea distinto de POST
    return render(request, 'pizzeriawebapp/registro.html', {'form':form})

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
                    usuario.to_csv()[0].split(';')[0] == fila[0].split(';')[0]
                    and fila[0].split(';')[4] == usuario.to_csv()[0].split(';')[1]
                ):
                    messages.success(request, "El usuario ha iniciado sesión correctamente")
                    return redirect('Home')

            messages.error(request, "El usuario no existe o la contraseña es incorrecta")
            return redirect('Login')
    else:
        form = LoginForms()

    return render(request, 'pizzeriawebapp/login.html', {'form': form})