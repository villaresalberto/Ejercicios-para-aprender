#!/usr/bin/env pyhon3

# Clase Animal, como si ponemos clase caraculo aunque vaya de animales. o como si ponemos Animal y va de diferentes cara culos, eso da igual.
class Animal:
# Funcion constructor
    def __init__(self, nombre, tipo, edad):

        self.nombre = nombre
        self.tipo = tipo                # Atributos creados
        self.edad = edad

# Funión método presentarse
    def presentarse(self):

        return f"Hola, soy {self.nombre} y soy un {self.tipo}. Tengo {self.edad} años"
# Función método cumplir años
    def cumplir_anios(self):
        self.edad += 1
        print(f"¡Felicidades {self.nombre}! Ahora tines {self.edad}")

# Creación de los animales
animal = Animal("Paul", "Perro", 11)            # Instancias
animal_2 = Animal("Karma", "Gato", 8)
animal_3 = Animal("Mini", "Serpiente", 3)

# Presentaciones
print(animal.presentarse())
print(animal_2.presentarse())
print(animal_3.presentarse())

# Animales cumpliendo años
animal.cumplir_anios()
animal_2.cumplir_anios()
