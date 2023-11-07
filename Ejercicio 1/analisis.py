from __future__ import annotations
from abc import ABC, abstractmethod
from statistics import mean, median, mode

#Producto abstracto
class Analisis(ABC):
    @abstractmethod
    def analizar(self, dataset):
        pass


#Productos concretos
class Media(Analisis):
    def analizar(self, dataset):
        return mean(dataset)

class Mediana(Analisis):
    def analizar(self, dataset):
        return median(dataset)

class Moda(Analisis):
    def analizar(self, dataset):
        return mode(dataset)