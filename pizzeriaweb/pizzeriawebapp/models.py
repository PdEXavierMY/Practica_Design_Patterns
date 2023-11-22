from __future__ import annotations
from django.db import models
from abc import ABC, abstractmethod
from typing import Any, Optional, List

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
    
class Component(ABC):
    """
    The base Component class declares common operations for both simple and
    complex objects of a composition.
    """

    @property
    def parent(self) -> Component:
        return self._parent

    @parent.setter
    def parent(self, parent: Component):
        """
        Optionally, the base Component can declare an interface for setting and
        accessing a parent of the component in a tree structure. It can also
        provide some default implementation for these methods.
        """

        self._parent = parent

    """
    In some cases, it would be beneficial to define the child-management
    operations right in the base Component class. This way, you won't need to
    expose any concrete component classes to the client code, even during the
    object tree assembly. The downside is that these methods will be empty for
    the leaf-level components.
    """

    def add(self, component: Component) -> None:
        pass

    def remove(self, component: Component) -> None:
        pass

    def is_composite(self) -> bool:
        """
        You can provide a method that lets the client code figure out whether a
        component can bear children.
        """

        return False

    @abstractmethod
    def operation(self) -> str:
        """
        The base Component may implement some default behavior or leave it to
        concrete classes (by declaring the method containing the behavior as
        "abstract").
        """

        pass


class Bebida(Component):
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

class PizzaMenu(Component):
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

class Entrante(Component):
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

class Postre(Component):
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

class Menu(Component):
    """
    The Composite class represents the complex components that may have
    children. Usually, the Composite objects delegate the actual work to their
    children and then "sum-up" the result.
    """

    def __init__(self) -> None:
        self._children: List[Component] = []

    """
    A composite object can add or remove other components (both simple or
    complex) to or from its child list.
    """

    def add(self, component: Component) -> None:
        self._children.append(component)
        component.parent = self

    def remove(self, component: Component) -> None:
        self._children.remove(component)
        component.parent = None

    def is_composite(self) -> bool:
        return True