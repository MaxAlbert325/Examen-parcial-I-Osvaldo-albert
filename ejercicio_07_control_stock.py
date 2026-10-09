class Producto:
    def __init__(self, nombre, precio, stock, stock_minimo):
        self.nombre = nombre
        self.precio = precio
        self.stock = stock
        self.stock_minimo = stock_minimo

    def ingresar_mercaderia(self, cantidad):
        if cantidad <= 0:
            print("La cantidad a ingresar debe ser positiva.")
            return
        self.stock += cantidad
        print(f"Se ingresaron {cantidad} unidades de {self.nombre}.")
        self.verificar_stock()

    def registrar_venta(self, cantidad):
        if cantidad <= 0:
            print("La cantidad vendida debe ser positiva.")
        elif cantidad > self.stock:
            print("Venta rechazada: no hay unidades suficientes.")
        else:
            self.stock -= cantidad
            print(f"Venta registrada: {cantidad} unidades de {self.nombre}.")
            self.verificar_stock()

    def verificar_stock(self):
        if self.stock < self.stock_minimo:
            print(f"ALERTA: el stock de {self.nombre} está por debajo del mínimo ({self.stock_minimo}).")

    def __str__(self):
        return f"Producto: {self.nombre} | Precio: {self.precio:,.0f} Gs. | Stock: {self.stock} | Mínimo: {self.stock_minimo}"


producto = Producto("Leche", 7000, 12, 5)
print(producto)
producto.registrar_venta(8)
print(producto)
producto.ingresar_mercaderia(10)
print(producto)
