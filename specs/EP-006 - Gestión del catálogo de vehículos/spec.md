# EP-006 — Gestión del catálogo de vehículos

**Goals:** G-02, G-03  
**Baseline:** Catálogo V0 - Semana 2

## Boundary

Esta épica incluye las operaciones básicas necesarias para que el personal de AutoRent pueda mantener el catálogo utilizado por CityDrive: registrar vehículos, modificar su información, cambiar su estado de disponibilidad y consultar el catálogo completo.

Quedan fuera la gestión mecánica del vehículo, la localización GPS, el mantenimiento físico de la flota y las integraciones con sistemas externos.

## Epic outcome

Proporcionar al personal de AutoRent las funciones mínimas necesarias para mantener actualizado el catálogo de vehículos del que depende el proceso de búsqueda y reserva de CityDrive.

## Stories

### US-018 — Dar de alta un vehículo

> Como personal de AutoRent, quiero registrar un nuevo vehículo en el sistema para que pueda formar parte del catálogo disponible.

- **Priority:** Must
- **Estimate:** 6 h-p
- **Uncertainty:** Media
- **Predecessors:** —
- **Initial plan:** Pendiente de asignación en la planificación de la Semana 3.

#### Acceptance criteria

- **US-018-AC-01:** El personal puede introducir los datos básicos definidos para un vehículo.
- **US-018-AC-02:** El sistema valida los campos obligatorios.
- **US-018-AC-03:** Si los datos son válidos, el vehículo queda registrado.
- **US-018-AC-04:** El vehículo registrado puede utilizarse posteriormente en búsquedas y reservas.

#### Verification and constraints

- Los vehículos utilizados serán ficticios.
- No se almacenará información de localización GPS.
- No se incluirán datos de mantenimiento mecánico.
- La información debe persistir correctamente.

---

### US-019 — Modificar la información de un vehículo

> Como personal de AutoRent, quiero modificar los datos de un vehículo para mantener actualizada su información.

- **Priority:** Should
- **Estimate:** 5 h-p
- **Uncertainty:** Baja
- **Predecessors:** US-018
- **Initial plan:** Pendiente de asignación en la planificación de la Semana 3.

#### Acceptance criteria

- **US-019-AC-01:** El personal puede seleccionar un vehículo existente.
- **US-019-AC-02:** Puede modificar los campos permitidos.
- **US-019-AC-03:** Los cambios válidos quedan almacenados.
- **US-019-AC-04:** Las consultas posteriores muestran la información actualizada.

#### Verification and constraints

- Solo se podrán modificar vehículos existentes.
- Las modificaciones deben respetar las validaciones definidas para el catálogo.
- No se incluye información mecánica ni GPS.

---

### US-020 — Modificar el estado de disponibilidad

> Como personal de AutoRent, quiero marcar un vehículo como disponible o no disponible para evitar que se ofrezcan vehículos que temporalmente no pueden alquilarse.

- **Priority:** Should
- **Estimate:** 4 h-p
- **Uncertainty:** Media
- **Predecessors:** US-018
- **Initial plan:** Pendiente de asignación en la planificación de la Semana 3.

#### Acceptance criteria

- **US-020-AC-01:** El personal puede cambiar el estado manual del vehículo.
- **US-020-AC-02:** Un vehículo marcado como no disponible no aparece como reservable.
- **US-020-AC-03:** Un vehículo puede volver a marcarse como disponible.
- **US-020-AC-04:** El nuevo estado queda almacenado correctamente.

#### Verification and constraints

- El estado manual debe tenerse en cuenta junto con las reservas existentes.
- No implica modificar físicamente el vehículo.
- No existe integración con sistemas externos de flota.

---

### US-021 — Consultar el catálogo completo

> Como personal de AutoRent, quiero consultar el catálogo completo de vehículos para revisar la información y el estado actual de la flota.

- **Priority:** Should
- **Estimate:** 5 h-p
- **Uncertainty:** Baja
- **Predecessors:** US-018
- **Initial plan:** Pendiente de asignación en la planificación de la Semana 3.

#### Acceptance criteria

- **US-021-AC-01:** El personal puede visualizar los vehículos registrados.
- **US-021-AC-02:** Cada elemento muestra la información básica definida para el catálogo.
- **US-021-AC-03:** Se muestra el estado actual de disponibilidad de cada vehículo.
- **US-021-AC-04:** La información coincide con los datos almacenados.

#### Verification and constraints

- La consulta está orientada al personal de AutoRent.
- Solo se utilizarán datos ficticios.
- No se incluye información GPS, mecánica ni procedente de sistemas externos.
