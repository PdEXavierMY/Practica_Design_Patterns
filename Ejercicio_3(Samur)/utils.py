import re
import json

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

def leer_json():
    with open('Ejercicio_3(Samur)/datos.json') as json_file:
        datos = json.load(json_file)
        print(datos)