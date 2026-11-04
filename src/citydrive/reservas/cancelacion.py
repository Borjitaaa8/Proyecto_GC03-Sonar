from dataclasses import dataclass


@dataclass
class Reserva:
    referencia: str
    estado: str = "activa"


def cancelar_reserva(reserva: Reserva) -> Reserva:
    if reserva.estado != "activa":
        raise ValueError("Solo se puede cancelar una reserva activa.")

    reserva.estado = "cancelada"
    return reserva