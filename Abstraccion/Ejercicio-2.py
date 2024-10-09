"""
Define una clase abstracta Empleado con un método abstracto calcular_salario().
Crea dos clases concretas: EmpleadoTiempoCompleto y EmpleadoPorHoras que heredan
de Empleado y cada una implementa calcular_salario() de manera distinta.
Aplica encapsulamiento, abstracción, polimorfismo y herencia.
"""

from abc import ABC, abstractmethod

class Empleado(ABC):
    def __init__(self, nombre, edad):
        self.__nombre = nombre  # Atributo privado (encapsulamiento)
        self.__edad = edad

    @abstractmethod
    def calcular_salario(self):
        pass
    
    def mostrar_informacion(self):  # Método común (abstracción)
        return f"Empleado: {self.__nombre}, Edad: {self.__edad}"

class EmpleadoTiempoCompleto(Empleado):
    def __init__(self, nombre, edad, salario_mensual):
        super().__init__(nombre, edad)
        self.__salario_mensual = salario_mensual

    def calcular_salario(self):  # Implementación del método abstracto (polimorfismo)
        return self.__salario_mensual

class EmpleadoPorHoras(Empleado):
    def __init__(self, nombre, edad, horas_trabajadas, tarifa_hora):
        super().__init__(nombre, edad)
        self.__horas_trabajadas = horas_trabajadas
        self.__tarifa_hora = tarifa_hora

    def calcular_salario(self):  # Implementación del método abstracto (polimorfismo)
        return self.__horas_trabajadas * self.__tarifa_hora

# Uso de las clases
empleado_tc = EmpleadoTiempoCompleto("Carlos", 30, 3000)
empleado_ph = EmpleadoPorHoras("Ana", 25, 120, 20)

print(empleado_tc.mostrar_informacion())
print(f"Salario Tiempo Completo: {empleado_tc.calcular_salario()}")

print(empleado_ph.mostrar_informacion())
print(f"Salario Por Horas: {empleado_ph.calcular_salario()}")
