class CuentaServicio:
    def __init__(self, cliente, gigabytes_incluidos):
        self.cliente = cliente
        self.gigabytes_incluidos = gigabytes_incluidos
        self.gigabytes_consumidos = 0

    def registrar_consumo(self, gigabytes):
        if gigabytes <= 0:
            print("El consumo debe ser mayor que cero.")
            return
        disponibles = self.gigabytes_disponibles()
        if disponibles <= 0:
            print("El paquete de datos ya se agotó.")
            return
        if gigabytes > disponibles:
            print(f"Solo quedan {disponibles:.2f} GB. No se puede registrar ese consumo.")
            return
        self.gigabytes_consumidos += gigabytes
        print(f"Consumo registrado: {gigabytes:.2f} GB.")
        if self.gigabytes_disponibles() == 0:
            print("Aviso: el paquete de datos se agotó.")

    def gigabytes_disponibles(self):
        return self.gigabytes_incluidos - self.gigabytes_consumidos

    def __str__(self):
        return f"Línea de {self.cliente} | Plan: {self.gigabytes_incluidos:.2f} GB | Consumidos: {self.gigabytes_consumidos:.2f} GB | Disponibles: {self.gigabytes_disponibles():.2f} GB"


cuenta = CuentaServicio("Diego Martínez", 10)
print(cuenta)
cuenta.registrar_consumo(3.5)
print(cuenta)
cuenta.registrar_consumo(6.5)
print(cuenta)
cuenta.registrar_consumo(1)
print(cuenta)
