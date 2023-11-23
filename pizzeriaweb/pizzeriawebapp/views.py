from django.shortcuts import render, redirect
from django.shortcuts import redirect
from django.contrib import messages
from .forms import PizzaCreationForm, UsuarioForms, LoginForms, MenuForms1, MenuForms2, MenuForms3, MenuForms4, MenuForms5
from .models import Usuario, UsuarioLogin, PizzaBuilder, Director, PizzaMenu, Entrante, Postre, Maridaje, Component, Menu
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

def comprobacion_menu(request):
    return render(request, 'pizzeriawebapp/comprobacion_menu.html')

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
            tipo_menu = 'Individual'
            precios = CSV().leer_precios()
            df = pd.read_csv('pizzas.csv', delimiter=';')  # Especifica el delimitador utilizado en tu archivo CSV
            entrante_1 = Entrante(
                nombre=form.cleaned_data['Entrante_1'],
                precio=float(precios[form.cleaned_data['Entrante_1']])
            )
            pizza_1 = PizzaMenu(
                nombre=form.cleaned_data['Pizza_1'],
                precio=df.loc[df['Nombre'] == form.cleaned_data['Pizza_1'], 'Precio'].values[0]
            )
            maridaje_1 = Maridaje(
                nombre=form.cleaned_data['Maridaje_1'],
                precio=float(precios[form.cleaned_data['Maridaje_1']])
            )
            postre_1 = Postre(
                nombre=form.cleaned_data['Postre_1'],
                precio=float(precios[form.cleaned_data['Postre_1']])
            )

            menu = Menu(
                tipo=tipo_menu
            )
            menu.add(entrante_1); menu.add(pizza_1); menu.add(maridaje_1); menu.add(postre_1)
            id_usuario = None
            with open('logs.txt', 'r') as logs_file:
                id_usuario = logs_file.read()
            menus = CSV().leer_menus()
            if menus:
                #si solo hay un elemento en la lista, el código es 1
                if len(menus) == 1:
                    codigo = 1
                else:
                    #si hay más de un elemento, el código es el último código + 1
                    ultimo_codigo = int(menus[-1][0].split(';')[-1])
                    codigo = ultimo_codigo + 1
            CSV().guardar_menus(menu, id_usuario, codigo)
            return redirect('Comprobacion Menu')

    else:
        form = MenuForms1()

    return render(request, 'pizzeriawebapp/menu_individual.html', {'form': form})

def menu2(request):
    if request.method == 'POST':
        form = MenuForms2(request.POST)
        if form.is_valid():
            tipo_menu = 'Doble'
            precios = CSV().leer_precios()
            df = pd.read_csv('pizzas.csv', delimiter=';')  # Especifica el delimitador utilizado en tu archivo CSV
            entrante_1 = Entrante(
                nombre=form.cleaned_data['Entrante_1'],
                precio=float(precios[form.cleaned_data['Entrante_1']])
            )
            entrante_2 = Entrante(
                nombre=form.cleaned_data['Entrante_2'],
                precio=float(precios[form.cleaned_data['Entrante_2']])
            )
            pizza_1 = PizzaMenu(
                nombre=form.cleaned_data['Pizza_1'],
                precio=df.loc[df['Nombre'] == form.cleaned_data['Pizza_1'], 'Precio'].values[0]
            )
            pizza_2 = PizzaMenu(
                nombre=form.cleaned_data['Pizza_2'],
                precio=df.loc[df['Nombre'] == form.cleaned_data['Pizza_2'], 'Precio'].values[0]
            )
            maridaje_1 = Maridaje(
                nombre=form.cleaned_data['Maridaje_1'],
                precio=float(precios[form.cleaned_data['Maridaje_1']])
            )
            maridaje_2 = Maridaje(
                nombre=form.cleaned_data['Maridaje_2'],
                precio=float(precios[form.cleaned_data['Maridaje_2']])
            )
            postre_1 = Postre(
                nombre=form.cleaned_data['Postre_1'],
                precio=float(precios[form.cleaned_data['Postre_1']])
            )
            postre_2 = Postre(
                nombre=form.cleaned_data['Postre_2'],
                precio=float(precios[form.cleaned_data['Postre_2']])
            )

            menu = Menu(
                tipo=tipo_menu
            )
            menu.add(entrante_1); menu.add(entrante_2); menu.add(pizza_1); menu.add(pizza_2); menu.add(maridaje_1); menu.add(maridaje_2); menu.add(postre_1); menu.add(postre_2)
            id_usuario = None
            with open('logs.txt', 'r') as logs_file:
                id_usuario = logs_file.read()
            menus = CSV().leer_menus()
            if menus:
                #si solo hay un elemento en la lista, el código es 1
                if len(menus) == 1:
                    codigo = 1
                else:
                    #si hay más de un elemento, el código es el último código + 1
                    ultimo_codigo = int(menus[-1][0].split(';')[-1])
                    codigo = ultimo_codigo + 1
            CSV().guardar_menus(menu, id_usuario, codigo)
            return redirect('Comprobacion Menu')
    else:
        form = MenuForms2()

    return render(request, 'pizzeriawebapp/menu_doble.html', {'form': form})

