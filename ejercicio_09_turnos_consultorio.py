class Turno:
    def __init__(self, paciente, hora):
        self.paciente = paciente
        self.hora = hora
        self.estado = "Pendiente"

    def marcar_atendido(self):
        self.estado = "Atendido"

    def __str__(self):
        return f"Hora: {self.hora} | Paciente: {self.paciente} | Estado: {self.estado}"


class Agenda:
    def __init__(self):
        self.turnos = []

    def agregar_turno(self, turno):
        self.turnos.append(turno)

    def listar_pendientes(self):
        print("Turnos pendientes:")
        hay_pendientes = False
        for turno in self.turnos:
            if turno.estado == "Pendiente":
                print(turno)
                hay_pendientes = True
        if not hay_pendientes:
            print("No hay turnos pendientes.")

    def __str__(self):
        return f"Agenda del consultorio: {len(self.turnos)} turnos registrados"


agenda = Agenda()
turno1 = Turno("Lucía Fernández", "08:00")
turno2 = Turno("Marcos Ruiz", "08:30")
turno3 = Turno("Sofía Acosta", "09:00")

agenda.agregar_turno(turno1)
agenda.agregar_turno(turno2)
agenda.agregar_turno(turno3)

turno1.marcar_atendido()
turno3.marcar_atendido()

print(agenda)
agenda.listar_pendientes()
