class Hismantenimiento:

    def __init__(
        self,
        via: str,
        tiempo_ulmantenimiento: int,
        tipo_mantenimiento: str,
        costo_mantenimiento: int,
    ):
        self.via = via
        self.tiempo = tiempo_ulmantenimiento
        self.tipo = tipo_mantenimiento
        self.costo = costo_mantenimiento
        self.registros = []

    def agregar_registro(self, descripcion):
        self.registros.append(descripcion)

    def mostrar_historial(self):
        historial = "Historial de mantenimientos:\n"
        for i, registro in enumerate(self.registros, start=1):
            historial += f"{i}. {registro}\n"
        return historial



    def mostrar_informacion(self) -> str:

        return (
            f"Tiempo desde el último mantenimiento: {self.tiempo}, "
            f"Tipo de mantenimiento realizado: {self.tipo}, "
            f":Costo del mantenimiento:  {self.costo},"
        )

    def actualizar_informacion(
        self,
        tiempo_ulmantenimiento: int,
        tipo_mantenimiento: str,
        costo_mantenimiento: int,
    ) -> None:

        self.tiempo = tiempo_ulmantenimiento
        self.tipo = tipo_mantenimiento
        self.costo = costo_mantenimiento
