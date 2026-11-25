# 2. Infraestructura: catálogos y consultorios

## 2.1 Catálogos

Ruta: **Infraestructura › Catálogos** (*Opciones de las listas desplegables del sistema*). Cada **categoría** es una lista desplegable que otros módulos consultan; aquí se agregan, ordenan o desactivan sus opciones.

<figure class="captura"><div class="marco"><img src="img/infra-catalogos.png" alt="Catálogos de infraestructura" data-ruta="/sigarh/infraestructura/catalogos" data-perfil="Administrador SIGARH (datos de prueba)"></div>
<figcaption>Figura 1. Catálogos: opciones de las listas desplegables.</figcaption></figure>

- **Indicadores:** Total opciones, Categorías con datos, Activas e Inactivas.
- **Filtros:** buscador *Buscar por nombre o código* y selector **Todas las categorías**.
- **Tabla:** Categoría, Código, Nombre, Descripción, Orden y Estado.

Las categorías disponibles son: tipos de documento, tipos de servicio, modalidades de atención, estados de cita, tipos de diagnóstico, tipos de alta, procedencia de emergencia, tipos de grupo ocupacional, métodos de pago, tipos de producto, estados de emergencia, estados de comprobante, destino de la atención, tipos de comprobante, **tipos de cama**, tipos de cupo de cita y puntos de llamado.

| Campo | Obligatorio | Descripción |
|---|:-:|---|
| Categoría | <span class="si">Sí</span> | La lista a la que pertenece la opción. *La categoría es requerida*. |
| Nombre | <span class="si">Sí</span> | El texto que verá el usuario. Máximo 100 caracteres. *El nombre es requerido*. |
| Código | <span class="no">No</span> | Identificador técnico opcional. Máximo 20 caracteres. |
| Orden | <span class="no">No</span> | Posición en la lista de opciones. |
| Descripción | <span class="no">No</span> | Explicación adicional. Máximo 255 caracteres. |
| Activo | — | Las opciones inactivas no aparecen en los selectores. |

!!! tip "Consejo"
    Use **Orden** para controlar cómo se listan las opciones en los formularios. Crear una opción **no crea funcionalidad nueva**: solo agrega un valor a una lista que ya existe.

!!! important "Importante"
    Para registrar camas necesita primero la categoría **Tipos de cama** con al menos una opción (por ejemplo, *Cama general* o *Cama UCI*). Sin ella, los formularios de salas y camas indican *Configura los tipos de cama en Infraestructura › Catálogos*.

## 2.2 Consultorios

Ruta: **Infraestructura › Consultorios** (*Ambientes de consulta para la programación médica*).

- **Indicadores:** Total consultorios, Activos, Con especialidad y Capacidad total.
- **Tabla:** Nombre, Especialidad, Piso, Capacidad, Equipamiento y Estado.

| Campo | Obligatorio | Descripción |
|---|:-:|---|
| Nombre del consultorio | <span class="si">Sí</span> | Máximo 100 caracteres. Ej.: *Consultorio 5*. *El nombre del consultorio es requerido*. |
| Especialidad fija | <span class="no">No</span> | Si el consultorio es de una sola disciplina, el selector de médicos en Programación Médica mostrará solo a los pertinentes. Por defecto: *Uso general (sin especialidad)*. |
| Piso | <span class="no">No</span> | Piso donde se ubica (*Sin piso* por defecto). |
| Capacidad de sala | <span class="si">Sí</span> | Pacientes que caben físicamente. **No define los cupos de citas.** |
| Equipamiento | <span class="no">No</span> | Equipos disponibles. Máximo 255 caracteres. |
| Activo | — | Solo los activos se usan en la programación. |

La **asignación de médicos y turnos** a un consultorio no se hace aquí, sino en **Programación Médica** del HIS.

!!! important "Importante"
    No se puede eliminar un consultorio con programación médica activa: *No se puede eliminar: el consultorio tiene N programación(es) médica(s) activa(s).* Desactívelo en su lugar.
