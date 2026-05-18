class Presupuesto:
    def __init__(self, cantidad_disponible_inicial):
        self.cantidad_disponible = cantidad_disponible_inicial
        self.cantidad_asignada = 0
    
    # Muestra saldos actuales en pantalla    
    def mostrar_informacion(self):
        print("----------Estado del Presupuesto----------")
        print(f"Cantidad disponble {self.cantidad_disponible}")
        print(f"Cantidad asiganada a obras {self.cantidad_asignada}")
        
    def actualizar_informacion(self, nueva_cantidad):
        self.cantidad_disponible = nueva_cantidad
        print("Presupuesto actualizado!"
              f"Nueva cantidad ${self.cantidad_disponible}")
        
    # Conectamos Presupuesto con Mantenimientos
    def emparejar_con_mantenimientos(self, objeto_mantenimiento):
        dinero_necesario = objeto_mantenimiento.presupuesto
        self.cantidad_asignada = dinero_necesario
        print(f"Se han asignado ${self.cantidad_asignada}"
              "para el Mantenimiento")
        