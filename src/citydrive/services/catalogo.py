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

    def modificar_vehiculo(
        self,
        vehiculo_id: str,
        marca: str,
        modelo: str,
        categoria: str,
        plazas: int,
        capacidad_carga: str,
        transmision: str,
    ) -> Vehiculo:
        if vehiculo_id not in self._vehiculos:
            raise ValueError("No existe ningún vehículo con ese identificador.")

        if not marca.strip():
            raise ValueError("La marca no puede estar vacía.")

        if not modelo.strip():
            raise ValueError("El modelo no puede estar vacío.")

        if not categoria.strip():
            raise ValueError("La categoría no puede estar vacía.")

        if not isinstance(plazas, int) or plazas <= 0:
            raise ValueError("El número de plazas debe ser mayor que cero.")

        if not capacidad_carga.strip():
            raise ValueError("La capacidad de carga no puede estar vacía.")

        if not transmision.strip():
            raise ValueError("La transmisión no puede estar vacía.")

        vehiculo = self._vehiculos[vehiculo_id]

        vehiculo.marca = marca.strip()
        vehiculo.modelo = modelo.strip()
        vehiculo.categoria = categoria.strip()
        vehiculo.plazas = plazas
        vehiculo.capacidad_carga = capacidad_carga.strip()
        vehiculo.transmision = transmision.strip()

        return vehiculo