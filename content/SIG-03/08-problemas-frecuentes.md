# 8. Problemas frecuentes

| Situación o mensaje | Causa | Qué hacer |
|---|---|---|
| *Configura los tipos de cama en Infraestructura › Catálogos* | No hay opciones en la categoría **Tipos de cama**. | Cree al menos una opción (capítulo 2). |
| *No se puede eliminar: el piso tiene N servicio(s) y N sala(s) asociados.* | El piso se usa. | Reasigne esos registros o desactive el piso. |
| *No se puede eliminar: la sala tiene N cama(s) ocupada(s).* | Hay pacientes internados. | Espere a registrar sus altas en Hospitalización. |
| *Ya existe una cama con el código …* | Código repetido. | Use otro código. |
| *Esta cama tiene una hospitalización activa; el alta del paciente debe registrarse desde el módulo de Hospitalización…* | Intenta cambiar el estado de una cama con paciente. | Registre el alta desde el HIS. |
| *No se pudieron generar las camas por un conflicto de código…; reintente.* | Otra operación usó el mismo prefijo. | Vuelva a intentarlo o cambie el prefijo. |
| *No se puede eliminar: el consultorio tiene N programación(es) médica(s) activa(s).* | El consultorio está programado. | Desactívelo o retire la programación en el HIS. |
| *Ya existe un almacén / producto con el código …* | Código repetido. | Use otro código. |
| *No se puede desactivar: … tiene existencias con stock mayor que cero* | Hay stock. | Regularice el inventario en el HIS (HIS-08) antes de desactivar. |
| *La temperatura mínima no puede ser mayor que la máxima* | Rango invertido. | Corrija las temperaturas de conservación. |
| *El RUC debe tener 11 dígitos* | RUC incompleto. | Escriba los 11 dígitos. |
| *El porcentaje debe estar entre 0 y 100* | Cobertura fuera de rango. | Corrija el porcentaje. |
| Caja no encuentra tarifa para un servicio | Falta la tarifa general o está inactiva. | Cree o active una tarifa **general** (capítulo 5). |
| No puedo abrir una caja | La caja está **inactiva** o ya está abierta. | Actívela (capítulo 5) y ábrala desde el HIS. |
| Un examen no se puede ordenar desde la consulta | El examen está **inactivo**. | Actívelo en el catálogo (capítulo 6). |
| No aparece un diagnóstico CIE-10 | El catálogo no lo incluye o está inactivo. | Use otro término de búsqueda o pida revisión a soporte. |
