import pandas as pd
from datos import *

if __name__ == "__main__":
    URL = "https://datos.madrid.es/egob/catalogo/212504-0-emergencias-activaciones.csv"
    data = pd.read_csv(URL, sep=';', encoding='ISO-8859-1')
    datos = Limpieza_datos(data)
    print("Vista inicial del dataset:\n")
    datos.vista_inicial()
    #vamos a eliminar las columnas que no sirven
    columnas = [
    "PRECIO",
    "DIAS-EXCLUIDOS",
    "HORA",
    "DESCRIPCION",
    "URL-INSTALACION",
    "NOMBRE-INSTALACION",
    "ACCESIBILIDAD-INSTALACION",
    "CLASE-VIAL-INSTALACION",
    "NOMBRE-VIA-INSTALACION",
    "NUM-INSTALACION",
    "DISTRITO-INSTALACION",
    "BARRIO-INSTALACION",
    "CODIGO-POSTAL-INSTALACION",
    "COORDENADA-X",
    "COORDENADA-Y",
    "LATITUD",
    "LONGITUD",
    "AUDIENCIA",
    "Unnamed: 29"
]
    for columna in columnas:
        datos.eliminar_columna(columna)
    print("Vista del dataset tras eliminar columnas:\n")
    datos.vista_inicial()
    print("Vista de la columna DIAS-SEMANA:\n")
    datos.vista_columna("DIAS-SEMANA")
    print("Vista de la columna TITULO-ACTIVIDAD:\n")
    datos.vista_columna("TITULO-ACTIVIDAD")
    print("Vista de la columna URL-ACTIVIDAD:\n")
    datos.vista_columna("URL-ACTIVIDAD")
    print("Vista de la columna TIPO:\n")
    datos.vista_columna("TIPO")
    #ahora rellenar los pocos valores nulos
    datos.rellenar_nulos("DIAS-SEMANA", "S, D")
    datos.rellenar_nulos("TITULO-ACTIVIDAD", "Actividad sin nombre")
    datos.rellenar_nulos("URL-ACTIVIDAD", "Sin URL")
    datos.rellenar_nulos("TIPO", "Sin tipo")
    print("Vista del dataset tras rellenar valores nulos:\n")
    datos.vista_inicial()