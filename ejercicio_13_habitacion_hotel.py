class Habitacion:
    def __init__(self, numero, tipo, tarifa_por_noche):
        self.numero = numero
        self.tipo = tipo
        self.tarifa_por_noche = tarifa_por_noche
        self.ocupada = False

    def ocupar(self):
        if self.ocupada:
            print(f"La habitación {self.numero} ya está ocupada.")
            return
        self.ocupada = True
        print(f"La habitación {self.numero} ahora está ocupada.")

    def liberar(self):
        if not self.ocupada:
            print(f"La habitación {self.numero} ya está libre.")
            return
        self.ocupada = False
        print(f"La habitación {self.numero} quedó libre.")

    def calcular_estadia(self, noches):
        if noches <= 0:
            print("La cantidad de noches debe ser positiva.")
            return 0
        return self.tarifa_por_noche * noches

    def __str__(self):
        if self.ocupada:
            estado = "Ocupada"
        else:
            estado = "Libre"
        return f"Habitación {self.numero} | Tipo: {self.tipo} | Tarifa: {self.tarifa_por_noche:,.0f} Gs./noche | Estado: {estado}"


habitacion1 = Habitacion(101, "Doble", 250000)
habitacion2 = Habitacion(202, "Suite", 450000)

print(habitacion1)
habitacion1.ocupar()
habitacion1.ocupar()
print(habitacion1)
print(f"Costo de 3 noches: {habitacion1.calcular_estadia(3):,.0f} Gs.")
habitacion1.liberar()
print(habitacion1)
print()
print(habitacion2)
