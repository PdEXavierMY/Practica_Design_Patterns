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
    
    def setNombre(self, nombre):
        self._product.nombre = nombre

    def setMasa(self, masa):
        self._product.masa = masa

    def setSalsa(self, salsa):
        self._product.salsa = salsa

    def agregarIngrediente(self, ingrediente):
        self._product.ingredientes = ingrediente

    def setTecnicaDeCoccion(self, tecnica):
        self._product.tecnica = tecnica

    def setPresentacion(self, presentacion):
        self._product.presentacion = presentacion

    def agregarExtra(self, extra):
        self._product.extras = extra

class Pizza:
    def __init__(self):
        self.nombre = None
        self.masa = None
        self.salsa = None
        self.ingredientes = None
        self.tecnica = None
        self.presentacion = None
        self.extras = None
    
    def to_csv(self):
        return [str(self.nombre)+";"+str(self.masa)+";"+str(self.salsa)+";"+str(self.ingredientes)+";"+str(self.tecnica)+";"+str(self.presentacion)+";"+str(self.extras)]

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

    def construir_pizza_completa(self, partes) -> None:
        self.builder.setNombre(partes[0])
        self.builder.setMasa(partes[1])
        self.builder.setSalsa(partes[2])
        self.builder.agregarIngrediente(partes[3])
        self.builder.setTecnicaDeCoccion(partes[4])
        self.builder.setPresentacion(partes[5])
        self.builder.agregarExtra(partes[6])


class Usuario():
    def __init__(self, usuario, nombre, apellidos, email, contraseña):
        self.usuario = usuario
        self.nombre = nombre
        self.apellidos = apellidos
        self.email = email
        self.contraseña = contraseña

    def to_csv(self):
        return [self.usuario+";"+self.nombre+";"+self.apellidos+";"+self.email+";"+self.contraseña]
    
class UsuarioLogin():
    def __init__(self, usuario, contraseña):
        self.usuario = usuario
        self.contraseña = contraseña

    def to_csv(self):
        return [self.usuario+";"+self.contraseña]