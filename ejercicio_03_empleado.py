class Empleado:
    def __init__(self, nombre, cargo, salario_mensual):
        self.nombre = nombre
        self.cargo = cargo
        self.salario_mensual = salario_mensual

    def salario_anual(self):
        # Se incluye un mes adicional como aguinaldo.
        return self.salario_mensual * 13

    def __str__(self):
        return f"Empleado: {self.nombre}\nCargo: {self.cargo}\nSalario mensual: {self.salario_mensual:,.0f} Gs."


empleado1 = Empleado("María López", "Cajera", 2800000)
empleado2 = Empleado("Juan Benítez", "Encargado", 4200000)

for empleado in [empleado1, empleado2]:
    print(empleado)
    print(f"Salario anual con aguinaldo: {empleado.salario_anual():,.0f} Gs.\n")
