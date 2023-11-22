from django.shortcuts import render, redirect
from django.shortcuts import redirect
from django.contrib import messages
from .forms import PizzaCreationForm, UsuarioForms, LoginForms, MenuForms1, MenuForms2, MenuForms3, MenuForms4, MenuForms5
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

def menu1(request):
    return render(request, 'pizzeriawebapp/menu_individual.html')

def menu2(request):
    return render(request, 'pizzeriawebapp/menu_doble.html')

def menu3(request):
    return render(request, 'pizzeriawebapp/menu_triple.html')

def menu4(request):
    return render(request, 'pizzeriawebapp/menu_familiar.html')

def menu5(request):
    return render(request, 'pizzeriawebapp/menu_infantil.html')

def comprobacion(request):
    return render(request, 'pizzeriawebapp/comprobacion.html')

def crear_pizza(request):
    if request.method == 'POST':
        form = PizzaCreationForm(request.POST)
        if form.is_valid():
            # Lee el archivo CSV con pandas
            df = pd.read_csv('pizzas.csv', delimiter=';')  # Especifica el delimitador utilizado en tu archivo CSV
            nombres_pizza = list(df['Nombre'])
            campos = ['nombre', 'masa', 'salsa', 'ingredientes', 'tecnica', 'presentacion', 'extras']
            pizza = []
            for campo in campos:
                if form.cleaned_data['nombre'] in nombres_pizza:
                    messages.error(request, f"Los nombres deben ser únicos. Ese nombre ya existe")
                    return redirect('Crear Pizza')
                else:
                    if campo == 'ingredientes' or campo == 'extras':
                        # Convierte la lista a cadena y reemplaza las comas por barras inclinadas
                        lista_cambiada = '/'.join(map(str, form.cleaned_data[campo]))
                        
                        # Agrega la cadena modificada a la lista final
                        pizza.append([lista_cambiada])
                    else:
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

def comprobacion(request):
    # Lee los datos del archivo CSV
    filas = CSV().leer_pizzas()

    # Obtén los encabezados y la última fila
    encabezados = filas[0][0].split(';')[:-2]
    ultima_fila = filas[-1][0].split(';')[:-2]
    for elemento in ultima_fila:
        if '[' in elemento:
            ultima_fila[ultima_fila.index(elemento)] = elemento.strip("[]' ")
    print(ultima_fila)

    # Pasa los datos a la plantilla
    context = {
        'Encabezados': encabezados,
        'Pizza': ultima_fila,
    }

    return render(request, 'pizzeriawebapp/comprobacion.html', context)

def borrar_ultima_pizza(request):
    # Lógica para borrar la última línea del archivo CSV
    CSV().borrar_ultima_pizza()

    # Redirige a la página de inicio u otra página que desees después de borrar la línea
    return redirect('Crear Pizza')

def menu1(request):
    if request.method == 'POST':
        form = MenuForms1(request.POST)
        if form.is_valid():
           pass
    else:
        form = MenuForms1()

    return render(request, 'pizzeriawebapp/menu_individual.html', {'form': form})

def menu2(request):
    if request.method == 'POST':
        form = MenuForms2(request.POST)
        if form.is_valid():
           pass
    else:
        form = MenuForms2()

    return render(request, 'pizzeriawebapp/menu_doble.html', {'form': form})

def menu3(request):
    if request.method == 'POST':
        form = MenuForms3(request.POST)
        if form.is_valid():
           pass
    else:
        form = MenuForms3()

    return render(request, 'pizzeriawebapp/menu_triple.html', {'form': form})

def menu4(request):
    if request.method == 'POST':
        form = MenuForms4(request.POST)
        if form.is_valid():
           pass
    else:
        form = MenuForms4()

    return render(request, 'pizzeriawebapp/menu_familiar.html', {'form': form})

def menu5(request):
    if request.method == 'POST':
        form = MenuForms5(request.POST)
        if form.is_valid():
           pass
    else:
        form = MenuForms5()

    return render(request, 'pizzeriawebapp/menu_infantil.html', {'form': form})

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