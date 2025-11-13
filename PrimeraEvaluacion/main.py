# Ejercicio1.py Biblioteca y libros
from Ejercicio1 import Biblioteca
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
#-------------------------------------------------------------------------------------------------------

# Ejercicio 2 — Gestión de Cursos y Alumnos

from Ejercicio2 import Curso

#Ejemplo de uso sistema gestion de cursos y alumnos
    
curso = Curso("Programación Orientada a Objetos")
curso.inscribir_alumno("Michael Arjel")
curso.inscribir_alumno("Benjamin Avendaño")
curso.inscribir_alumno("Edgard Parra")
curso.inscribir_alumno("Lilian Labbé")

print("Estado inicial del curso:")
print(curso.estado_curso())

curso.remover_alumno("Lilian Labbé")

print("Estado después de remover un alumno:")
print(curso.estado_curso())

# Intento de remover alumno no inscrito
curso.remover_alumno("Camila Soto")
print("Estado final del curso:")
print(curso.estado_curso())
#Fin del código
#-------------------------------------------------------------------------------------------------------

# Ejercicio 3 — Gestión de Películas en un Catálogo

from Ejercicio3 import Pedido

pedido = Pedido()
pedido.agregar_item("Camisa", 15990, 2)
pedido.agregar_item("Pantalones", 39990, 1)
pedido.agregar_item("Zapatos", 79990, 1)

print("Detalle del pedido:")
pedido.listar_items()

total = pedido.total_pedido()
print(f"Total a pagar: {total}")
#Fin del código
#-----------------------------------------------------------------------------------------------------

# Ejercicio 4 — Sensor de Mediciones Ambientales

from Ejercicio4 import Sensor
# Probar el sistema de sensor de mediciones ambientales
nombre_sensor = input("Ingrese el nombre del sensor: ")
sensor = Sensor(nombre_sensor)

while True:
    valor = input("Ingrese una medición (o 'fin' para terminar): ")
    if valor.lower() == "fin":
        break
    else:
        sensor.agregar_medicion(float(valor))

sensor.mostrar_resumen()
#Fin del codigo
#-------------------------------------------------------------------------------------------------------

# Ejercicio 5 - Pelicula y Catalogo

from Ejercicio5 import Catalogo

# Ejemplo de uso

catalogo = Catalogo()
catalogo.registrar_pelicula("Dune: Parte Dos", "Ciencia Ficción", 2024)
catalogo.registrar_pelicula("The Batman", "Crimen / Acción", 2022)
catalogo.registrar_pelicula("John Wick 4", "Acción / Crimen", 2023)
catalogo.registrar_pelicula("Tenet", "Ciencia Ficción / Acción", 2020)
catalogo.registrar_pelicula("The Killer", "Crimen / Suspenso", 2023)
catalogo.registrar_pelicula("Rebel Moon: Parte 1", "Ciencia Ficción / Acción", 2023)

print("Catálogo completo:")
catalogo.mostrar_catalogo()

titulo_buscar = "Inception"
pelicula_encontrada = catalogo.buscar_pelicula(titulo_buscar)
if pelicula_encontrada:
    print(f"\nPelícula encontrada: {pelicula_encontrada.informacion()}")
else:
    print(f"\nLa película '{titulo_buscar}' no se encuentra en el catálogo.")

genero_filtrar = "Ciencia Ficción"
peliculas_filtradas = catalogo.filtrar_por_genero(genero_filtrar)
if peliculas_filtradas:
    print(f"\nPelículas del género '{genero_filtrar}':")
    for pelicula in peliculas_filtradas:
        print(pelicula.informacion())
else:
    print(f"\nNo se encontraron películas del género '{genero_filtrar}'.")
#Fin del código
#------------------------------------------------------------------------------------------------------

# Ejercicio 6 - Usuario y Autenticación simple

from Ejercicio6 import SistemaUsuarios

# Modo de uso del sistema de usuarios y autenticación simple
sistema = SistemaUsuarios()

# Registrar usuarios
sistema.registrar_usuario("Lili", "1234")
sistema.registrar_usuario("Juan", "abcd")
sistema.registrar_usuario("Lili", "9999")  # Intento duplicado

# Iniciar sesión
sistema.iniciar_sesion("Lili", "1234")     # Correcto
sistema.iniciar_sesion("Juan", "1234")     # Contraseña incorrecta
sistema.iniciar_sesion("Pedro", "qwerty")  # Usuario no existe

# Consultar si un usuario existe
sistema.usuario_registrado("Juan")
sistema.usuario_registrado("Maria")
#Fin del codigo
#-------------------------------------------------------------------------------------------------------

# Ejercicio 7 - Agenda y Contacto

from Ejercicio7 import Agenda

# Ejemplo de uso agenda y contacto

agenda = Agenda()
print(agenda.agregar_contacto("Lilian Labbé", "1234567890", "lilian@mail.cl"))
print(agenda.agregar_contacto("Benjamin Avendaño", "9876543210", "benjamin@mail.cl"))
print(agenda.agregar_contacto("Lilian Labbé", "1112223333", "lilianl@mail.cl"))
print("\nListado de contactos:")
agenda.mostrar_contactos()
print("\nBúsqueda de contacto 'Lilian Labbé':")
print(agenda.buscar_contacto("Lilian Labbé"))
print("\nBúsqueda de contacto 'Camila Soto':")
print(agenda.buscar_contacto("Camila Soto"))
print("\nEliminación de contacto 'Benjamin Avendaño':")
print(agenda.eliminar_contacto("Benjamin Avendaño"))
print("\nEliminación de contacto 'Camila Soto':")
print(agenda.eliminar_contacto("Camila Soto"))
print("\nListado de contactos actualizado:")
agenda.mostrar_contactos()
#Fin del código y todos los ejercicios
