from __future__ import annotations
from abc import ABC, abstractmethod
from analisis import Analisis, Media, Mediana, Moda
from visualizacion import Visualizacion, Histograma, Barras, Gcirculo


class AbstractFactory(ABC):

    @abstractmethod
    def create_analisis(self) -> Analisis:
        pass

    @abstractmethod
    def create_visualizacion(self) -> Visualizacion:
        pass


class Estudio_inicial(AbstractFactory):

    def create_analisis(self) -> Analisis:
        return Media()

    def create_visualizacion(self) -> Visualizacion:
        return Histograma()


class Estudio2(AbstractFactory):

    def create_analisis(self) -> Analisis:
        return Mediana()

    def create_visualizacion(self) -> Visualizacion:
        return Barras()
    
    
class Estudio_final(AbstractFactory):

    def create_analisis(self) -> Analisis:
        return Moda()

    def create_visualizacion(self) -> Visualizacion:
        return Gcirculo()