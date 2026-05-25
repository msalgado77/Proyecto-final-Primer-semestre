class Reportes:
    def __init__(self, nombre_via: str, fecha: str, estado: str):
        self.nombre_via = nombre_via
        self.fecha = fecha
        self.estado = estado

    def mostrar_informacion(self) -> str:
        return (
            f"Nombre de la vía: {self.nombre_via}\n"
            f"Fecha del reporte: {self.fecha}\n"
            f"Estado: {self.estado}"
        )

    def actualizar_informacion(self, nombre_via: str = None, fecha: str = None, estado: str = None) -> None:
        if nombre_via:
            self.nombre_via = nombre_via
        if fecha:
            self.fecha = fecha
        if estado:
            self.estado = estado

    def enlazar_con_via(self, via_objeto) -> None:
        """
        Enlaza el reporte con una vía específica.
        Recibe un objeto de la clase Vias y muestra su información.
        """
        print("Reporte enlazado con la siguiente vía:")
        print(via_objeto.mostrar_informacion())
