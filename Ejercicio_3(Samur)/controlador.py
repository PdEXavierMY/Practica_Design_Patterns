import pandas as pd
import json
import re
from composite import Component, Archivo, Enlace, Carpeta

def extraer_usuario():
    ruta_archivo_logs = 'Ejercicio_3(Samur)/logs.txt'
    with open(ruta_archivo_logs, 'r', encoding='utf-8') as archivo_logs:
        primera_linea = archivo_logs.readline()
        match = re.search(r'El usuario [\w\s]+ con id \d+', primera_linea)
        if match:
            return match.group(0)
        else:
            return None

def separador():
    print("--------------------------------------------------")

def login():
    nombre = input("Ingrese su nombre de usuario: ")
    print('\n')
    contraseña = input("Ingrese su contraseña: ")
    print('\n')
    usuarios = pd.read_csv('Ejercicio_3(Samur)/usuarios.csv', sep=';')
    if nombre in usuarios['Usuario'].values:
        if contraseña in usuarios['Contraseña'].values:
            print("¡Bienvenido!")
        else:
            print("Contraseña incorrecta")
            login()
    else:
        print("Nombre de usuario incorrecto")
        login()
    id = usuarios.loc[usuarios['Usuario'] == nombre, 'ID'].values[0]
    #escribir en logs.txt el inicio de sesión
    logs = open('Ejercicio_3(Samur)/logs.txt', 'a', encoding='utf-8')
    logs.write(f"El usuario {nombre} con id {id} ha iniciado sesión\n")
    logs.close()

def registrarse():
    print("Registro de usuario:\n")
    usuario = input("Usuario: ")
    #el nombre de usuario no puede estar vacío ni tener espacios
    while usuario == "" or " " in usuario:
        print("El nombre de usuario no puede estar vacío ni tener espacios")
        usuario = input("Usuario: ")
    print('\n')
    nombre = input("Nombre: ")
    #el nombre no puede estar vacío
    while nombre == "":
        print("El nombre no puede estar vacío!")
        nombre = input("Nombre: ")
    print('\n')
    apellidos = input("Apellidos: ")
    print('\n')
    correo = input("Correo: ")
    #el correo no puede estar vacío, no debe tener espacios y debe tener formato de correo
    while correo == "" or "@" not in correo or ".com" not in correo or ".es" not in correo or " " in correo or correo.count("@") > 1 or correo.count(".com") > 1 or correo.count(".es") > 1:
        print("El correo no puede estar vacío y debe tener formato de correo (solo se admiten .com y .es)")
        correo = input("Correo: ")
    print('\n')
    contraseña = input("Contraseña: ")
    #la contraseña no puede estar vacía
    while contraseña == "":
        print("La contraseña no puede estar vacía!")
        contraseña = input("Contraseña: ")
    print('\n')
    confirmar_contraseña = input("Confirmar Contraseña: ")
    #la contraseña no puede estar vacía
    while confirmar_contraseña == "":
        print("La contraseña no puede estar vacía!")
        confirmar_contraseña = input("Confirmar Contraseña: ")

    if contraseña == confirmar_contraseña:
        usuarios = pd.read_csv('Ejercicio_3(Samur)/usuarios.csv', sep=';')
        ids_registrados = usuarios['ID'].values

        #si el usuario y la contraseña ya existen volver atrás
        if nombre in usuarios['Usuario'].values:
            if contraseña in usuarios['Contraseña'].values:
                print("El usuario ya existe.")
                gestor_usuarios()
        else:
            if len(ids_registrados) == 0:
                identificador = 1
            else:
                identificador = max(ids_registrados) + 1

            nuevo_usuario = pd.DataFrame({'ID': [identificador], 'Usuario': [usuario], 'Nombre': [nombre], 'Apellidos': [apellidos], 'Email': [correo], 'Contraseña': [contraseña]})
            nuevo_usuario.to_csv('Ejercicio_3(Samur)/usuarios.csv', sep=';', mode='a', header=False, index=False)
            print("¡Registro exitoso!")
    else:
        print("Las contraseñas no coinciden. Vuelve a intentarlo.")
        registrarse()
    #escribir en logs.txt el inicio de sesión
    logs = open('Ejercicio_3(Samur)/logs.txt', 'a', encoding='utf-8')
    logs.write(f"El usuario {nombre} con id {identificador} se ha registrado\n")
    logs.close()
    

