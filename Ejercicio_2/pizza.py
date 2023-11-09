from __future__ import annotations
from typing import Any

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