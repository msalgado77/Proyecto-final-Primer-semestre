from primarias.vias import Vias


class Prioridad:

    def __init__(
        self,
        estado_actual: str,
        criterios_daños: str,
        promedio_circulacion: int,
        promedio_accidentes: int,
        via: Vias,
    ) -> None:

        self.via = via
        self.estado = estado_actual
        self.daños = criterios_daños
        self.circulacion = promedio_circulacion
        self.accidentes = promedio_accidentes
        self.puntaje_prioridad = 0

    def mostrar_informacion(self) -> str:
        return (
            f"Vía: {self.via.nombre}\n"
            f"Estado de la vía: {self.estado}\n"
            f"Promedio de accidentes: {self.accidentes}\n"
            f"Promedio de circulación: {self.circulacion}\n"
            f"Criterios de daños causados a la vía: {self.daños}"
        )

    def actualizar_informacion(
        self,
        estado_actual: str,
        criterios_daños: str,
        promedio_circulacion: int,
        promedio_accidentes: int,
    ) -> None:
        self.estado = estado_actual
        self.daños = criterios_daños
        self.circulacion = promedio_circulacion
        self.accidentes = promedio_accidentes
        self.asignar_puntaje()

    def asignar_puntaje(self) -> None:
        self.puntaje_prioridad = self.accidentes + self.circulacion

    def comparar_prioridad(self, otra_prioridad: "Prioridad") -> str:
        if self.puntaje_prioridad > otra_prioridad.puntaje_prioridad:
            return f"La via {self.via} tiene mayor prioridad."
        elif self.puntaje_prioridad < otra_prioridad.puntaje_prioridad:
            return f"La via {otra_prioridad.via} tiene mayor prioridad."
        else:
            return "Ambas vías tienen la misma prioridad."