def login_usuario():
    nombre = input("Ingrese su nombre de usuario: ")
    print('\n')
    contraseña = input("Ingrese su contraseña: ")
    print('\n')
    usuarios = pd.read_csv('Ejercicio_3(Samur)/admin.csv', sep=';')
    if nombre in usuarios['Usuario'].values:
        if contraseña in usuarios['Contraseña'].values:
            print(f"¡Bienvenido administrador {nombre}!")
        else:
            print("Contraseña incorrecta")
            login_usuario()
    else:
        print("Nombre de usuario incorrecto")
        login_usuario()
    id = usuarios.loc[usuarios['Usuario'] == nombre, 'ID'].values[0]
    #escribir en logs.txt el inicio de sesión
    logs = open('Ejercicio_3(Samur)/logs.txt', 'a', encoding='utf-8')
    logs.write(f"El administrador {nombre} con id {id} ha iniciado sesión\n")
    logs.close()

def gestor_usuarios():
    print("1. Login")
    print("2. Registrarse")
    print("3. Salir")
    separador()
    opcion = input("Introduzca una opción: ")
    if opcion == "1":
        login()
        return True
    elif opcion == "2":
        registrarse()
        return True
    elif opcion == "3":
        print("Hasta pronto")
    elif opcion == "/admin":
        login_usuario()
        return True
    else:
        print("\nOpción incorrecta\n")
        gestor_usuarios()

def leer_json():
    with open('Ejercicio_3(Samur)/datos.json') as json_file:
        datos = json.load(json_file)
        print(datos)

def gestor_documentos():
    # Nombre del archivo JSON
    archivo_json = "Ejercicio_3(Samur)/archivos.json"

    # Abrir y cargar el contenido del archivo JSON en un diccionario
    with open(archivo_json, "r") as archivo:
        diccionario = json.load(archivo)
    print("¿Qué desea hacer?")
    print("1. Visualizar los documentos")
    print("2. Buscar un documento")
    print("3. Crear un documento")
    print("4. Editar un documento")
    print("5. Borrar un documento")
    print("6. Buscar una carpeta")
    print("7. Crear una carpeta")
    print("8. Editar una carpeta")
    print("9. Borrar una carpeta")
    print("10. Salir")
    separador()
    opcion = input("Introduzca una opción: ")
    explorador = dic_to_composite(diccionario)
    if opcion == "1":
        print(explorador.visualizar())
    elif opcion == "2":
        print("¿Qué documento desea buscar?")
        nombre_documento = input("Introduzca el nombre del documento: ")
        resultado = buscar_documento(diccionario, nombre_documento)
        if len(resultado) > 0:
            print(f"Se han encontrado {len(resultado)} resultados:")
            for documento in resultado:
                print(f"Nombre: {documento['nombre']}")
                print(f"Tipo: {documento['tipo']}")
                print(f"Tamaño: {documento['tamano']}")
                #si el documento tiene la clave hipervinculo, imprimir el hipervinculo
                if "hipervinculo" in documento:
                    print(f"Hipervínculo: {documento['hipervinculo']}")
        else:
            print("No se han encontrado resultados")
    elif opcion == "3":
        print("¿Qué tipo de documento desea crear? (Debe introducir Enlace si va a ser un hipervínculo):")
        tipo_documento = input("Introduzca el tipo del archivo: ")
        
        nombre_documento = input("Introduzca el nombre del documento: ")
        tamano_documento = input("Introduzca el tamaño del documento: ")
        ruta_documento = input("Introduzca la ruta del archivo: ")
        hipervinculo_documento = None

        if tipo_documento == "Enlace":
            hipervinculo_documento = input("Introduzca el hipervínculo del enlace: ")

        crear_documento(explorador, ruta_documento, nombre_documento, tipo_documento, tamano_documento, hipervinculo_documento)
        print("Documento creado con éxito")
        print(explorador.visualizar())
    '''
    elif opcion == "4":
        editar_documento(diccionario)
    elif opcion == "5":
        borrar_documento(diccionario)
    elif opcion == "6":
        buscar_carpeta(diccionario)
    elif opcion == "7":
        crear_carpeta(diccionario)
    elif opcion == "8":
        editar_carpeta(diccionario)
    elif opcion == "9":
        borrar_carpeta(diccionario)
    elif opcion == "10":
        print("Hasta pronto")
    else:
        print("\nOpción incorrecta\n")
        gestor_documentos()'''

