"""Modelo de datos para la acción de selección de vehículo."""

from datetime import datetime

class SeleccionVehiculo:
    def __init__(self, id_seleccion: str, id_vehiculo: str, id_usuario: str, estado_disponibilidad: str, fecha_seleccion: str = None):
        self.id_seleccion = id_seleccion
        self.id_vehiculo = id_vehiculo
        self.id_usuario = id_usuario
        self.estado_disponibilidad = estado_disponibilidad
        self.fecha_seleccion = fecha_seleccion if fecha_seleccion else datetime.now().isoformat()

    def to_dict(self):
        return {
            "id_seleccion": self.id_seleccion,
            "id_vehiculo": self.id_vehiculo,
            "id_usuario": self.id_usuario,
            "estado_disponibilidad": self.estado_disponibilidad,
            "fecha_seleccion": self.fecha_seleccion
        }