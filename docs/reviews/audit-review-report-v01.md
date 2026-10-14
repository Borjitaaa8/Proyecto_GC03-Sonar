
# Informe de Auditoría de Planificación y Viabilidad (v01)

- **Proyecto:** CityDrive (MoveTech Solutions / AutoRent)
- **Agente auditor:** `audit-reviewer`
- **Fecha:** Semana 4
- **Fuentes auditadas:** `CityDrive_Semana3_FINAL.xlsx`, especificaciones `EP-001` a `EP-006` y planificación ProjectLibre.

---

## 1. Identificación y Tratamiento de Riesgos del Proyecto

| ID               | Situación                                      | Evento                                                                                        | Consecuencia                                                   | Tratamiento                                                                                                                         |
| :--------------- | :---------------------------------------------- | :-------------------------------------------------------------------------------------------- | :------------------------------------------------------------- | :---------------------------------------------------------------------------------------------------------------------------------- |
| **RSK-01** | Concurrencia crítica en reservas (`US-012`). | Dos usuarios intentan reservar el mismo vehículo en fechas solapadas simultáneamente.       | Reserva duplicada y pérdida de confianza del cliente.         | **Mitigar:** Implementación de bloqueo atómico con validación previa en base de datos transaccional.                       |
| **RSK-02** | Variabilidad en estimaciones de equipo.         | Desviaciones de tiempo en historias de incertidumbre alta (ej. `US-012` estimada en 7 h-p). | Retraso acumulado en entregas de releases.                     | **Aceptar/Mitigar:** Uso del margen de contingencia global de 30 h (22,7%) concentrado especialmente en IT-006 (12 h libres). |
| **RSK-03** | Cuello de botella en roles clave.               | Concentración de lógica crítica en el Tech Lead (`Óscar` con 25 h planificadas).        | Posible sobreasignación puntual o bloqueo si hay incidencias. | **Mitigar:** Apoyo cruzado de Álvaro en desarrollo backend y reparto de subtareas en IT-001/IT-004.                          |
| **RSK-04** | Definición no funcional de rendimiento.        | Requisito de tiempos de respuesta no medible de forma reproducible.                           | Discrepancias en la aceptación del DoD.                       | **Mitigar:** Criterios acotados a respuestas <2s en entorno local documentados en el DoD.                                     |

---

## 2. Auditoría del Modelo de Planificación (ProjectLibre y Excel)

### 2.1. Configuración de Recursos y Capacidad

- **Equipo:** 5 integrantes (Julia, Andrea, Óscar, Borja, Álvaro) con roles diferenciados.
- **Capacidad nominal:** 27 h/semana; **Capacidad efectiva:** 22 h/semana (5 h de deducción por ceremonias de gestión y coordinación).
- **Control de sobreasignación:** Ningún integrante excede su techo semanal en ninguna iteración (máximas cargas: Julia 5 h, Andrea 4 h, Óscar 5 h, Borja 4 h, Álvaro 4 h).

### 2.2. Coste del Proyecto

- **Tarifa justificada:** 25,00 €/h estándar para el equipo de desarrollo.
- **Coste de desarrollo del Backlog:** $102\text{ h} \times 25\text{ €/h} = \mathbf{2.550,00\ \text{€}}$.
- **Presupuesto horizonte con contingencia:** $132\text{ h} \times 25\text{ €/h} = \mathbf{3.300,00\ \text{€}}$.
- **Reserva financiera:** $\mathbf{750,00\ \text{€}}$ (30 h de colchón).

### 2.3. Secuencialidad y Camino Crítico

- **Precedencias respetadas:** Se valida el orden entre entregas: alta de catálogo (`US-018`) y fechas (`US-001`) $\rightarrow$ disponibilidad masiva (`US-002`) $\rightarrow$ reserva (`US-007`/`US-008`) $\rightarrow$ concurrencia y confirmación (`US-012`/`US-009`).
- **Camino crítico:** Formado por `US-001` $\rightarrow$ `US-002` $\rightarrow$ `US-007` $\rightarrow$ `US-008` $\rightarrow$ `US-012` $\rightarrow$ `US-009` $\rightarrow$ `US-010` $\rightarrow$ `US-014` $\rightarrow$ `US-016`. Las desviaciones en este flujo deben absorberse con la holgura de IT-006.

---

## 3. Dictamen Final del Auditor

- **Veredicto:** **APROBADO CON CONDICIONES (READY_WITH_CONDITIONS)**.
- **Condición:** Mantener la supervisión de la secuencia interna durante las iteraciones 1 y 4 debido a márgenes reducidos (+1 h y +2 h), asegurando que el buffer de IT-006 permanezca reservado para estabilización.
