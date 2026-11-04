from dataclasses import dataclass
from datetime import date


@dataclass
class Reserva:
    vehiculo_id: str
    fecha_inicio: date
    fecha_fin: date
    estado: str = "activa"


def fechas_se_solapan(
    inicio_1: date,
    fin_1: date,
    inicio_2: date,
    fin_2: date,
) -> bool:
    if inicio_1 > fin_1 or inicio_2 > fin_2:
        raise ValueError("La fecha de inicio no puede ser posterior a la fecha de fin.")

    return inicio_1 <= fin_2 and inicio_2 <= fin_1


def vehiculo_disponible(
    vehiculo_id: str,
    fecha_inicio: date,
    fecha_fin: date,
    reservas: list[Reserva],
) -> bool:
    if fecha_inicio > fecha_fin:
        raise ValueError("La fecha de inicio no puede ser posterior a la fecha de fin.")

    for reserva in reservas:
        if reserva.vehiculo_id != vehiculo_id:
            continue

        if reserva.estado != "activa":
            continue

        if fechas_se_solapan(
            fecha_inicio,
            fecha_fin,
            reserva.fecha_inicio,
            reserva.fecha_fin,
        ):
            return False

    return True