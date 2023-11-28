from abc import ABC, abstractmethod
from composite import Carpeta
from utils import es_admin, extraer_usuario


class Arbol_Composite(ABC):
    """
    The Subject interface declares common operations for both RealSubject and
    the Proxy. As long as the client works with RealSubject using this
    interface, you'll be able to pass it a proxy instead of a real subject.
    """

    @abstractmethod
    def request_access(self) -> None:
        pass


class Arbol_Composite_Real(Arbol_Composite):
    def __init__(self, composite):
        self.composite = composite
    """
    The RealSubject contains some core business logic. Usually, RealSubjects are
    capable of doing some useful work which may also be very slow or sensitive -
    e.g. correcting input data. A Proxy can solve these issues without any
    changes to the RealSubject's code.
    """

    def request_access(self) -> None:
        print("Gestionando accesos...")


class Proxy(Arbol_Composite):
    """
    The Proxy has an interface identical to the RealSubject.
    """

    def __init__(self, real_subject: Arbol_Composite_Real) -> None:
        self._real_subject = real_subject

    def request_access(self) -> None:
        """
        The most common applications of the Proxy pattern are lazy loading,
        caching, controlling the access, logging, etc. A Proxy can perform one
        of these things and then, depending on the result, pass the execution to
        the same method in a linked RealSubject object.
        """

        if self.check_access():
            self._real_subject.request()
            self.log_access()
            return True
        else:
            return False

    def check_access(self) -> bool:
        print("Proxy: Comprobando acceso...")
        if es_admin():
            print("Proxy: Acceso concedido.")
            return True
        else:
            print("Proxy: Acceso denegado.")
            return False

    def log_access(self) -> None:
        print("Proxy ha concedido acceso", end="")
        #introducir en logs.txt el acceso concedido de proxy
        logs = open('Ejercicio_3(Samur)/logs.txt', 'a', encoding='utf-8')
        logs.write(f"{extraer_usuario()} ha sido aprobado como administrador\n")
        logs.close()