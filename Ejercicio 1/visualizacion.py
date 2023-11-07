from __future__ import annotations
from abc import ABC, abstractmethod
import matplotlib.pyplot as plt

#producto abstracto
class Visualizacion(ABC):
    @abstractmethod
    def generar_visualizacion(self, dataset):
        pass

    def mostrar_datos(self, dataset):
        print(dataset)


#productos concreto
class Histograma(Visualizacion):
    def generar_visualizacion(self, dataset):
        # Generar un histograma a partir del dataset
        plt.hist(dataset, bins=10, color='skyblue', edgecolor='black')
        plt.xlabel('Valores')
        plt.ylabel('Frecuencia')
        plt.title('Histograma')
        plt.show()

class Barras(Visualizacion):
    def generar_visualizacion(self, dataset):
        # Contar el número de repeticiones de cada valor
        valores_unicos = list(set(dataset))
        conteo_valores = [dataset.count(valor) for valor in valores_unicos]

        # Ubicación de las barras en el eje x
        ubicacion_barras = range(len(valores_unicos))

        # Generar un gráfico de barras con etiquetas en el eje x y conteo en el eje y
        plt.bar(ubicacion_barras, conteo_valores, color='green')
        plt.xlabel('Valores')
        plt.ylabel('Número de Repeticiones')
        plt.title('Gráfico de Barras')

        # Establecer las etiquetas en el eje x
        plt.xticks(ubicacion_barras, valores_unicos)

        plt.show()

class Gcirculo(Visualizacion):
    def generar_visualizacion(self, dataset):
        # Generar un gráfico circular (de queso) a partir del dataset
        plt.pie(dataset, labels=range(len(dataset)), autopct='%1.1f%%', startangle=90)
        plt.axis('equal')
        plt.title('Gráfico Circular')
        plt.show()