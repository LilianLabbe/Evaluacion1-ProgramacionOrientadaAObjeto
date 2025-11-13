# Ejercicio 1 — Libro y Biblioteca
# Diseña un sistema sencillo para gestionar una biblioteca. Cada libro debe tener identificados su título,
# autor y la cantidad de copias disponibles. La biblioteca debe permitir registrar nuevos libros, entregar
# libros en préstamo a los usuarios, recibir devoluciones y mostrar en cualquier momento el estado
# completo del catálogo (qué libros hay y cuántas copias quedan disponibles).
# Requerimientos funcionales
# • El sistema debe permitir registrar un nuevo libro, indicando su título, autor y número de copias
# disponibles.
# • El sistema debe permitir consultar el catálogo completo, mostrando todos los libros registrados
# junto con sus copias disponibles.
# • El sistema debe permitir buscar un libro por título para verificar si existe en la biblioteca y
# cuántas copias quedan.
# • El sistema debe permitir registrar el préstamo de un libro, disminuyendo en una unidad la
# cantidad de copias disponibles.
# • Si se intenta prestar un libro sin copias disponibles, el sistema debe informarlo claramente y no
# realizar el préstamo.
# • El sistema debe permitir registrar la devolución de un libro, aumentando en una unidad la
# cantidad de copias disponibles.
# • El sistema debe ofrecer una forma de visualizar el estado actualizado de un libro específico
# (título, autor, copias disponibles) después de préstamos y devoluciones.

class Libro:
    def __init__(self, titulo, autor, copias_disponibles):
        self.titulo = titulo
        self.autor = autor
        self.copias_disponibles = copias_disponibles

    def prestar(self):
        if self.copias_disponibles > 0:
            self.copias_disponibles -= 1
            return True
        else:
            return False

    def devolver(self):
        self.copias_disponibles += 1

    def estado(self):
        return f"Título: {self.titulo}, Autor: {self.autor}, Copias disponibles: {self.copias_disponibles}"
class Biblioteca:
    def __init__(self):
        self.catalogo = {}

    def registrar_libro(self, titulo, autor, copias_disponibles):
        if titulo not in self.catalogo:
            self.catalogo[titulo] = Libro(titulo, autor, copias_disponibles)
        else:
            self.catalogo[titulo].copias_disponibles += copias_disponibles

    def mostrar_catalogo(self):
        for libro in self.catalogo.values():
            print(libro.estado())

    def buscar_libro(self, titulo):
        return self.catalogo.get(titulo, None)

    def prestar_libro(self, titulo):
        libro = self.buscar_libro(titulo)
        if libro:
            if libro.prestar():
                print(f"Su prestamo se ha realizado con exito, ya puedes llevar tu libro a casa!!'{titulo}'.")
            else:
                print(f"El libro no se encuentra disponible en estos momentos'{titulo}'.")
        else:
            print(f"El libro '{titulo}' no lo tenemos en la biblioteca, disculpe las molestias.")

    def devolver_libro(self, titulo):
        libro = self.buscar_libro(titulo)
        if libro:
            libro.devolver() 
            print(f"La devolución de su libro fue exitosa, '{titulo}'.")
        else:
            print(f"El libro '{titulo}' no está registrado en la biblioteca, lamentamos el inconveniente!!.")
    def estado_libro(self, titulo):
        libro = self.buscar_libro(titulo)
        if libro:
            print(libro.estado())
        else:            
            print(f"El libro '{titulo}' no está registrado en la biblioteca, disculpe las molestias!!.")
#Fin del código


biblioteca=Biblioteca()
#Registro de libros
biblioteca.registrar_libro("1984", "George Orwell", 5)  
biblioteca.registrar_libro("Renegados", "Marissa Meyer", 3)
biblioteca.registrar_libro("Alas de sangre", "Rebecca Yarros", 4)

#catalogo inicial de los libros en biblioteca
print("Catálogo inicial:")
biblioteca.mostrar_catalogo()

biblioteca.prestar_libro("Renegados")
biblioteca.prestar_libro("Renegados")
biblioteca.prestar_libro("Renegados")
biblioteca.prestar_libro("Renegados") # Intento de préstamo sin copias disponibles

#estado de los prestamos de libros
print("\nEstado después de préstamos:")
biblioteca.estado_libro("Renegados")

#devolucion de libros
biblioteca.devolver_libro("Renegados")

print("\nEstado después de devolución:")
biblioteca.estado_libro("Renegados")

#Catalogo final de la biblioteca y sus libros
print("\nCatálogo final:")
biblioteca.mostrar_catalogo()  
#Fin del código