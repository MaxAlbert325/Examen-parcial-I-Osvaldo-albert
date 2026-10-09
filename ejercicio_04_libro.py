class Libro:
    def __init__(self, titulo, autor, disponible):
        self.titulo = titulo
        self.autor = autor
        self.disponible = disponible

    def __str__(self):
        if self.disponible:
            estado = "Disponible"
        else:
            estado = "Prestado"
        return f"Título: {self.titulo}\nAutor: {self.autor}\nEstado: {estado}"


libro1 = Libro("El principito", "Antoine de Saint-Exupéry", True)
libro2 = Libro("Don Quijote de la Mancha", "Miguel de Cervantes", False)

print(libro1)
print()
print(libro2)
