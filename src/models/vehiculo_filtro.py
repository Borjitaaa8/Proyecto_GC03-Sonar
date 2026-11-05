"""Modelo representativo del vehículo con información de tipo y categoría de filtrado."""

class VehiculoFiltro:
    def __init__(self, id_vehiculo: str, modelo: str, tipo: str, disponible: bool = True):
        self.id_vehiculo = id_vehiculo
        self.modelo = modelo
        self.tipo = tipo
        self.disponible = disponible

    def to_dict(self):
        return {
            "id_vehiculo": self.id_vehiculo,
            "modelo": self.modelo,
            "tipo": self.tipo,
            "disponible": self.disponible
        }