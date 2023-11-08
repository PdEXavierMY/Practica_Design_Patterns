from builder import Builder

class Director:

    def __init__(self) -> None:
        self._builder = None

    @property
    def builder(self) -> Builder:
        return self._builder

    @builder.setter
    def builder(self, builder: Builder) -> None:
        self._builder = builder

    def construir_pizza_completa(self, diccionario) -> None:
        self.builder.setMasa(diccionario["masa"])
        self.builder.setSalsa(diccionario["salsa"])
        self.builder.setTecnicaDeCoccion(diccionario["tecnica"])
        self.builder.setPresentacion(diccionario["presentacion"])
        self.builder.agregarMaridaje(diccionario["maridaje"])
        self.builder.agregarExtra(diccionario["extra"])
        self.builder.agregarIngrediente(diccionario["ingredientes"])