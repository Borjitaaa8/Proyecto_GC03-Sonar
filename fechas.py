
from dataclasses import dataclass
from datetime import date


@dataclass
class RangoFechas:
    fecha_inicio: date | None = None
    fecha_fin: date | None = None
