# Importamos todas las clases
from primarias.vias import Vias
from primarias.Prioridad import Prioridad
from primarias.Mantenimientos import Mantenimientos
from secundarias.Presupuesto import Presupuesto
from secundarias.Historial_mantenimiento import Hismantenimiento

print("========================================")
print("=== INTEGRACIÓN TOTAL DEL PROYECTO ===")
print("========================================\n")

# Creamos una Vía

via_principal = Vias(
    "Avenida Central", "Norte", 100.5, 10.5, "Principal", "Asfalto", "15/05/2026"
)

prioridad_avenida = Prioridad("Crítico", "Huecos profundos", 15, 10, via_principal)
prioridad_avenida.asignar_puntaje()

print("------Datos de la Prioridad------")
print(prioridad_avenida.mostrar_informacion())
print("\n")


mantenimiento_avenida = Mantenimientos(5000, 10, ["Asfalto", "Cemento"])

mantenimiento_avenida.emparejar_prioridad(prioridad_avenida)
print("\n")


presupuesto_alcaldia = Presupuesto(15000)
presupuesto_alcaldia.emparejar_con_mantenimientos(mantenimiento_avenida)
print("\n")


historial_avenida = Hismantenimiento("Avenida Central", 15, "Recarpeteo", 7000)

historial_avenida.agregar_registro("Reparación de huecos profundos")
historial_avenida.agregar_registro("Reemplazo de señalización")
historial_avenida.agregar_registro("Recarpeteo con asfalto")


print("------Historial de Mantenimientos------")
print(historial_avenida.mostrar_historial())


print("\n------Datos del mantenimiento------")
print(f"Tiempo desde último mantenimiento: {historial_avenida.tiempo} días")
print(f"Tipo de mantenimiento: {historial_avenida.tipo}")
print(f"Costo total: ${historial_avenida.costo}")
