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

    def consultar_catalogo(self) -> list[dict]:
        catalogo = []

        for vehiculo in self._vehiculos.values():
            catalogo.append(
                {
                    "id": vehiculo.id,
                    "marca": vehiculo.marca,
                    "modelo": vehiculo.modelo,
                    "categoria": vehiculo.categoria,
                    "plazas": vehiculo.plazas,
                    "capacidad_carga": vehiculo.capacidad_carga,
                    "transmision": vehiculo.transmision,
                    "estado_operativo": vehiculo.estado_operativo,
                }
            )

        return catalogo