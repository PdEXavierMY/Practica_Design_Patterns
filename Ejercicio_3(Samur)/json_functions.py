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
    return composite

def guardar_a_json(composite, nombre_archivo):
    """
    Guarda la estructura del composite en un archivo JSON.
    """
    diccionario = composite_to_dic(composite)
    with open(nombre_archivo, 'w') as archivo:
        json.dump(diccionario, archivo, indent=2)
    print(f"La estructura se ha guardado en '{nombre_archivo}'.")

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

def composite_to_dic(composite):
    """
    Convierte un composite en un diccionario.
    """
    diccionario = {"nombre": composite.nombre}

    carpetas = []
    documentos = []

    for child in composite._children:
        if child.is_composite():
            carpetas.append(composite_to_dic(child))
        else:
            if isinstance(child, Archivo):
                documento = {
                    "nombre": child.nombre,
                    "tipo": child.tipo,
                    "tamano": child.tamaño
                }
            elif isinstance(child, Enlace):
                documento = {
                    "nombre": child.nombre,
                    "tipo": child.tipo,
                    "tamano": child.tamaño,
                    "hipervinculo": child.hipervinculo
                }
            documentos.append(documento)

    if carpetas:
        diccionario["carpetas"] = carpetas
    if documentos:
        diccionario["documentos"] = documentos

    return diccionario