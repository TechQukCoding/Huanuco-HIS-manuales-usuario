# Puntos por confirmar con la aplicación corriendo

Todo lo redactado se verificó leyendo el código del ERP. Estos puntos dependen de la configuración o del comportamiento en ejecución:

| # | Manual | Punto | Cómo confirmarlo |
|---|---|---|---|
| 1 | GEN-00 §2.4 | "A las 24 horas se pide iniciar sesión de nuevo" sale de `SESSION_MAX_DURATION_HOURS` (valor por defecto 24). El servidor del hospital puede haberlo cambiado. | Revisar el `.env` del backend. |
| 2 | GEN-00 §2.4 | "La sesión se renueva mientras trabaja": existe el plugin `auth-refresh.client.ts`; falta ver el comportamiento real. | Trabajar más de 60 min y observar. |
| 3 | GEN-00 §2.3 | Límite de 5 intentos / 15 min (constantes en `rate_limit.py`). Requiere Redis activo. | Probar con una cuenta de prueba. |
| 4 | GEN-00 §4.1 | Las reglas de contraseña se verificaron en el ERP y en SIGARH (`validar_password`); en el perfil del HIS no se leyó la validación. | Probar en `/app/perfil`. |
| 5 | GEN-00 §3.2 | Barra superior de SIGARH: se vio ayuda y notificaciones; confirmar que no tiene más iconos. | Captura real. |
| 6 | ERP-01 §5.3 | Desde el ERP, "Nueva cuenta" ofrece cualquier rol hospitalario, pero `validar_perfil` solo admite sin perfil el rol `administrador`. **Posible mejora del producto**: filtrar los roles del formulario. | Intentar crear un médico desde el ERP. |
| 7 | ERP-01 §2.4 | Colores de ocupación: 75 % advertencia / 90 % crítico (del código del escritorio). | Captura con datos de prueba. |
| 8 | Todos | Posición de los números de llamada: se colocan cuando existan las capturas reales. | Tomar capturas. |
| 9 | SIG-04 §2.3 | **Posible mejora del producto**: el menú de usuarios, perfiles y roles ofrece **Eliminar**, pero el backend siempre responde 409 (*Las cuentas y permisos se desactivan; no se eliminan para conservar auditoría*). Conviene ocultar la opción en esas tres pantallas. | Intentar eliminar un usuario de prueba. |
| 10 | SIG-04 §2.3 y §7 | En catálogos **en uso**, el backend rechaza cualquier cambio salvo la Descripción (`changed - {descripcion}`), lo que parecería impedir también **desactivarlos**. Confirmar si hay otra vía para desactivar. | Desactivar un catálogo ya usado. |
| 11 | SIG-04 §3.3 | La etiqueta *Aún no restringe* depende de la marca `enforced` por submódulo; la lista actual puede variar. | Captura real del árbol. |
| 12 | SIG-04 §5.3 | "Elegir al empleado con programación aprobada" sale de un texto de ayuda; el backend solo valida la profesión (MED / ENF). | Probar con un médico sin programación. |
| 13 | SIG-04 §7 | Qué campos de cada catálogo son obligatorios se tomó de las marcas del formulario; confirmar los de Niveles, Departamentos y Grupos (comparten un componente común). | Abrir cada formulario. |
| 14 | SIG-04 §7.3 | La pantalla *UPSS y servicios* es una jerarquía; falta documentar su alta/edición con capturas. | Captura real. |
| 15 | SIG-01 §2.2 | El alta de empleados es un asistente de 5 pasos; los campos *Profesión*, *Régimen laboral* y *Condición laboral* salen de componentes compartidos. Confirmar su orden y etiquetas con capturas. | Abrir el alta de empleado. |
| 16 | SIG-01 §2.5 | Las reglas de coherencia (tipo de trabajador vs. vínculo, nivel remunerativo vs. profesión) se leyeron en el backend; falta ver en qué combinaciones aparece cada mensaje. | Probar con datos de prueba. |
| 17 | SIG-01 §3.4 | El formulario de Tolerancias exige dependencia y grupo, pero el backend admite reglas solo por grupo. Confirmar si existen reglas antiguas sin dependencia. | Revisar los datos de la base. |
| 18 | SIG-01 §6 y §8 | No se documentó **quién** puede aprobar o rechazar cada movimiento (jefatura, RR. HH.): los permisos por acción de estas pantallas no se pudieron confirmar en el código leído. | Probar con un usuario sin permiso. |
| 19 | SIG-01 §8.2 | Al aprobar un cambio de turno solo se documentó la asistencia del solicitante; confirmar qué ocurre con la del aceptante en la fecha de reemplazo. | Aprobar un cambio de prueba. |
| 20 | SIG-01 §6.3 y §7.2 | Aprobar vacaciones o licencias retira cupos de Consulta Externa y marca en riesgo citas: confirmar el aviso que ve el usuario. | Aprobar una vacación de un médico con agenda. |
| 21 | SIG-02 §4.2 | En la categoría Médicos, el diagnóstico marca como **error** cualquier turno de tipo complementario o retén (*requieren reglas y autorizaciones específicas*), por lo que esos roles no se pueden enviar ni aprobar. Confirmar si es el comportamiento previsto en esta versión. | Crear un rol médico complementario de prueba. |
| 22 | SIG-02 §7.2 | Significado exacto de la marca *Rol pendiente de aprobación* en el calendario de turnos. | Captura real con un rol pendiente. |
| 23 | SIG-02 §2.1 | El motivo del rechazo se muestra al pasar el cursor sobre el estado en la lista (atributo `title`); confirmar que es visible en pantallas táctiles. | Probar en móvil. |
| 24 | SIG-02 §5.3 | Reglas de aprobación leídas en `puede_aprobar_roles` (permiso + jefe de servicio o alcance global); falta confirmar el caso de un revisor sin jefatura con alcance global apagado. | Probar con un revisor de prueba. |
| 25 | SIG-03 §2.1 | Los nombres de las 17 categorías de Catálogos se tomaron de sus claves en el backend; confirmar cómo las muestra la pantalla. | Captura real del selector de categorías. |
| 26 | SIG-03 §4.2 | La columna *Marcas* del listado de medicamentos no se documentó: no se vio de dónde sale. | Abrir un producto con marcas. |
| 27 | SIG-03 §5.1 | El backend puede crear seguros estándar por su cuenta (`asegurar_seguros_estandar`); confirmar y documentar cuáles. | Revisar los seguros de un hospital nuevo. |
| 28 | SIG-03 §5.3 | Qué tipos de servicio Caja no cobra automáticamente (marca `caja: false` en el formulario de tarifas). | Revisar `TarifaForm.vue` con desarrollo. |
| 29 | SIG-03 §5.2 | Los campos de *Cajas* no muestran marca de obligatorio; confirmar la validación del backend. | Intentar crear una caja vacía. |
| 30 | SIG-03 §7.1 | La API del CIE-10 admite crear, editar y eliminar, pero la pantalla es solo de consulta. Confirmar que es lo previsto. | Consultar con desarrollo. |
| 31 | HIS-01 §8.1 | **Posible mejora del producto**: *Servicio Social* pide los **UUID** del paciente y del trabajador social en lugar de un buscador. El manual explica cómo copiarlos de la dirección de la ficha. | Abrir *Nueva evaluación*. |
| 32 | HIS-01 §2.2 | *Buscar por DNI* consulta un servicio de identidad externo; confirmar su disponibilidad en el hospital y qué mensaje sale si no responde. | Probar con red restringida. |
| 33 | HIS-01 §3.2 | Significado exacto de *Fuente de financiamiento* y *Producto / Plan* al citar. | Captura real del modal. |
| 34 | HIS-01 §4.3 | No se vio un botón *Agregar Programación* en el listado (existe la pantalla de creación); confirmar cómo se llega a ella y quién puede. | Revisar el menú con un perfil de admisión. |
| 35 | HIS-01 §6.4 | Permiso necesario para *Turnero › Configuración* (middleware `panel`). | Probar con un perfil sin permiso. |
| 36 | HIS-01 §5.2 | Efecto de *Atender* con una cita vinculada en la lista de espera (¿cambia el estado de la cita?). | Probar con datos de prueba. |
| 37 | HIS-02 §5.5 | **Posible incoherencia del producto**: el formulario de hospitalización de la consulta muestra un botón *Dar de Alta*, pero el backend responde que el alta se registra firmando la epicrisis en Hospitalización. | Probar el botón con un paciente internado de prueba. |
| 38 | HIS-02 §3.2 | Los rangos de ejemplo de los signos vitales (p. ej. frecuencia respiratoria *30-60*) parecen pediátricos; confirmar si deben variar por edad. | Revisar con el área clínica. |
| 39 | HIS-02 §7.1 | Los nombres exactos de las tres listas de la Bandeja electrónica se infirieron de sus mensajes vacíos. | Captura real. |
| 40 | HIS-02 §8.4 | Cuándo se habilita el botón *Programar* de una solicitud de telesalud (depende de que exista una cita virtual del paciente por enlazar). | Probar con datos de prueba. |
| 41 | HIS-02 §4 | Los destinos *Alta* y *Referencia* y sus efectos sobre otros módulos (Admisión, Referencias) se validaron en backend; falta probar el recorrido completo. | Atender una consulta de prueba de principio a fin. |
| 42 | Entorno | **Mejora para desarrollo**: el backend declara `sqlalchemy` sin `greenlet`/`sqlalchemy[asyncio]`; en algunos equipos Windows `pip install -e ".[dev]"` no lo instala y `alembic` falla. | Instalación limpia en Windows. |
| 43 | Entorno | **Mejora para desarrollo**: `npm install` falla con `ERESOLVE` (conflicto de pares entre `@pinia/nuxt` y `@pinia-plugin-persistedstate/nuxt`); funciona con `--legacy-peer-deps`. Sugerido: `.npmrc` con `legacy-peer-deps=true`. | `npm install` en limpio. |
| 44 | Datos de prueba | **Choque de scripts**: `scripts.demo_sigarh` etapa `renombrar` falla (`uq_mant_perfiles_usuario_nombre`) porque la instalación del hospital ya crea los perfiles con nombre limpio (*Médico asistencial*, etc.) además de los *(prueba)* de `seed_datos_prueba`. Se omitió esa etapa (`--solo configuracion rrhh roles nutricion`). | Instalar un hospital nuevo y correr los tres scripts en orden. |

