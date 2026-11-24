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

