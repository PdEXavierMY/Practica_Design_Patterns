from __future__ import annotations
from abc import ABC, abstractmethod
import matplotlib.pyplot as plt

class Visualizacion(ABC):
    @abstractmethod
    def generar_visualizacion(self, dataset):
        pass

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
        # Generar un gráfico de barras a partir del dataset
        plt.bar(range(len(dataset)), dataset, color='green')
        plt.xlabel('Categorías')
        plt.ylabel('Valores')
        plt.title('Gráfico de Barras')
        plt.show()

class Gcirculo(Visualizacion):
    def generar_visualizacion(self, dataset):
        # Generar un gráfico circular (de queso) a partir del dataset
        plt.pie(dataset, labels=range(len(dataset)), autopct='%1.1f%%', startangle=90)
        plt.axis('equal')
        plt.title('Gráfico Circular')
        plt.show()

'''# Ejemplo de uso:
datos = [10, 20, 30, 40, 50]
histograma_visualizacion = Histograma()
barras_visualizacion = Barras()
gcirculo_visualizacion = Gcirculo()

histograma_visualizacion.generar_visualizacion(datos)
barras_visualizacion.generar_visualizacion(datos)
gcirculo_visualizacion.generar_visualizacion(datos)'''