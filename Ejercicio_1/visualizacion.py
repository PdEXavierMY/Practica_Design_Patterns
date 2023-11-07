from __future__ import annotations
from abc import ABC, abstractmethod
import matplotlib.pyplot as plt
from collections import Counter

#producto abstracto
class Visualizacion(ABC):
    @abstractmethod
    def generar_visualizacion(self, dataset, titulo):
        pass

    def mostrar_datos(self, dataset):
        print(dataset)


#productos concreto
class Histograma(Visualizacion):
    def generar_visualizacion(self, dataset, titulo):
        # Generar un histograma a partir del dataset
        plt.hist(dataset, bins=10, color='skyblue', edgecolor='black')
        plt.xlabel('Valores')
        plt.ylabel('Frecuencia')
        plt.title(titulo)  # Usar el título proporcionado como argumento
        plt.show()

class Barras(Visualizacion):
    def generar_visualizacion(self, dataset, titulo):
        # Contar el número de repeticiones de cada valor
        valores_unicos = list(set(dataset))
        conteo_valores = [dataset.count(valor) for valor in valores_unicos]

        # Ubicación de las barras en el eje x
        ubicacion_barras = range(len(valores_unicos))

        # Generar un gráfico de barras con etiquetas en el eje x y conteo en el eje y
        plt.bar(ubicacion_barras, conteo_valores, color='green')
        plt.xlabel('Valores')
        plt.ylabel('Número de Repeticiones')
        plt.title(titulo)  # Usar el título proporcionado como argumento
        plt.xticks(ubicacion_barras, valores_unicos)  # Establecer las etiquetas en el eje x
        plt.show()

    def generar_visualizacion_string(self, dataset, titulo):
        # Separar los días en cada fila y contar su frecuencia
        dias = [dia for fila in dataset for dia in fila.split(',')]
        conteo_dias = Counter(dias)

        # Extraer los días únicos y sus frecuencias
        dias_unicos = list(conteo_dias.keys())
        frecuencias = list(conteo_dias.values())

        # Generar un histograma con etiquetas en el eje x y frecuencias en el eje y
        plt.bar(dias_unicos, frecuencias, color='skyblue', edgecolor='black')
        plt.xlabel('Días de la Semana')
        plt.ylabel('Frecuencia')
        plt.title(titulo)  # Usar el título proporcionado como argumento
        plt.show()

class Gcirculo(Visualizacion):
    def generar_visualizacion(self, dataset, titulo):
        # Contar el número de repeticiones de cada tipo de actividad
        conteo_actividades = Counter(dataset)

        # Extraer los tipos de actividad y sus repeticiones
        tipos_actividades = list(conteo_actividades.keys())
        repeticiones = list(conteo_actividades.values())

        # Colores para las porciones del gráfico
        colores = ['lightcoral', 'lightblue', 'lightgreen', 'lightsalmon', 'lightcyan']

        # Generar un gráfico circular (de queso) con etiquetas, leyenda y colores
        plt.pie(repeticiones, labels=tipos_actividades, autopct='%1.1f%%', startangle=90, colors=colores)
        plt.axis('equal')
        plt.title(titulo)  # Usar el título proporcionado como argumento
        plt.show()