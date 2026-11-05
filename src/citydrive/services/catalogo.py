from citydrive.models.vehiculo import Vehiculo


class CatalogoVehiculos:
    def __init__(self):
        self._vehiculos: dict[str, Vehiculo] = {}

    def registrar_vehiculo(
        self,
        marca: str,
        modelo: str,
        categoria: str,
        plazas: int,
        capacidad_carga: str,
        transmision: str,
    ) -> Vehiculo:
        vehiculo = Vehiculo(
            marca=marca,
            modelo=modelo,
            categoria=categoria,
            plazas=plazas,
            capacidad_carga=capacidad_carga,
            transmision=transmision,
        )

        if vehiculo.id in self._vehiculos:
            raise ValueError("Ya existe un vehículo con ese identificador.")

        self._vehiculos[vehiculo.id] = vehiculo
        return vehiculo

    def obtener_vehiculos(self) -> list[Vehiculo]:
        return list(self._vehiculos.values())

    def cambiar_estado_vehiculo(
        self,
        vehiculo_id: str,
        nuevo_estado: str,
    ) -> Vehiculo:
        if vehiculo_id not in self._vehiculos:
            raise ValueError("No existe ningún vehículo con ese identificador.")

        if nuevo_estado not in ("disponible", "no disponible"):
            raise ValueError(
                "El estado debe ser 'disponible' o 'no disponible'."
            )

        vehiculo = self._vehiculos[vehiculo_id]
        vehiculo.estado_operativo = nuevo_estado

        return vehiculo