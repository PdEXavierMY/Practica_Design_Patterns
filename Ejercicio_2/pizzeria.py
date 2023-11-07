from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Any

class Builder(ABC):
    @property
    @abstractmethod
    def producto(self) -> None:
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
        self.producto = Pizza()

    @property
    def producto(self) -> None:
        producto = self._producto
        self.reset()
        return producto

    def setMasa(self, masa):
        self.producto.add(masa)

    def setSalsa(self, salsa):
        self.producto.add(salsa)

    def agregarIngrediente(self, ingrediente):
        self.producto.add(ingrediente)

    def setTecnicaDeCoccion(self, tecnica):
        self.producto.add(tecnica)

    def setPresentacion(self, presentacion):
        self.producto.add(presentacion)

    def agregarMaridaje(self, maridaje):
        self.producto.add(maridaje)

    def agregarExtra(self, extra):
        self.producto.add(extra)

class Pizza():
    """
    Podríamos hacer muchas cosas con los ingredientes y características definidas,
    por eso creamos una clase producto concreto que es la pizza.
    """

    def __init__(self) -> None:
        self.parts = []

    def add(self, part: Any) -> None:
        self.parts.append(part)

    def list_parts(self) -> None:
        print(f"Partes de la pizza: {', '.join(self.parts)}", end="")

class Director:

    def __init__(self) -> None:
        self._builder = None

    @property
    def builder(self) -> Builder:
        return self._builder

    @builder.setter
    def builder(self, builder: Builder) -> None:
        """
        The Director works with any builder instance that the client code passes
        to it. This way, the client code may alter the final type of the newly
        assembled product.
        """
        self._builder = builder

    """
    Se pueden construir varias variaciones de producto usando los mismos pasos de construcción.
    """

    def construir_pizza_completa(self, diccionario) -> None:
        self.builder.setMasa(diccionario["masa"])
        self.builder.setSalsa(diccionario["salsa"])
        self.builder.setTecnicaDeCoccion(diccionario["tecnica"])
        self.builder.setPresentacion(diccionario["presentacion"])
        self.builder.agregarMaridaje(diccionario["maridaje"])
        self.builder.agregarExtra(diccionario["extra"])
        self.builder.agregarIngrediente(diccionario["ingredientes"])


if __name__ == "__main__":
    """
    El código del cliente crea un objeto builder, lo pasa al director y luego inicia el proceso de construcción.
    El resultado final se recupera del objeto builder.
    """
    director = Director()
    builder = PizzaBuilder()
    director.builder = builder

    pizza_margarita = {
        "masa": "Masa fina",
        "salsa": "Salsa de tomate",
        "tecnica": "Horno",
        "presentacion": "Redonda",
        "maridaje": "Cerveza",
        "extra": "Queso",
        "ingredientes": "Queso, tomate, albahaca"
    }

    pizza_barbacoa = {
        "masa": "Masa fina",
        "salsa": "Salsa barbacoa",
        "tecnica": "Horno",
        "presentacion": "Rectangular",
        "maridaje": "Cerveza",
        "extra": "Queso",
        "ingredientes": "Queso, tomate, bacon, pollo"
    }

    director.construir_pizza_completa(pizza_margarita)
    builder.producto.list_parts()
    print("\n")
    director.construir_pizza_completa(pizza_barbacoa)
    builder.producto.list_parts()
    print("\n")