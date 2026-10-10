# EP-004 — Control de disponibilidad y conflictos

**Goals:** G-01, G-02, G-03  
**Baseline:** Catálogo V0 - Semana 2

## Boundary

Esta épica incluye el bloqueo del vehículo durante las fechas reservadas, la prevención de reservas que se solapen sobre un mismo vehículo y la gestión del caso en el que un vehículo deje de estar disponible mientras un usuario está realizando una reserva.

Quedan fuera los sistemas externos de sincronización de flotas y cualquier integración con hardware o dispositivos IoT.

## Epic outcome

Garantizar que las reservas registradas sean coherentes con la disponibilidad real de la flota y evitar que un mismo vehículo pueda quedar reservado simultáneamente para periodos incompatibles.

## Stories

### US-011 — Bloquear el vehículo para las fechas reservadas

> Como sistema, quiero marcar como no disponible un vehículo durante las fechas de una reserva confirmada para evitar que pueda volver a reservarse en ese mismo periodo.

- **Priority:** Must
- **Estimate:** 5 h-p
- **Uncertainty:** Media
- **Predecessors:** US-009, US-012
- **Initial plan:** Pendiente de asignación en la planificación de la Semana 3.

#### Acceptance criteria

- **US-011-AC-01:** Tras confirmar una reserva, el vehículo queda ocupado durante las fechas reservadas.
- **US-011-AC-02:** Una búsqueda posterior no ofrece el vehículo como disponible durante un periodo incompatible.
- **US-011-AC-03:** El bloqueo afecta únicamente al intervalo de fechas reservado.

#### Verification and constraints

- La disponibilidad debe mantenerse coherente con las reservas almacenadas.
- El bloqueo no implica una modificación física del vehículo.
- No se utilizarán sistemas externos de flotas ni dispositivos IoT.

---

### US-012 — Evitar reservas solapadas

> Como cliente, quiero que el sistema impida reservar un vehículo ocupado durante alguna de las fechas seleccionadas para evitar conflictos entre reservas.

- **Priority:** Must
- **Estimate:** 7 h-p
- **Uncertainty:** Alta
- **Predecessors:** US-007
- **Initial plan:** Pendiente de asignación en la planificación de la Semana 3.

#### Acceptance criteria

- **US-012-AC-01:** El sistema comprueba las reservas existentes antes de registrar una nueva.
- **US-012-AC-02:** Si existe solapamiento, la nueva reserva no se registra.
- **US-012-AC-03:** El usuario recibe un mensaje indicando que el vehículo no está disponible.
- **US-012-AC-04:** Dos reservas del mismo vehículo pueden existir únicamente cuando sus periodos no se solapan.

#### Verification and constraints

- Un vehículo no puede tener dos reservas activas que compartan al menos un día.
- Las fechas de inicio y fin se consideran incluidas en el periodo reservado.
- Si una reserva finaliza el día 12, una nueva reserva del mismo vehículo podrá comenzar como mínimo el día 13.
- La validación debe mantener la integridad de la información.
- Solo se consideran las reservas almacenadas dentro de CityDrive.

---

### US-013 — Informar de cambios de disponibilidad durante la reserva

> Como cliente, quiero ser informado si el vehículo deja de estar disponible antes de confirmar la reserva para poder seleccionar otra alternativa.

- **Priority:** Should
- **Estimate:** 4 h-p
- **Uncertainty:** Media
- **Predecessors:** US-012
- **Initial plan:** Pendiente de asignación en la planificación de la Semana 3.

#### Acceptance criteria

- **US-013-AC-01:** La disponibilidad se vuelve a comprobar antes de confirmar la reserva.
- **US-013-AC-02:** Si el vehículo ya no está disponible, la reserva no se confirma.
- **US-013-AC-03:** El usuario recibe un mensaje claro indicando el conflicto.
- **US-013-AC-04:** El usuario puede volver a la búsqueda para elegir otro vehículo.

#### Verification and constraints

- El mensaje debe ser comprensible y no ambiguo.
- No se debe crear una reserva cuando la disponibilidad haya cambiado.
- La comprobación debe utilizar la información actual del propio sistema.
