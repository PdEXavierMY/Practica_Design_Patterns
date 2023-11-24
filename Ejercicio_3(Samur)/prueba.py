import json
from composite import *
from proxy import *

# Nombre del archivo JSON
archivo_json = "Ejercicio_3(samur)/archivos.json"

# Leer el contenido del archivo JSON
with open(archivo_json, "r") as archivo:
    contenido_json = archivo.read()

# Convertir el JSON a un diccionario
diccionario_archivos = json.loads(contenido_json)

# Ahora 'diccionario_archivos' contiene la estructura del JSON como un diccionario de Python
print(diccionario_archivos)