"""Servicio para procesar la selección de un vehículo y redirigir al formulario de reserva."""

from typing import Dict, Any
from src.models.seleccion_vehiculo import SeleccionVehiculo

_VEHICULOS_CATALOGO = {
    "VEH-01": "DISPONIBLE",
    "VEH-02": "RESERVADO"
}

def seleccionar_vehiculo(id_vehiculo: str, id_usuario: str) -> Dict[str, Any]:
    """Valida la selección de un vehículo disponible y genera la ruta de redirección al formulario."""
    if not id_vehiculo or not id_usuario:
        raise ValueError("Se requieren el identificador del vehículo y del usuario.")

    id_vehiculo_norm = id_vehiculo.strip().upper()
    estado = _VEHICULOS_CATALOGO.get(id_vehiculo_norm)

    if not estado:
        raise ValueError(f"El vehículo '{id_vehiculo}' no existe en el catálogo.")

    if estado != "DISPONIBLE":
        raise ValueError(f"No se puede seleccionar el vehículo '{id_vehiculo_norm}': no se encuentra disponible.")

    seleccion = SeleccionVehiculo(
        id_seleccion=f"SEL-{id_vehiculo_norm}",
        id_vehiculo=id_vehiculo_norm,
        id_usuario=id_usuario.strip(),
        estado_disponibilidad=estado
    )

    return {
        "status": "SELECCION_EXITOSA",
        "redireccion": f"/reservas/formulario?vehiculo={id_vehiculo_norm}",
        "detalle": seleccion.to_dict()
    }

if __name__ == "__main__":
    print("Probando seleccion de vehiculo:")
    print(seleccionar_vehiculo("VEH-01", "USR-99"))