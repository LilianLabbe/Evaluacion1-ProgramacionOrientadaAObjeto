# buscar una película específica por su título, filtrar el listado para ver solo las películas de un
# determinado género y consultar en cualquier momento el listado completo de todas las películas
# registradas.
# Requerimientos funcionales
# • El sistema debe permitir registrar una nueva película, indicando su título, género y año de
# lanzamiento.
# • El sistema debe permitir consultar el catálogo completo, mostrando todas las películas
# registradas con su información básica.
# • El sistema debe permitir buscar una película por su título, indicando claramente si se encuentra
# en el catálogo y mostrando sus datos.
# • El sistema debe permitir filtrar las películas por género, mostrando solo aquellas que
# correspondan al género solicitado.
# • Si se realiza una búsqueda o filtro y no se encuentran películas, el sistema debe informarlo
# claramente.
# • El sistema debe ofrecer una forma de visualizar el catálogo actualizado después de agregar
# nuevas películas o realizar búsquedas y filtros.

class Pelicula:
    def __init__(self, titulo, genero, anio_lanzamiento):
        self.titulo = titulo
        self.genero = genero
        self.anio_lanzamiento = anio_lanzamiento
    def informacion(self):
        return f"Título: {self.titulo}, Género: {self.genero}, Año de lanzamiento: {self.anio_lanzamiento}"
class Catalogo:
    def __init__(self):
        self.peliculas = []
    def registrar_pelicula(self, titulo, genero, anio_lanzamiento):
        pelicula = Pelicula(titulo, genero, anio_lanzamiento)
        self.peliculas.append(pelicula)
    def mostrar_catalogo(self):
        if not self.peliculas:
            print("El catálogo está vacío.")
            return
        for pelicula in self.peliculas:
            print(pelicula.informacion())
    def buscar_pelicula(self, titulo):
        for pelicula in self.peliculas:
            if pelicula.titulo.lower() == titulo.lower():
                return pelicula
        return None
    def filtrar_por_genero(self, genero):
        peliculas_filtradas = [pelicula for pelicula in self.peliculas if pelicula.genero.lower() == genero.lower()]
        return peliculas_filtradas
#Fin del código del ejercicio 