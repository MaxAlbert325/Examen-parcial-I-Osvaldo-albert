class Cliente:
    def __init__(self, nombre, cedula, telefono):
        self.nombre = nombre
        self.cedula = cedula
        self.telefono = telefono

    def __str__(self):
        return f"Ficha del cliente\nNombre: {self.nombre}\nCédula: {self.cedula}\nTeléfono: {self.telefono}"


cliente1 = Cliente("Ana Gómez", "1234567", "0981123456")
cliente2 = Cliente("Carlos Pérez", "7654321", "0972123456")

print(cliente1)
print()
print(cliente2)
