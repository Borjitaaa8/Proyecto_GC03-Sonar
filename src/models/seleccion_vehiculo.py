"""Modelo de datos para la acción de selección de vehículo y redirección a reserva."""

class SeleccionVehiculo:
    def __init__(self, id_vehiculo: str, matricula: str, modelo: str, url_formulario: str, disponible: bool = True):
        self.id_vehiculo = id_vehiculo
        self.matricula = matricula
        self.modelo = modelo
        self.url_formulario = url_formulario
        self.disponible = disponible

    def to_dict(self):
        return {
            "id_vehiculo": self.id_vehiculo,
            "matricula": self.matricula,
            "modelo": self.modelo,
            "url_formulario": self.url_formulario,
            "disponible": self.disponible
        }