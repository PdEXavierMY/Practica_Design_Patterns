from django.shortcuts import render, redirect
from django.shortcuts import redirect
from .forms import PizzaCreationForm, UsuarioForms, LoginForms
from .models import Usuario, UsuarioLogin
from .csv_controller import CSV
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
        form = PizzaCreationForm(request.POST)
        if form.is_valid():
            campos = ['masa', 'salsa', 'tecnica', 'presentacion', 'maridaje']
            pizza = []
            ingredientes_generales = ['Queso', 'Pepperoni', 'Champiñones', 'Pimientos', 'Aceitunas', 'Pollo', 'Jamón', 'Anchoas', 'Atún', 'Tomate Cherry']
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
            if campos_usuario in filas == True:
                print("El usuario ya existe")
                return redirect('Login')
            else:
                CSV().guardar_usuarios(usuario)
                print("El usuario se ha registrado correctamente")
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
                usuario = form.cleaned_data['usuario'],
                contraseña = form.cleaned_data['contraseña'],
            )
            filas = CSV().leer_usuarios()
            if usuario.to_csv() in filas == True:
                print("El usuario ha iniciado sesión correctamente")
                return redirect('Home')
            else:
                print("El usuario no existe")
                return redirect('Registro')
        else:
            pass
    else:
        form = LoginForms() # aquí iniciamos un formulario vacío para que lo pinte cuando request.method sea distinto de POST
    return render(request, 'pizzeriawebapp/login.html', {'form':form})