"""Servicio para aplicar filtros por tipo de vehículo y restaurar la lista completa."""

from typing import List, Dict, Any
from src.models.vehiculo_filtro import VehiculoFiltro

_FLOTA = [
    VehiculoFiltro("VEH-01", "Toyota Yaris", "SUV", True),
    VehiculoFiltro("VEH-02", "Renault Clio", "SEDAN", True),
    VehiculoFiltro("VEH-03", "Nissan Qashqai", "SUV", True),
    VehiculoFiltro("VEH-04", "Peugeot 208", "COMPACTO", False)
]

def filtrar_por_tipo(tipo: str) -> List[Dict[str, Any]]:
    """Filtra el catálogo por tipo de vehículo. Si el filtro es nulo o vacío, restaura la lista."""
    if not tipo or not tipo.strip() or tipo.strip().upper() == "TODOS":
        return [v.to_dict() for v in _FLOTA]

    tipo_norm = tipo.strip().upper()
    return [v.to_dict() for v in _FLOTA if v.tipo == tipo_norm]

if __name__ == "__main__":
    print("Probando filtro de vehiculos:")
    print("Filtro SUV:", filtrar_por_tipo("SUV"))
    print("Restaurar lista:", len(filtrar_por_tipo("TODOS")))