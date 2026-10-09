class Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

    def __str__(self):
        return f"{self.nombre} - {self.precio:,.0f} Gs."


class Item:
    def __init__(self, producto, cantidad):
        self.producto = producto
        self.cantidad = cantidad

    def subtotal(self):
        return self.producto.precio * self.cantidad

    def __str__(self):
        return f"{self.producto.nombre} x {self.cantidad} = {self.subtotal():,.0f} Gs."


class Carrito:
    def __init__(self):
        self.items = []

    def agregar_item(self, producto, cantidad):
        if cantidad <= 0:
            print("La cantidad debe ser positiva.")
            return
        self.items.append(Item(producto, cantidad))

    def calcular_total(self):
        total = 0
        for item in self.items:
            total += item.subtotal()
        return total

    def mostrar_detalle(self):
        print("Detalle de la compra:")
        for item in self.items:
            print(item)
        print(f"Total general: {self.calcular_total():,.0f} Gs.")

    def __str__(self):
        return f"Carrito con {len(self.items)} ítems"


producto1 = Producto("Arroz", 8000)
producto2 = Producto("Aceite", 12000)
producto3 = Producto("Fideos", 5000)

carrito = Carrito()
carrito.agregar_item(producto1, 2)
carrito.agregar_item(producto2, 1)
carrito.agregar_item(producto3, 3)
print(carrito)
carrito.mostrar_detalle()
