import json
from composite import *
from proxy import *

'''# Nombre del archivo JSON
archivo_json = "Ejercicio_3(Samur)/archivos.json"
archivo_json_prueba = "Ejercicio_3(Samur)/archivos2.json"
explorador = cargar_desde_json(archivo_json)

print(explorador.visualizar())
buscar_documento(explorador, "se")
crear_documento(explorador, "explorador de archivos/escritorio", "Documento 1", "Enlace", "0.001 KB", "https://www.google.com")
editar_documento(explorador, "explorador de archivos/escritorio", "Documento 1", "nombre", "Documento 2")
borrar_documento(explorador, "explorador de archivos/escritorio", "Documento 2")
separador()
buscar_carpeta(explorador, "config")
crear_carpeta(explorador, "explorador de archivos/escritorio/config", "Carpeta 1")
crear_documento(explorador, "explorador de archivos/escritorio/config/Carpeta 1", "Documento 1", "Enlace", "0.001 KB", "https://www.google.com")
editar_carpeta(explorador, "explorador de archivos/escritorio/config", "Carpeta 1", "Carpeta 2")
borrar_carpeta(explorador, "explorador de archivos/escritorio/config", "Carpeta 2")
crear_documento(explorador, "Carpeta 1/Carpeta 2", "Documento 1", "Enlace", "0.001 KB", "https://www.google.com")
crear_documento(explorador, "explorador de archivos/escritorio", "Documento 1", "Enlace", "0.001 KB", "https://www.google.com")
crear_carpeta(explorador, "explorador de archivos/escritorio", "Carpeta 1")
crear_carpeta(explorador, "explorador de archivos/escritorio", "Carpeta 2")
crear_documento(explorador, "explorador de archivos/escritorio/Carpeta 2", "Documento Prueba", "Texto", "20 KB")
crear_carpeta(explorador, "explorador de archivos/escritorio/Carpeta 1", "Prueba")

guardar_a_json(explorador, archivo_json_prueba)

explrador2 = cargar_desde_json(archivo_json_prueba)
print(explrador2.visualizar())'''