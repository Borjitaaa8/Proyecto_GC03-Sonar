# EP-002 — Filtrado y consulta de vehículos

**Goals:** G-01, G-02  
**Baseline:** Catálogo V0 - Semana 2

## Boundary

Esta épica incluye el filtrado de los resultados disponibles según el tipo de vehículo, la consulta de las características principales de cada vehículo y la visualización de su disponibilidad.

Quedan fuera de esta épica la introducción inicial de las fechas, la confirmación de reservas y la gestión del catálogo por parte del personal de AutoRent.

## Epic outcome

Facilitar que el cliente pueda reducir las opciones disponibles y consultar la información necesaria de cada vehículo antes de decidir cuál desea reservar.

## Stories

### US-004 — Filtrar los vehículos por tipo

> Como cliente, quiero filtrar los vehículos disponibles por tipo para poder encontrar más fácilmente un coche o una furgoneta según mis necesidades.

- **Priority:** Must
- **Estimate:** 4 h-p
- **Uncertainty:** Baja
- **Predecessors:** US-002
- **Initial plan:** Pendiente de asignación en la planificación de la Semana 3.

#### Acceptance criteria

- **US-004-AC-01:** El usuario puede seleccionar el tipo coche.
- **US-004-AC-02:** El usuario puede seleccionar el tipo furgoneta.
- **US-004-AC-03:** Los resultados muestran únicamente vehículos del tipo seleccionado.
- **US-004-AC-04:** El usuario puede eliminar el filtro y volver a ver todos los vehículos disponibles.

#### Verification and constraints

- El filtro se aplica únicamente sobre los resultados de vehículos disponibles.
- En esta versión solo se contemplan coches y furgonetas.
- El filtro debe ser fácil de localizar y utilizar.
- Si no existen resultados del tipo seleccionado, se debe mostrar un mensaje claro.

---

### US-005 — Consultar las características de un vehículo

> Como cliente, quiero consultar las características principales de un vehículo para poder valorar si se adapta a mis necesidades.

- **Priority:** Should
- **Estimate:** 5 h-p
- **Uncertainty:** Baja
- **Predecessors:** US-002
- **Initial plan:** Pendiente de asignación en la planificación de la Semana 3.

#### Acceptance criteria

- **US-005-AC-01:** El usuario puede acceder a la información principal de un vehículo.
- **US-005-AC-02:** Se muestra al menos el tipo de vehículo y la información básica definida en el catálogo.
- **US-005-AC-03:** La información mostrada corresponde al vehículo seleccionado.

#### Verification and constraints

- Solo se utilizará información ficticia del catálogo de AutoRent.
- La información debe mostrarse de forma clara y legible.
- No se incluirán datos mecánicos o técnicos ajenos al alcance definido.

---

### US-006 — Visualizar la disponibilidad del vehículo seleccionado

> Como cliente, quiero comprobar que el vehículo seleccionado está disponible para las fechas indicadas antes de iniciar la reserva.

- **Priority:** Must
- **Estimate:** 4 h-p
- **Uncertainty:** Media
- **Predecessors:** US-002
- **Initial plan:** Pendiente de asignación en la planificación de la Semana 3.

#### Acceptance criteria

- **US-006-AC-01:** El sistema indica si el vehículo está disponible para el rango seleccionado.
- **US-006-AC-02:** Un vehículo con una reserva incompatible no se muestra como disponible.
- **US-006-AC-03:** Un vehículo marcado manualmente como no disponible tampoco se considera disponible.

#### Verification and constraints

- La disponibilidad debe calcularse usando las reservas almacenadas y el estado del vehículo.
- La información mostrada debe ser coherente con los resultados de búsqueda.
- No se utilizarán servicios externos para determinar la disponibilidad.
