from __future__ import annotations
from abc import ABC, abstractmethod
from statistics import mean, median, mode

class Analisis(ABC):
    @abstractmethod
    def analizar(self, dataset):
        pass



class Media(Analisis):
    def analizar(self, dataset):
        return mean(dataset)

class Mediana(Analisis):
    def analizar(self, dataset):
        return median(dataset)

class Moda(Analisis):
    def analizar(self, dataset):
        return mode(dataset)
    
'''# Ejemplo de uso:
datos = [1, 2, 3, 4, 5, 5, 6, 6, 6, 7]
media_analisis = Media()
mediana_analisis = Mediana()
moda_analisis = Moda()

print("Media:", media_analisis.analizar(datos))
print("Mediana:", mediana_analisis.analizar(datos))
print("Moda:", moda_analisis.analizar(datos))'''