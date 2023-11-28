import re

def extraer_usuario():
    ruta_archivo_logs = 'Ejercicio_3(Samur)/logs.txt'
    with open(ruta_archivo_logs, 'r', encoding='utf-8') as archivo_logs:
        primera_linea = archivo_logs.readline()
        match = re.search(r'El (usuario|administrador) [\w\s]+ con id \d+', primera_linea)
        if match:
            return match.group(0)
        else:
            return None
        
def es_admin():

    registro_usuario = extraer_usuario()

    if any(variacion in registro_usuario for variacion in ["admin", "administrador", "administradora"]):
        return True
    else:
        return False


def separador():
    print("--------------------------------------------------")