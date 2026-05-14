class Prioridad:

    def _init_(self, estado_actual: str, criterios_daños: str, promedio_circulacion: int, promedio_accidentes: int)-> None:

        self.estado = estado_actual
        self.daños = criterios_daños
        self.circulacion = promedio_circulacion
        self.accidentes = promedio_accidentes

    def mostrar_informacion(self) -> str:
       
        return (
            f"Estado de la vía: {self.estado}, "
            f"Promedio de accidentes: {self.accidentes}, "
            f"Promedio de circulación: {self.circulacion},"
            f"Criterios de daños causados a la vía: {self.daños}"
        )




















































































