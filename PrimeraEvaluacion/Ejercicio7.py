# Ejercicio 7 — Agenda y Contacto
# Diseñe un sistema sencillo para gestionar una agenda de contactos. Cada contacto debe estar
# identificado por un nombre, un número de teléfono y un correo electrónico. La agenda debe
# permitir registrar nuevos contactos, buscar un contacto específico, eliminar contactos existentes y
# consultar en cualquier momento el listado completo de las personas almacenadas.
# Requerimientos funcionales
# • El sistema debe permitir agregar un nuevo contacto, indicando nombre, teléfono y correo
# electrónico.
# • El sistema debe permitir consultar el listado completo de contactos, mostrando los datos
# principales de cada uno.
# • El sistema debe permitir buscar un contacto por su nombre, mostrando su información si
# existe en la agenda.
# • El sistema debe permitir eliminar un contacto de la agenda, usando su nombre u otro dato
# identificador.
# • Si se intenta buscar o eliminar un contacto que no existe, el sistema debe informarlo
# claramente.
# • El sistema debe ofrecer una forma de visualizar el estado actualizado de la agenda después
# de agregar, eliminar o buscar contactos

class Contacto:
    def __init__(self, nombre, telefono, correo):
        self.nombre = nombre
        self.telefono = telefono
        self.correo = correo

    def informacion(self):
        return f"Nombre: {self.nombre}, Teléfono: {self.telefono}, Correo: {self.correo}"
class Agenda:
    def __init__(self):
        self.contactos = {}

    def agregar_contacto(self, nombre, telefono, correo):
        if nombre in self.contactos:
            return f"Error: Este contacto '{nombre}' ya existe."
        self.contactos[nombre] = Contacto(nombre, telefono, correo)
        return f"Contacto '{nombre}' agregado correctamentw."

    def mostrar_contactos(self):
        if not self.contactos:
            print("La agenda está vacía.")
            return
        for contacto in self.contactos.values():
            print(contacto.informacion())

    def buscar_contacto(self, nombre):
        contacto = self.contactos.get(nombre)
        if contacto:
            return contacto.informacion()
        else:
            return f"Error: El contacto '{nombre}' no existe."

    def eliminar_contacto(self, nombre):
        if nombre in self.contactos:
            del self.contactos[nombre]
            return f"Contacto '{nombre}' eliminado exitosamente."
        else:
            return f"Error: El contacto '{nombre}' no existe."
#Fin del codigo del ejercicio 7