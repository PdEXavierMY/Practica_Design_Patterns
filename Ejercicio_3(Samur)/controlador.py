import pandas as pd
import json
import re
from composite import Component, Archivo, Enlaces, Carpeta

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
    if opcion == "1":
        visualizar_documentos(diccionario)
    elif opcion == "2":
        print("¿Qué documento desea buscar?")
        nombre_documento = input("Introduzca el nombre del documento: ")
        buscar_documento(diccionario, nombre_documento)
    elif opcion == "3":
        crear_documento(diccionario)
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
        gestor_documentos()


def visualizar_documentos(diccionario):
    try:
        # Imprimir de manera estructurada
        print(json.dumps(diccionario, indent=2))
        #escribir en logs.txt la visualización de documentos
        logs = open('Ejercicio_3(Samur)/logs.txt', 'a', encoding='utf-8')
        usuario = extraer_usuario()
        logs.write(f"{usuario} ha visualizado los documentos\n")

    except json.JSONDecodeError as e:
        print(f"Error al decodificar JSON: {e}")

def buscar_documento(diccionario, fragmento_nombre):
    def buscar_en_carpeta(carpeta, ruta_actual=""):
        documentos_encontrados = []

        for documento in carpeta.get("documentos", []):
            if fragmento_nombre.lower() in documento["nombre"].lower():
                documentos_encontrados.append(documento)

        for subcarpeta in carpeta.get("carpetas", []):
            nueva_ruta = f"{ruta_actual}/{subcarpeta['nombre']}" if ruta_actual else subcarpeta['nombre']
            documentos_encontrados.extend(buscar_en_carpeta(subcarpeta, nueva_ruta))

        return documentos_encontrados

    documentos_encontrados = []

    for carpeta_raiz in diccionario.get("config", []):
        documentos_encontrados.extend(buscar_en_carpeta(carpeta_raiz))

    if documentos_encontrados:
        print(f"Documentos que contienen '{fragmento_nombre}':")
        for documento_encontrado in documentos_encontrados:
            print(json.dumps(documento_encontrado, indent=2))
    else:
        print(f"No se encontraron documentos que contengan '{fragmento_nombre}'.")
    #escribir en logs.txt la búsqueda realizada
    logs = open('Ejercicio_3(Samur)/logs.txt', 'a', encoding='utf-8')
    usuario = extraer_usuario()
    logs.write(f"{usuario} ha buscado un documento {fragmento_nombre}\n")

def crear_documento(diccionario):
    tipo_documento = input("¿Qué tipo de documento desea crear? (Texto, PDF, Enlace...): ")
    nombre_documento = input(f"Introduzca el nombre del {tipo_documento.lower()}: ")
    print('\n')
    tamaño_documento = input(f"Introduzca el tamaño del {tipo_documento.lower()}: ")
    print('\n')
    
    # Si es un enlace, solicitar hipervínculo
    if tipo_documento == "Enlace":
        hipervinculo = input("Introduzca el hipervínculo: ")
        print('\n')
    else:
        hipervinculo = None

    ruta_carpeta = input("Introduzca la ruta de la carpeta donde desea crear el documento: ")
    print('\n')

    # Crear el documento según el tipo
    if tipo_documento != "Enlace":
        documento = Archivo(nombre_documento, tipo_documento, tamaño_documento)
    else:
        documento = Enlaces(nombre_documento, tipo_documento, tamaño_documento, hipervinculo)

    # Obtener la referencia a la carpeta especificada en ruta_carpeta
    carpetas = ruta_carpeta.split('/')
    carpeta_actual = diccionario
    for carpeta in carpetas:
        if "carpetas" in carpeta_actual:
            carpeta_encontrada = None
            for c in carpeta_actual["carpetas"]:
                if c["nombre"] == carpeta:
                    carpeta_encontrada = c
                    break
            if carpeta_encontrada:
                carpeta_actual = carpeta_encontrada
            else:
                print(f"Error: La carpeta '{carpeta}' no existe en la ruta especificada.")
                return
        else:
            print("Error: La ruta especificada no es válida.")
            return

    # Añadir el documento a la carpeta
    if "documentos" in carpeta_actual:
        carpeta_actual["documentos"].append(documento)
    else:
        carpeta_actual["documentos"] = [documento]

    # Convertir el diccionario a JSON
    json_resultante = json.dumps(diccionario, indent=2)

    # Guardar el JSON actualizado en el archivo
    with open("Ejercicio_3(Samur)/archivos_actualizados.json", "w") as archivo_json:
        archivo_json.write(json_resultante)

    print("Documento creado y añadido correctamente.")



# Nombre del archivo JSON
archivo_json = "Ejercicio_3(Samur)/archivos.json"

# Abrir y cargar el contenido del archivo JSON en un diccionario
with open(archivo_json, "r") as archivo:
    diccionario = json.load(archivo)