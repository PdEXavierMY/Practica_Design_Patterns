from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Any
from pizza import Pizza

class Builder(ABC):
    @property
    @abstractmethod
    def product(self) -> None:
        pass

    @abstractmethod
    def setMasa(self, masa):
        pass

    @abstractmethod
    def setSalsa(self, salsa):
        pass

    @abstractmethod
    def agregarIngrediente(self, ingrediente):
        pass

    @abstractmethod
    def setTecnicaDeCoccion(self, tecnica):
        pass

    @abstractmethod
    def setPresentacion(self, presentacion):
        pass

    @abstractmethod
    def agregarMaridaje(self, maridaje):
        pass

    @abstractmethod
    def agregarExtra(self, extra):
        pass

class PizzaBuilder(Builder):
    
    def __init__(self) -> None:
        """
        A fresh builder instance should contain a blank product object, which is
        used in further assembly.
        """
        self.reset()

    def reset(self) -> None:
        self._product = Pizza()  # Cambio de nombre del atributo

    @property
    def product(self) -> None:
        product = self._product
        self.reset()
        return product

    def setMasa(self, masa):
        self._product.add(masa)

    def setSalsa(self, salsa):
        self._product.add(salsa)

    def agregarIngrediente(self, ingrediente):
        self._product.add(ingrediente)

    def setTecnicaDeCoccion(self, tecnica):
        self._product.add(tecnica)

    def setPresentacion(self, presentacion):
        self._product.add(presentacion)

    def agregarMaridaje(self, maridaje):
        self._product.add(maridaje)

    def agregarExtra(self, extra):
        self._product.add(extra)