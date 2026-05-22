class Vias:
    def __init__(self, nombre_via: str, ubicacion_via: str, largo_via: float, ancho_via: float,
                 tipo_via: str, material_via: str, fecha_mantenimiento: str):
        self.nombre = nombre_via
        self.ubicacion = ubicacion_via
        self.largo = largo_via
        self.ancho = ancho_via
        self.tipo = tipo_via
        self.material = material_via
        self.ultimo_mantenimiento = fecha_mantenimiento

    def mostrar_informacion(self) -> str:
        return (
            f"Nombre: {self.nombre}\n"
            f"Ubicación: {self.ubicacion}\n"
            f"Largo: {self.largo} m\n"
            f"Ancho: {self.ancho} m\n"
            f"Tipo de vía: {self.tipo}\n"
            f"Material: {self.material}\n"
            f"Último mantenimiento: {self.ultimo_mantenimiento}"
        )

    def actualizar_informacion(self, nombre: str = None, ubicacion: str = None, largo: float = None,
                               ancho: float = None, tipo: str = None, material: str = None,
                               fecha_mantenimiento: str = None) -> None:
        if nombre:
            self.nombre = nombre
        if ubicacion:
            self.ubicacion = ubicacion
        if largo:
            self.largo = largo
        if ancho:
            self.ancho = ancho
        if tipo:
            self.tipo = tipo
        if material:
            self.material = material
        if fecha_mantenimiento:
            self.ultimo_mantenimiento = fecha_mantenimiento
