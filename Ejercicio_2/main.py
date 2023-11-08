from director import Director
from builder import PizzaBuilder

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
    builder.product.list_parts()
    print("\n")
    director.construir_pizza_completa(pizza_barbacoa)
    builder.product.list_parts()
    print("\n")