def buscar_documento(diccionario, fragmento_nombre):
    resultados = []

    # Buscar en los documentos de la carpeta actual
    documentos = diccionario.get("documentos", [])
    for documento in documentos:
        if fragmento_nombre.lower() in documento["nombre"].lower():
            resultados.append(documento)

    # Buscar en las carpetas recursivamente
    carpetas = diccionario.get("carpetas", [])
    for carpeta in carpetas:
        resultados.extend(buscar_documento(carpeta, fragmento_nombre))

    return resultados

def dic_to_composite(diccionario):
    # Crear el composite principal (explorador de archivos)
    explorador = Carpeta(diccionario["nombre"])

    # Recorrer las carpetas y documentos del diccionario
    for carpeta_data in diccionario.get("carpetas", []):
        carpeta = dic_to_composite(carpeta_data)
        explorador.add(carpeta)

    for documento_data in diccionario.get("documentos", []):
        if documento_data.get("tipo") == "Enlace":
            documento = Enlace(
                documento_data["nombre"],
                documento_data["tipo"],
                documento_data["tamano"],
                documento_data["hipervinculo"]
            )
        else:
            documento = Archivo(
                documento_data["nombre"],
                documento_data["tipo"],
                documento_data["tamano"]
            )
        explorador.add(documento)

    return explorador

def crear_documento(composite, ruta, nombre, tipo, tamano, hipervinculo=None):
    # Divide la ruta en partes
    partes_ruta = ruta.split('/')

    # Verifica si la primera carpeta en la ruta coincide con la carpeta raíz
    if partes_ruta[0] != composite.nombre:
        print(f"Tu carpeta raíz introducida es '{partes_ruta[0]}'.")
        print(f"No se puede agregar el documento. La carpeta raíz debe ser '{composite.nombre}'.")
        return

    # Inicia desde el composite raíz
    ubicacion = composite

    # Recorre las partes de la ruta para encontrar la ubicación correcta
    for carpeta_nombre in partes_ruta[1:]:
        ubicacion = next((c for c in ubicacion._children if c.nombre == carpeta_nombre), None)
        if ubicacion is None:
            # La carpeta no existe
            print(f"No se puede agregar el documento. La carpeta '{carpeta_nombre}' no existe.")
            return

    # Crea el documento y agrégalo a la ubicación correcta
    if tipo == "Enlace":
        documento = Enlace(nombre, tipo, tamano, hipervinculo)
    else:
        documento = Archivo(nombre, tipo, tamano)
    ubicacion.add(documento)
    print(f"Documento '{nombre}' creado con éxito en la carpeta '{ubicacion.nombre}'.")
    print(composite.visualizar())



# Nombre del archivo JSON
archivo_json = "Ejercicio_3(Samur)/archivos.json"

# Abrir y cargar el contenido del archivo JSON en un diccionario
with open(archivo_json, "r") as archivo:
    diccionario = json.load(archivo)

explorador = dic_to_composite(diccionario)
'''
print(explorador.visualizar())
crear_documento(explorador, "Carpeta 1/Carpeta 2", "Documento 1", "Enlace", "0.001 KB", "https://www.google.com")
crear_documento(explorador, "explorador de archivos/escritorio", "Documento 1", "Enlace", "0.001 KB", "https://www.google.com")
'''