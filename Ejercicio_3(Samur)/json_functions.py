import json
from composite import *

def leer_json():
    with open('Ejercicio_3(Samur)/datos.json') as json_file:
        datos = json.load(json_file)
        print(datos)

def cargar_desde_json(nombre_archivo):
    """
    Carga la estructura desde un archivo JSON y devuelve el composite correspondiente.
    """
    with open(nombre_archivo, 'r') as archivo:
        diccionario = json.load(archivo)
    composite = dic_to_composite(diccionario)
    print(f"La estructura se ha cargado desde '{nombre_archivo}'.")
    return composite

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