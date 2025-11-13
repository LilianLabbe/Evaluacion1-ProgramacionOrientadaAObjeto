# Ejercicio 4 — Sensor y Mediciones
# Diseñe un sistema sencillo para registrar y analizar las mediciones de un sensor. Cada sensor debe estar
# identificado por un nombre y almacenar los valores de sus mediciones a lo largo del tiempo. El sistema
# debe permitir registrar nuevos valores para el sensor y consultar en cualquier momento el promedio de
# las mediciones realizadas, así como el valor máximo y el valor mínimo registrados.
# Requerimientos funcionales
# • El sistema debe permitir definir un sensor, indicando su nombre.
# • El sistema debe permitir registrar nuevas mediciones asociadas a ese sensor.
# • El sistema debe permitir consultar el promedio de todas las mediciones registradas para el
# sensor.
# • El sistema debe permitir consultar el valor máximo registrado por el sensor.
# • El sistema debe permitir consultar el valor mínimo registrado por el sensor.
# • El sistema debe ofrecer una forma de visualizar el nombre del sensor y un resumen de sus
# mediciones, incluyendo promedio, máximo y mínimo.

# Ejercicio 4 — Sensor y Mediciones (versión simple)

# Ejercicio 4 — Sensor y Mediciones (versión POO y simple)

class Sensor:
    def __init__(self, nombre):
        self.nombre = nombre
        self.mediciones = []

    def agregar_medicion(self, valor):
        self.mediciones.append(valor)
        print("Medición registrada correctamente.")

    def promedio(self):
        if len(self.mediciones) == 0:
            return None
        return sum(self.mediciones) / len(self.mediciones)

    def maximo(self):
        if len(self.mediciones) == 0:
            return None
        return max(self.mediciones)

    def minimo(self):
        if len(self.mediciones) == 0:
            return None
        return min(self.mediciones)

    def mostrar_resumen(self):
        if len(self.mediciones) == 0:
            print("No hay mediciones registradas.")
        else:
            print("\n--- Resumen del Sensor ---")
            print("Nombre del sensor:", self.nombre)
            print("Promedio:", self.promedio())
            print("Máximo:", self.maximo())
            print("Mínimo:", self.minimo())
# Fin del código