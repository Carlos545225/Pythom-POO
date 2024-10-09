"""
Define una clase abstracta FormaGeometrica con un método abstracto calcular_area().
Crea dos clases concretas: Cuadrado y Circulo que heredan de FormaGeometrica y cada
una debe implementar su propia versión de calcular_area()
"""

from abc import ABC, abstractmethod
import math

class FormaGeometrica(ABC):
    @abstractmethod
    def calcular_area(self):
        pass

class Cuadrado(FormaGeometrica):
    def __init__(self, lado):
        self.lado = lado

    def calcular_area(self):
        return self.lado ** 2

class Circulo(FormaGeometrica):
    def __init__(self, radio):
        self.radio = radio

    def calcular_area(self):
        return math.pi * (self.radio ** 2)

# Uso de las clases
cuadrado = Cuadrado(5)
print(f"Área del cuadrado: {cuadrado.calcular_area()}")

circulo = Circulo(3)
print(f"Área del círculo: {circulo.calcular_area()}")
