# EP-005 — Consulta y gestión de reservas

**Goals:** G-01, G-02  
**Baseline:** Catálogo V0 - Semana 2

## Boundary

Esta épica incluye la consulta de una reserva mediante su referencia, la visualización de sus datos, la posibilidad de cancelarla y la consulta de las reservas activas por parte del personal de AutoRent.

Quedan fuera los reembolsos, pagos, modificaciones contractuales y cualquier gestión relacionada con aseguradoras.

## Epic outcome

Permitir que el cliente pueda consultar y gestionar de forma básica una reserva ya realizada y que el personal de AutoRent tenga visibilidad sobre las reservas activas.

## Stories

### US-014 — Consultar una reserva mediante su referencia

> Como cliente, quiero introducir la referencia de mi reserva para poder consultarla posteriormente.

- **Priority:** Must
- **Estimate:** 4 h-p
- **Uncertainty:** Baja
- **Predecessors:** US-010
- **Initial plan:** Pendiente de asignación en la planificación de la Semana 3.

#### Acceptance criteria

- **US-014-AC-01:** El usuario puede introducir una referencia de reserva.
- **US-014-AC-02:** Si la referencia existe, el sistema recupera la reserva correspondiente.
- **US-014-AC-03:** Si la referencia no existe, se muestra un mensaje claro.
- **US-014-AC-04:** La consulta no modifica los datos almacenados.

#### Verification and constraints

- Cada referencia debe identificar una única reserva.
- Las reservas y referencias utilizadas serán ficticias.
- Los errores deben comunicarse de forma comprensible.
- La consulta debe ser sencilla.

---

### US-015 — Visualizar los datos de una reserva

> Como cliente, quiero visualizar el vehículo, las fechas y el estado de mi reserva para comprobar su información.

- **Priority:** Should
- **Estimate:** 4 h-p
- **Uncertainty:** Baja
- **Predecessors:** US-014
- **Initial plan:** Pendiente de asignación en la planificación de la Semana 3.

#### Acceptance criteria

- **US-015-AC-01:** Se muestra el vehículo asociado a la reserva.
- **US-015-AC-02:** Se muestran las fechas de inicio y fin.
- **US-015-AC-03:** Se muestra el estado actual de la reserva.
- **US-015-AC-04:** La información corresponde a la referencia consultada.

#### Verification and constraints

- Solo se mostrará información perteneciente a la reserva localizada.
- La presentación debe ser clara y comprensible.
- No se mostrarán datos sensibles reales.

---

### US-016 — Cancelar una reserva

> Como cliente, quiero cancelar una reserva existente para liberar el vehículo cuando ya no vaya a necesitarlo.

- **Priority:** Should
- **Estimate:** 5 h-p
- **Uncertainty:** Media
- **Predecessors:** US-014
- **Initial plan:** Pendiente de asignación en la planificación de la Semana 3.

#### Acceptance criteria

- **US-016-AC-01:** El usuario puede solicitar la cancelación de una reserva localizada.
- **US-016-AC-02:** Una reserva cancelada deja de considerarse activa.
- **US-016-AC-03:** Las fechas correspondientes vuelven a quedar disponibles si no existe otro conflicto.
- **US-016-AC-04:** El sistema informa de que la cancelación se ha realizado correctamente.

#### Verification and constraints

- La cancelación no implica reembolsos ni operaciones de pago.
- Solo podrán cancelarse reservas existentes.
- La actualización debe mantener coherente la disponibilidad del vehículo.

---

### US-017 — Consultar las reservas activas

> Como personal de AutoRent, quiero consultar las reservas activas para conocer qué vehículos están comprometidos y durante qué fechas.

- **Priority:** Must
- **Estimate:** 5 h-p
- **Uncertainty:** Media
- **Predecessors:** US-009
- **Initial plan:** Pendiente de asignación en la planificación de la Semana 3.

#### Acceptance criteria

- **US-017-AC-01:** El personal puede consultar una lista de reservas activas.
- **US-017-AC-02:** Cada reserva muestra al menos el vehículo y las fechas asociadas.
- **US-017-AC-03:** Las reservas canceladas no se consideran activas.
- **US-017-AC-04:** La información coincide con las reservas almacenadas.

#### Verification and constraints

- La consulta está orientada al personal de AutoRent.
- Se utilizarán únicamente datos ficticios.
- No incluye facturación, pagos ni información de aseguradoras.
