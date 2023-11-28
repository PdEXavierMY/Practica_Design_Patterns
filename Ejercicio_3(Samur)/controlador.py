from utils import separador
from gestion_archivos import *
from json_functions import *

def gestor_documentos():
    # Nombre del archivo JSON
    archivo_json = "Ejercicio_3(Samur)/archivos.json"
    explorador = cargar_desde_json(archivo_json)

    print("¿Qué desea hacer?")
    print("1. Visualizar la estructura de documentos")
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
        print(explorador.visualizar())
    elif opcion == "2":
        print("¿Qué documento desea buscar?")
        nombre_documento = input("Introduzca el nombre del documento: ")
        buscar_documento(explorador, nombre_documento)
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
        #guardar en el json
        guardar_a_json(explorador, archivo_json)
    elif opcion == "4":
        print("¿Qué documento desea editar?")
        nombre_documento = input("Introduzca el nombre del documento: ")
        atributo_a_modificar = input("Introduzca el atributo que desea modificar: ")
        nuevo_valor = input("Introduzca el nuevo valor: ")
        ruta_documento = input("Introduzca la ruta del archivo: ")
        editar_documento(explorador, ruta_documento, nombre_documento, atributo_a_modificar, nuevo_valor)
        #guardar en el json
        guardar_a_json(explorador, archivo_json)
    elif opcion == "5":
        print("¿Qué documento desea borrar?")
        nombre_documento = input("Introduzca el nombre del documento: ")
        ruta_documento = input("Introduzca la ruta del archivo: ")
        borrar_documento(explorador, ruta_documento, nombre_documento)
        #guardar en el json
        guardar_a_json(explorador, archivo_json)
    elif opcion == "6":
        print("¿Qué carpeta desea buscar?")
        nombre_carpeta = input("Introduzca el nombre de la carpeta: ")
        buscar_carpeta(explorador, nombre_carpeta)
    elif opcion == "7":
        print("¿Qué carpeta desea crear?")
        nombre_carpeta = input("Introduzca el nombre de la carpeta: ")
        ruta_carpeta = input("Introduzca la ruta de la carpeta: ")
        crear_carpeta(explorador, ruta_carpeta, nombre_carpeta)
        #guardar en el json
        guardar_a_json(explorador, archivo_json)
    elif opcion == "8":
        print("¿Qué carpeta desea editar?")
        nombre_carpeta = input("Introduzca el nombre de la carpeta: ")
        nuevo_nombre = input("Introduzca el nuevo nombre de la carpeta: ")
        ruta_carpeta = input("Introduzca la ruta de la carpeta: ")
        editar_carpeta(explorador, ruta_carpeta, nombre_carpeta, nuevo_nombre)
        #guardar en el json
        guardar_a_json(explorador, archivo_json)
    elif opcion == "9":
        print("¿Qué carpeta desea borrar?")
        nombre_carpeta = input("Introduzca el nombre de la carpeta: ")
        ruta_carpeta = input("Introduzca la ruta de la carpeta: ")
        borrar_carpeta(explorador, ruta_carpeta, nombre_carpeta)
        #guardar en el json
        guardar_a_json(explorador, archivo_json)
    elif opcion == "10":
        print("Hasta pronto")
    else:
        print("\nOpción incorrecta\n")
        gestor_documentos()


if __name__ == "__main__":
    gestor_documentos()