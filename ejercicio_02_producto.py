class Producto:
    def __init__(self, nombre, precio, cantidad):
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad

    def valor_total(self):
        return self.precio * self.cantidad

    def __str__(self):
        return f"Producto: {self.nombre}\nPrecio unitario: {self.precio:,.0f} Gs.\nStock: {self.cantidad} unidades"


producto1 = Producto("Arroz", 8000, 15)
producto2 = Producto("Aceite", 12000, 10)
producto3 = Producto("Azúcar", 6500, 20)

for producto in [producto1, producto2, producto3]:
    print(producto)
    print(f"Valor total en stock: {producto.valor_total():,.0f} Gs.\n")