def menu3(request):
    if request.method == 'POST':
        form = MenuForms3(request.POST)
        if form.is_valid():
            tipo_menu = 'Triple'
            precios = CSV().leer_precios()
            df = pd.read_csv('pizzas.csv', delimiter=';')  # Especifica el delimitador utilizado en tu archivo CSV
            entrante_1 = Entrante(
                nombre=form.cleaned_data['Entrante_1'],
                precio=float(precios[form.cleaned_data['Entrante_1']])
            )
            entrante_2 = Entrante(
                nombre=form.cleaned_data['Entrante_2'],
                precio=float(precios[form.cleaned_data['Entrante_2']])
            )
            entrante_3 = Entrante(
                nombre=form.cleaned_data['Entrante_3'],
                precio=float(precios[form.cleaned_data['Entrante_3']])
            )
            pizza_1 = PizzaMenu(
                nombre=form.cleaned_data['Pizza_1'],
                precio=df.loc[df['Nombre'] == form.cleaned_data['Pizza_1'], 'Precio'].values[0]
            )
            pizza_2 = PizzaMenu(
                nombre=form.cleaned_data['Pizza_2'],
                precio=df.loc[df['Nombre'] == form.cleaned_data['Pizza_2'], 'Precio'].values[0]
            )
            pizza_3 = PizzaMenu(
                nombre=form.cleaned_data['Pizza_3'],
                precio=df.loc[df['Nombre'] == form.cleaned_data['Pizza_3'], 'Precio'].values[0]
            )
            maridaje_1 = Maridaje(
                nombre=form.cleaned_data['Maridaje_1'],
                precio=float(precios[form.cleaned_data['Maridaje_1']])
            )
            maridaje_2 = Maridaje(
                nombre=form.cleaned_data['Maridaje_2'],
                precio=float(precios[form.cleaned_data['Maridaje_2']])
            )
            maridaje_3 = Maridaje(
                nombre=form.cleaned_data['Maridaje_3'],
                precio=float(precios[form.cleaned_data['Maridaje_3']])
            )
            postre_1 = Postre(
                nombre=form.cleaned_data['Postre_1'],
                precio=float(precios[form.cleaned_data['Postre_1']])
            )
            postre_2 = Postre(
                nombre=form.cleaned_data['Postre_2'],
                precio=float(precios[form.cleaned_data['Postre_2']])
            )
            postre_3 = Postre(
                nombre=form.cleaned_data['Postre_3'],
                precio=float(precios[form.cleaned_data['Postre_3']])
            )

            menu = Menu(
                tipo=tipo_menu
            )
            menu.add(entrante_1); menu.add(entrante_2); menu.add(entrante_3); menu.add(pizza_1); menu.add(pizza_2); menu.add(pizza_3); menu.add(maridaje_1); menu.add(maridaje_2); menu.add(maridaje_3); menu.add(postre_1); menu.add(postre_2); menu.add(postre_3)
            id_usuario = None
            with open('logs.txt', 'r') as logs_file:
                id_usuario = logs_file.read()
            menus = CSV().leer_menus()
            if menus:
                #si solo hay un elemento en la lista, el código es 1
                if len(menus) == 1:
                    codigo = 1
                else:
                    #si hay más de un elemento, el código es el último código + 1
                    ultimo_codigo = int(menus[-1][0].split(';')[-1])
                    codigo = ultimo_codigo + 1
            CSV().guardar_menus(menu, id_usuario, codigo)
            return redirect('Comprobacion Menu')
    else:
        form = MenuForms3()

    return render(request, 'pizzeriawebapp/menu_triple.html', {'form': form})

