from django.shortcuts import render, redirect
from django.shortcuts import redirect
from .forms import PizzaCreationForm, UsuarioForms, LoginForms
from .models import Usuario
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
            print(request.POST)
            campos = ['masa', 'salsa', 'tecnica', 'presentacion', 'maridaje']
            pizza = []
            ingredientes = []
            extras = []
            for campo in campos:
                pizza.append(form.cleaned_data[campo])
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
            print(filas)
            print(usuario.to_csv())
            print(usuario.to_csv() in filas)
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
            return redirect('Home')
        else:
            pass
    else:
        form = LoginForms() # aquí iniciamos un formulario vacío para que lo pinte cuando request.method sea distinto de POST
    return render(request, 'pizzeriawebapp/login.html', {'form':form})