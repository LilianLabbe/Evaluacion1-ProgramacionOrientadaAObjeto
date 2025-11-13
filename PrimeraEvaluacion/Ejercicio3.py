# Ejercicio 3 — Pedido e Ítem
# Diseñe un sistema sencillo para gestionar un pedido de compra. Cada ítem del pedido debe tener un
# nombre, un precio y una cantidad, y debe ser capaz de calcular su propio subtotal (precio por cantidad).
# El pedido debe permitir registrar varios ítems y ofrecer una forma de calcular el monto total a pagar
# sumando los subtotales de todos los ítems incluidos.
# • El sistema debe permitir registrar un nuevo ítem indicando su nombre, precio y cantidad.
# • El sistema debe permitir calcular el subtotal de un ítem, multiplicando su precio por la cantidad.
# • El sistema debe permitir agregar ítems a un pedido, de modo que un mismo pedido pueda
# contener varios ítems distintos.
# • El sistema debe permitir consultar el listado de ítems de un pedido, mostrando al menos el
# nombre, el precio, la cantidad y el subtotal de cada uno.
# • El sistema debe permitir calcular el total del pedido, sumando los subtotales de todos los ítems
# registrados.
# • El sistema debe ofrecer una forma de visualizar el total final a pagar junto con el detalle de los
# ítems que lo componen.

class Item:
    def __init__(self, nombre, precio, cantidad):
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad

    def subtotal(self):
        return self.precio * self.cantidad
class Pedido:
    def __init__(self):
        self.items = []

    def agregar_item(self, nombre, precio, cantidad):
        item = Item(nombre, precio, cantidad)
        self.items.append(item)

    def listar_items(self):
        for item in self.items:
            print(f"Nombre: {item.nombre}, Precio: {item.precio}, Cantidad: {item.cantidad}, Subtotal: {item.subtotal()}")

    def total_pedido(self):
        return sum(item.subtotal() for item in self.items)
# Fin del codigo