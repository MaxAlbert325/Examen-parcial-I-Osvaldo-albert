class CuentaCorriente:
    def __init__(self, cliente, saldo=0):
        self.cliente = cliente
        self.saldo = saldo

    def acreditar(self, monto):
        if monto <= 0:
            print("El monto a acreditar debe ser positivo.")
            return
        self.saldo += monto
        print(f"Se acreditaron {monto:,.0f} Gs.")

    def registrar_consumo(self, monto):
        if monto <= 0:
            print("El consumo debe ser un monto positivo.")
        elif monto > self.saldo:
            print("Compra rechazada: saldo insuficiente.")
        else:
            self.saldo -= monto
            print(f"Compra registrada por {monto:,.0f} Gs.")

    def __str__(self):
        return f"Cuenta de {self.cliente} | Saldo: {self.saldo:,.0f} Gs."


cuenta = CuentaCorriente("Pedro Ramírez", 100000)
print(cuenta)
cuenta.acreditar(50000)
print(cuenta)
cuenta.registrar_consumo(80000)
print(cuenta)
cuenta.registrar_consumo(100000)
print(cuenta)
