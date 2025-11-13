# Ejercicio 6 — Usuario y Autenticación simple
# Diseñe un sistema sencillo de autenticación de usuarios. Cada usuario debe estar identificado por un
# nombre de usuario y una contraseña. El sistema debe permitir registrar nuevos usuarios y,
# posteriormente, validar sus credenciales cuando intenten iniciar sesión, indicando claramente si el
# acceso es aceptado o rechazado.
# Requerimientos funcionales
# • El sistema debe permitir registrar un nuevo usuario, indicando nombre de usuario y
# contraseña.
# • El sistema debe impedir registrar un nombre de usuario que ya exista, informando claramente
# la situación.
# • El sistema debe permitir iniciar sesión (login) solicitando nombre de usuario y contraseña.
# • Al intentar iniciar sesión, el sistema debe validar las credenciales y:
# o Autorizar el acceso si el usuario existe y la contraseña coincide.
# o Rechazar el acceso si el usuario no existe o la contraseña es incorrecta, informando el
# motivo de forma clara.
# • El sistema debe permitir consultar si un usuario está registrado, usando su nombre de usuario.
# • El sistema debe ofrecer una forma de mostrar un mensaje de resultado después de cada
# # intento de registro o login, indicando si la operación fue exitosa o no.

# Ejercicio 6 — Usuario y Autenticación simple (versión fácil y limpia)

class SistemaUsuarios:
    def __init__(self):
        self.usuarios = {}  # Guarda los usuarios y contraseñas en un diccionario

    def registrar_usuario(self, nombre, contraseña):
        if nombre in self.usuarios:
            print("El nombre de usuario ya existe.")
        else:
            self.usuarios[nombre] = contraseña
            print("Usuario registrado correctamente.")

    def iniciar_sesion(self, nombre, contraseña):
        if nombre not in self.usuarios:
            print("Usuario no registrado.")
        elif self.usuarios[nombre] != contraseña:
            print("Contraseña incorrecta.")
        else:
            print("Acceso permitido. Bienvenido,", nombre + "!")

    def usuario_registrado(self, nombre):
        if nombre in self.usuarios:
            print("El usuario está registrado.")
        else:
            print("El usuario no existe.")
#Fin del codigo del ejercicio