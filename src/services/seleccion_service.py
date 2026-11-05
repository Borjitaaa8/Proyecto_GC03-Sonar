"""Servicio para procesar la acción de selección de vehículo y redirigir al formulario de reserva."""

from typing import Dict, Any
from src.models.seleccion_vehiculo import SeleccionVehiculo

# Simulación de catálogo de AutoRent en memoria
_CATALOGO_AUTORENT = {
    "VEH-01": {"matricula": "1111-AAA", "modelo": "Seat Ibiza", "disponible": True},
    "VEH-02": {"matricula": "2222-BBB", "modelo": "Ford Focus", "disponible": False},
    "VEH-03": {"matricula": "3333-CCC", "modelo": "Renault Clio", "disponible": True}
}

def seleccionar_vehiculo_para_reserva(id_vehiculo: str) -> Dict[str, Any]:
    """Valida la selección del vehículo y genera el enlace de redirección al formulario de reserva."""
    if not id_vehiculo or not id_vehiculo.strip():
        raise ValueError("El identificador del vehículo es obligatorio para realizar la selección.")

    id_normalizado = id_vehiculo.strip().upper()
    vehiculo = _CATALOGO_AUTORENT.get(id_normalizado)

    if not vehiculo:
        raise ValueError(f"El vehículo con identificador '{id_vehiculo}' no existe en AutoRent.")

    if not vehiculo["disponible"]:
        raise ValueError(f"El vehículo '{vehiculo['modelo']}' no está disponible para selección.")

    # Generación de la URL de redirección al formulario con el vehículo preseleccionado
    url_destino = f"/reservas/formulario?id_vehiculo={id_normalizado}"

    seleccion = SeleccionVehiculo(
        id_vehiculo=id_normalizado,
        matricula=vehiculo["matricula"],
        modelo=vehiculo["modelo"],
        url_formulario=url_destino,
        disponible=True
    )

    return {
        "status": "SELECCIONADO",
        "redireccion": seleccion.url_formulario,
        "datos": seleccion.to_dict()
    }

if __name__ == "__main__":
    print("Probando acción de selección de vehículo:")
    res_valido = seleccionar_vehiculo_para_reserva("VEH-01")
    print(f"Selección válida: {res_valido}")

    try:
        seleccionar_vehiculo_para_reserva("VEH-02")
    except ValueError as e:
        print(f"Control de selección no disponible superado: {e}")