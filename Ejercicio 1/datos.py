import pandas as pd
import random

class Limpieza_datos(object):
    def __init__(self, data):
        self.data = data

    def vista_inicial(self):
        print("Cabeza del dataset:")
        print(self.data.head(), "\n")
        print("Cola del dataset:")
        print(self.data.tail(), "\n")
        print("Dimensiones del dataset:")
        print(self.data.shape, "\n")
        print("Columnas del dataset:")
        print(self.data.columns, "\n")
        print("Tipos de datos:")
        print(self.data.dtypes, "\n")
        print("Valores únicos:")
        print(self.data.describe(), "\n")
        print("Valores nulos:")
        print(self.data.isnull().sum(), "\n")

    def vista_columna(self, columna):
        print("Columna:")
        print(self.data[columna], "\n")
        print("Valores únicos de la columna", columna)
        print(self.data[columna].unique(), "\n")
        print("Número de valores únicos de la columna", columna)
        print(len(self.data[columna].unique()), "\n")
        print("Número de valores nulos de la columna", columna)
        print(self.data[columna].isnull().sum(), "\n")

    def eliminar_columna(self, columna):
        self.data = self.data.drop(columna, axis=1)

    def rellenar_nulos(self, columna, valor):
        self.data[columna] = self.data[columna].fillna(valor)

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
    #añadir una columna con un precio aleatorio de 0 a 15 para cada evento
    precios = []
    for i in range(len(datos.data)):
        precios.append(random.randint(0, 15))
    datos.data["PRECIO"] = precios
    print("Vista del dataset tras añadir la columna PRECIO:\n")
    datos.vista_inicial()
    #guardar el dataset
    datos.data.to_csv("Ejercicio 1/datos_limpio.csv", sep=';', encoding='UTF-8', index=False)