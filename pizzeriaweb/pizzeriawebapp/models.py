from django.db import models
from abc import ABC, abstractmethod
from typing import Any

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
        self._product = Pizza()

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

class Pizza():
    """
    Podríamos hacer muchas cosas con los ingredientes y características definidas,
    por eso creamos una clase producto concreto que es la pizza.
    """

    def __init__(self) -> None:
        self.parts = []

    def add(self, part: Any) -> None:
        self.parts.append(part)

    def list_parts(self):
        print(f"Partes de la pizza: {', '.join(self.parts)}", end="")

    def get_parts(self):
        #devuelve la lista con las partes de la pizza
        return self.parts

class Director():
    """
    El director solo es responsable de ejecutar los pasos de construcción en una
    secuencia particular. Es útil cuando se producen objetos de acuerdo con un
    orden o configuración específicos. En este caso, se trata de una pizza.
    """

    def __init__(self) -> None:
        self._builder = None

    @property
    def builder(self) -> Builder:
        return self._builder

    @builder.setter
    def builder(self, builder: Builder) -> None:
        """
        El director funciona con cualquier instancia de constructor que el código
        del cliente le pase. De esta manera, el código del cliente puede cambiar
        el tipo final del producto recién ensamblado.
        """
        self._builder = builder

    """
    El director puede construir varias configuraciones de productos utilizando
    las mismas etapas de construcción.
    """

    def construir_pizza_completa(self, diccionario) -> None:
        self.builder.setMasa(diccionario["masa"])
        self.builder.setSalsa(diccionario["salsa"])
        self.builder.setTecnicaDeCoccion(diccionario["tecnica"])
        self.builder.setPresentacion(diccionario["presentacion"])
        self.builder.agregarMaridaje(diccionario["maridaje"])
        self.builder.agregarExtra(diccionario["extra"])
        self.builder.agregarIngrediente(diccionario["ingredientes"])


class Usuario():
    def __init__(self, usuario, nombre, apellidos, email, contraseña):
        self.usuario = usuario
        self.nombre = nombre
        self.apellidos = apellidos
        self.email = email
        self.contraseña = contraseña

    def to_csv(self):
        return [self.usuario+";"+self.nombre+";"+self.apellidos+";"+self.email+";"+self.contraseña]