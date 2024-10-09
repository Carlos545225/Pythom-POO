"""
Define una clase abstracta TareaEmpleado con un método abstracto realizar_tarea().
Crea dos clases concretas: Ingeniero y Doctor que heredan de TareaEmpleado y cada
una implementa realizar_tarea() de manera específica según su especialidad.
Aplica encapsulamiento, abstracción, polimorfismo y herencia.
"""

from abc import ABC, abstractmethod

class TareaEmpleado(ABC):
    def __init__(self, nombre, especialidad):
        self.__nombre = nombre  # Atributo privado (encapsulamiento)
        self.__especialidad = especialidad

    @abstractmethod
    def realizar_tarea(self):
        pass

    def mostrar_informacion(self):  # Método común para todas las subclases (abstracción)
        return f"Empleado: {self.__nombre}, Especialidad: {self.__especialidad}"

class Ingeniero(TareaEmpleado):
    def __init__(self, nombre, especialidad, proyecto):
        super().__init__(nombre, especialidad)
        self.__proyecto = proyecto

    def realizar_tarea(self):  # Implementación específica para Ingeniero (polimorfismo)
        return f"Trabajando en el proyecto: {self.__proyecto}"

class Doctor(TareaEmpleado):
    def __init__(self, nombre, especialidad, pacientes):
        super().__init__(nombre, especialidad)
        self.__pacientes = pacientes

    def realizar_tarea(self):  # Implementación específica para Doctor (polimorfismo)
        return f"Atendiendo a {self.__pacientes} pacientes hoy"

# Uso de las clases
ingeniero = Ingeniero("Carlos", "Ingeniería Civil", "Construcción de Puente")
doctor = Doctor("Ana", "Medicina General", 10)

print(ingeniero.mostrar_informacion())
print(ingeniero.realizar_tarea())

print(doctor.mostrar_informacion())
print(doctor.realizar_tarea())
