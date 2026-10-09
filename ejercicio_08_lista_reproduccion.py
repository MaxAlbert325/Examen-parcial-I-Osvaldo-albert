class Cancion:
    def __init__(self, titulo, artista, duracion):
        self.titulo = titulo
        self.artista = artista
        self.duracion = duracion  # Duración en segundos

    def __str__(self):
        minutos = self.duracion // 60
        segundos = self.duracion % 60
        return f"{self.titulo} - {self.artista} ({minutos}:{segundos:02d})"


class ListaReproduccion:
    def __init__(self, nombre):
        self.nombre = nombre
        self.canciones = []

    def agregar_cancion(self, cancion):
        self.canciones.append(cancion)

    def duracion_total(self):
        total = 0
        for cancion in self.canciones:
            total += cancion.duracion
        return total

    def __str__(self):
        texto = f"Lista de reproducción: {self.nombre}\n"
        for cancion in self.canciones:
            texto += f"- {cancion}\n"
        total = self.duracion_total()
        texto += f"Duración total: {total // 60}:{total % 60:02d}"
        return texto


lista = ListaReproduccion("Mis favoritas")
lista.agregar_cancion(Cancion("Canción 1", "Artista A", 210))
lista.agregar_cancion(Cancion("Canción 2", "Artista B", 185))
lista.agregar_cancion(Cancion("Canción 3", "Artista C", 240))
print(lista)