def menu4(request):
    if request.method == 'POST':
        form = MenuForms4(request.POST)
        if form.is_valid():
            tipo_menu = 'Familiar'
            precios = CSV().leer_precios()
            df = pd.read_csv('pizzas.csv', delimiter=';')  # Especifica el delimitador utilizado en tu archivo CSV
            entrante_1 = Entrante(
                nombre=form.cleaned_data['Entrante_1'],
                precio=float(precios[form.cleaned_data['Entrante_1']])
            )
            entrante_2 = Entrante(
                nombre=form.cleaned_data['Entrante_2'],
                precio=float(precios[form.cleaned_data['Entrante_2']])
            )
            entrante_3 = Entrante(
                nombre=form.cleaned_data['Entrante_3'],
                precio=float(precios[form.cleaned_data['Entrante_3']])
            )
            entrante_4 = Entrante(
                nombre=form.cleaned_data['Entrante_4'],
                precio=float(precios[form.cleaned_data['Entrante_4']])
            )
            pizza_1 = PizzaMenu(
                nombre=form.cleaned_data['Pizza_1'],
                precio=df.loc[df['Nombre'] == form.cleaned_data['Pizza_1'], 'Precio'].values[0]
            )
            pizza_2 = PizzaMenu(
                nombre=form.cleaned_data['Pizza_2'],
                precio=df.loc[df['Nombre'] == form.cleaned_data['Pizza_2'], 'Precio'].values[0]
            )
            pizza_3 = PizzaMenu(
                nombre=form.cleaned_data['Pizza_3'],
                precio=df.loc[df['Nombre'] == form.cleaned_data['Pizza_3'], 'Precio'].values[0]
            )
            maridaje_1 = Maridaje(
                nombre=form.cleaned_data['Maridaje_1'],
                precio=float(precios[form.cleaned_data['Maridaje_1']])
            )
            maridaje_2 = Maridaje(
                nombre=form.cleaned_data['Maridaje_2'],
                precio=float(precios[form.cleaned_data['Maridaje_2']])
            )
            maridaje_3 = Maridaje(
                nombre=form.cleaned_data['Maridaje_3'],
                precio=float(precios[form.cleaned_data['Maridaje_3']])
            )
            maridaje_4 = Maridaje(
                nombre=form.cleaned_data['Maridaje_4'],
                precio=float(precios[form.cleaned_data['Maridaje_4']])
            )
            postre_1 = Postre(
                nombre=form.cleaned_data['Postre_1'],
                precio=float(precios[form.cleaned_data['Postre_1']])
            )
            postre_2 = Postre(
                nombre=form.cleaned_data['Postre_2'],
                precio=float(precios[form.cleaned_data['Postre_2']])
            )
            postre_3 = Postre(
                nombre=form.cleaned_data['Postre_3'],
                precio=float(precios[form.cleaned_data['Postre_3']])
            )
            postre_4 = Postre(
                nombre=form.cleaned_data['Postre_4'],
                precio=float(precios[form.cleaned_data['Postre_4']])
            )

            menu = Menu(
                tipo=tipo_menu
            )
            menu.add(entrante_1); menu.add(entrante_2); menu.add(entrante_3); menu.add(entrante_4); menu.add(pizza_1); menu.add(pizza_2); menu.add(pizza_3); menu.add(maridaje_1); menu.add(maridaje_2); menu.add(maridaje_3); menu.add(maridaje_4); menu.add(postre_1); menu.add(postre_2); menu.add(postre_3); menu.add(postre_4)
            id_usuario = None
            with open('logs.txt', 'r') as logs_file:
                id_usuario = logs_file.read()
            menus = CSV().leer_menus()
            if menus:
                #si solo hay un elemento en la lista, el código es 1
                if len(menus) == 1:
                    codigo = 1
                else:
                    #si hay más de un elemento, el código es el último código + 1
                    ultimo_codigo = int(menus[-1][0].split(';')[-1])
                    codigo = ultimo_codigo + 1
            CSV().guardar_menus(menu, id_usuario, codigo)
            return redirect('Comprobacion Menu')
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

def comprobacion_menu(request):
    # Lee los datos del archivo CSV
    filas = CSV().leer_menus()

    # Obtén los encabezados y la última fila
    encabezados = filas[0][0].split(';')[:-2]
    ultima_fila = filas[-1][0].split(';')[:-2]
    for elemento in ultima_fila:
        if '[' in elemento:
            ultima_fila[ultima_fila.index(elemento)] = elemento.strip("[]' ")

    # Pasa los datos a la plantilla
    context = {
        'Encabezados': encabezados,
        'Menu': ultima_fila,
    }

    return render(request, 'pizzeriawebapp/comprobacion_menu.html', context)

def borrar_ultimo_menu(request):
    # Lógica para borrar la última línea del archivo CSV
    CSV().borrar_ultimo_menu()

    # Redirige a la página de inicio u otra página que desees después de borrar la línea
    return redirect('Home')

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