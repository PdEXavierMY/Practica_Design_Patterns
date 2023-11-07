from __future__ import annotations
from abc import ABC, abstractmethod
from Ejercicio_1.analisis import Analisis, Media, Mediana, Moda
from Ejercicio_1.visualizacion import Visualizacion, Histograma, Barras, Gcirculo
    
# Fábrica para crear objetos de visualización
class VisualizacionFactory(ABC):
    @abstractmethod
    def crear_visualizacion(self) -> Visualizacion:
        pass

class HistogramaFactory(VisualizacionFactory):
    def crear_visualizacion(self) -> Visualizacion:
        return Histograma()

class BarrasFactory(VisualizacionFactory):
    def crear_visualizacion(self) -> Visualizacion:
        return Barras()

class GcirculoFactory(VisualizacionFactory):
    def crear_visualizacion(self) -> Visualizacion:
        return Gcirculo()

# Fábrica para crear objetos de análisis de datos
class AnalisisFactory(ABC):
    @abstractmethod
    def crear_analisis(self) -> Analisis:
        pass

class MediaFactory(AnalisisFactory):
    def crear_analisis(self) -> Analisis:
        return Media()

class MedianaFactory(AnalisisFactory):
    def crear_analisis(self) -> Analisis:
        return Mediana()

class ModaFactory(AnalisisFactory):
    def crear_analisis(self) -> Analisis:
        return Moda()