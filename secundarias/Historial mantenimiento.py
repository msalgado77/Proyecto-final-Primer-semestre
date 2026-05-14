class Hismantenimiento:

    def _init_(self, tiempo_ulmantenimiento: int, tipo_mantenimiento: str, costo_mantenimiento: int)-> None:

        self.tiempo = tiempo_ulmantenimiento
        self.tipo = tipo_mantenimiento
        self.costo = costo_mantenimiento

    def mostrar_informacion(self) -> str:
       
        return (
            f"Tiempo desde el último mantenimiento: {self.tiempo}, "
            f"Tipo de mantenimiento realizado: {self.tipo}, "
            f":Costo del mantenimiento:  {self.costo},"
        )



























































































