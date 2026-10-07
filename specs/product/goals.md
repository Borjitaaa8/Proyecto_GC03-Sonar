# Objetivos y Alcance: CityDrive

## Objetivos
| ID | Objetivo | Resultado esperado |
|---|---|---|
| G-01 | Autonomía del cliente | El usuario puede completar el recorrido esencial de una reserva sin ayuda externa. |
| G-02 | Claridad y confianza | El usuario comprende el vehículo elegido, las fechas y el estado de su reserva. |
| G-03 | Incremento revisable | Un tercero puede instalar, ejecutar y evaluar de manera estable el incremento desarrollado. |

## Indicadores de éxito
| ID | Objetivo | Meta |
|---|---|---|
| M-01 | G-01 | Al menos cuatro de cinco participantes completan el escenario de reserva en menos de diez minutos y sin ayuda. |
| M-02 | G-02 | Al menos cuatro de cinco participantes comprenden correctamente qué vehículo han reservado y para qué fechas. |
| M-03 | G-03 | Una persona que no haya implementado el producto puede seguir el guion de instalación sin intervenciones no documentadas. |
| M-04 | Todos | No existe ningún defecto bloqueante abierto durante la revisión final. |

## Stakeholders
Los principales stakeholders del proyecto CityDrive son:
* **Clientes de AutoRent:** Usuarios finales que consultarán la disponibilidad de vehículos y realizarán reservas.
* **Personal de AutoRent:** Encargado de mantener la información de los vehículos y consultar las reservas activas.
* **Dirección de AutoRent:** Interesada en mejorar la gestión de las reservas y modernizar el servicio ofrecido a los clientes.
* **Equipo de desarrollo MoveTech Solutions:** Responsable de la planificación, desarrollo, pruebas y evolución del producto.

## Alcance incluido
El proyecto incluye:
* **S-01:** Un recorrido esencial y coherente para la búsqueda, filtrado y reserva individual de un vehículo por días.
* **S-02:** Un catálogo controlado de vehículos y reservas completamente ficticios.
* **S-03:** Funciones básicas para que el personal de AutoRent pueda mantener el catálogo de vehículos y consultar las reservas necesarias para la demostración.

## Exclusiones
Quedan expresamente fuera del proyecto:
* **EX-01:** Procesamiento de pagos reales, pasarelas de pago o facturación.
* **EX-02:** Integraciones con aseguradoras de vehículos.
* **EX-03:** Apertura de puertas mediante hardware o integración IoT con la flota física.

## Supuestos
Para el desarrollo de CityDrive se parte de los siguientes supuestos:
* La información del catálogo de vehículos será ficticia y estará disponible para el desarrollo y las pruebas.
* Cada vehículo solo podrá estar reservado por un cliente para un mismo rango de fechas.
* El sistema trabajará únicamente con la agencia AutoRent.
* No será necesario conectarse con sistemas externos para consultar la disponibilidad de los vehículos.
* Los usuarios dispondrán de acceso a Internet y de un navegador web actualizado.

## Restricciones
El proyecto debe respetar las siguientes condiciones:
* Prohibición de utilizar datos personales, bancarios o de conducción reales.
* Uso exclusivo de las tecnologías y convenciones aprobadas en el curso.
* El desarrollo deberá ajustarse al tiempo y capacidad disponible del equipo.

## Trazabilidad
La cadena de trazabilidad será:
**Misión -> objetivos -> épicas -> historias -> tareas -> código y pruebas -> evidencias.**
Una épica que no contribuya a ningún objetivo se considera fuera del alcance hasta que se apruebe un cambio en los objetivos o en el alcance del proyecto.

## Gestión de cambios
Cualquier modificación de los objetivos, métricas, alcance, exclusiones, supuestos o restricciones requerirá:
1. Revisión por parte del equipo.
2. Decisión explícita del Product Owner.
3. Registro de la decisión tomada.
4. Revisión de la planificación y de la capacidad del equipo si fuera necesario.
5. Actualización de los documentos y referencias afectadas.
