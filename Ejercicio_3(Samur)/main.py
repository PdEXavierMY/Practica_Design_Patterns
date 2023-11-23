from controlador import *
import pandas as pd

if __name__ == "__main__":
    #borrar el contenido de logs.txt
    logs = open('Ejercicio_3(Samur)/logs.txt', 'w')
    logs.write("")
    logs.close()
    print("Bienvenido al gestor de documentos")
    separador()
    print("Identifíquese:")
    separador()
    separador()
    identificacion = gestor()
    if identificacion:
        pass