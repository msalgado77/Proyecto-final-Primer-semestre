class Mantenimientos:
    def __init__(self, presupuesto, tiempo_inicial, materiales_iniciales):
        self.presupuesto = presupuesto
        self.tiempo = tiempo_inicial
        self.materiales = materiales_iniciales

        # Empieza vacio porque al principio no falta nada.
        self.materiales_faltantes = []

    # Mostramos la informacion en la pantalla
    def mostrar_informacion(self):
        print("----------Estado del Mantenimiento----------")
        print(f"Presupuesto asignado ${self.presupuesto}")
        print(f"Tiempo estimado {self.tiempo_inicial} días")
        print(f"Materiales listos {self.materiales}")
        print(f"Materiales faltantes {self.materiales_faltantes}")

    def actualizar_informacion(self, nuevo_presupuesto, nuevo_tiempo,
                               nuevos_materiales):
        self.presupuesto = nuevo_presupuesto
        self.tiempo = nuevo_tiempo
        self.materiales = nuevos_materiales
        print("La información del Mantenimiento a sido actualizada con éxito!")
