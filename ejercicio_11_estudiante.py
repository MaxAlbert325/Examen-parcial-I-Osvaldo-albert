class Estudiante:
    def __init__(self, nombre, nota_minima=2):
        self.nombre = nombre
        self.notas = {}
        self.nota_minima = nota_minima

    def registrar_nota(self, materia, nota):
        if nota < 1 or nota > 5:
            print("La nota debe estar entre 1 y 5.")
            return
        self.notas[materia] = nota

    def calcular_promedio(self):
        if len(self.notas) == 0:
            return 0
        suma = 0
        for nota in self.notas.values():
            suma += nota
        return suma / len(self.notas)

    def esta_aprobado(self):
        return len(self.notas) > 0 and self.calcular_promedio() >= self.nota_minima

    def __str__(self):
        texto = f"Boletín de {self.nombre}\n"
        for materia, nota in self.notas.items():
            texto += f"{materia}: {nota}\n"
        texto += f"Promedio: {self.calcular_promedio():.2f}\n"
        if self.esta_aprobado():
            texto += "Condición: Aprobado"
        else:
            texto += "Condición: No aprobado"
        return texto


estudiante = Estudiante("Camila González")
estudiante.registrar_nota("Matemática", 4)
estudiante.registrar_nota("Informática", 5)
estudiante.registrar_nota("Comunicación", 3)
print(estudiante)
