# 4. El diagnóstico y las reglas de programación

El **diagnóstico** revisa el rol cada vez que cambia y separa lo que hay que corregir de lo que solo conviene saber:

| Nivel | Efecto |
|---|---|
| **Error** | **Impide enviar** el rol a revisión y también **impide aprobarlo**. |
| **Advertencia** | No bloquea; avisa de algo que conviene revisar. |

En el editor y en la pantalla de revisión aparece el recuento, por ejemplo *2 advertencias*. Cada mensaje indica el empleado y la actividad afectados.

## 4.1 Reglas generales (todas las categorías)

| Mensaje | Qué corregir |
|---|---|
| *… trabajador inactivo o inexistente.* | Reactive al empleado o quítelo del rol. |
| *… no tiene actividades asignadas.* | Agregue al menos una actividad. |
| *… la actividad no tiene turnos.* | Agregue al menos un turno a la actividad. |
| *… actividad inactiva o inexistente.* / *… horario inactivo o inexistente.* | Elija una actividad u horario activos (manual SIG-04). |
| *… horario con horas inválidas.* | Corrija el horario en el catálogo. |
| *… turno fuera de su vigencia laboral los días …* | Hay días del turno anteriores al ingreso o posteriores al cese del empleado (manual SIG-01). |
| *… un turno no tiene horario; no generará cupos.* / *… no tiene días de la semana.* | En actividades asistenciales, todo turno necesita horario y días. |
| *… X y Y se solapan en día y horario.* | Dos turnos asistenciales del mismo empleado coinciden. |
| *(advertencia)* un turno de una actividad **no asistencial** no tiene horario | No bloquea; conviene asignarlo. |
| *(advertencia)* *Ningún turno del rol usa una actividad que genere agenda (p. ej. «Consulta externa»): al aprobarlo no se abrirán cupos de consulta en la App Hospitalaria.* | Se puede aprobar, pero **no abrirá cupos**. Use una actividad asistencial. |

## 4.2 Reglas de la categoría Médicos

Para los médicos el diagnóstico revisa además la **ficha del empleado** y la **jornada**. Todos estos son **errores**:

| Mensaje | Qué corregir en la ficha (manual SIG-01) |
|---|---|
| *Complete profesión, tipo de trabajador, nivel, grupo ocupacional y servicio del médico.* | Complete esos cinco datos. |
| *Registre la colegiatura y su habilitación verificada en la ficha del médico.* | Número de colegiatura (o CMP) y habilitación. |
| *Registre fecha de ingreso y vínculo laboral del médico.* | Complete esos datos. |
| *Registre la jornada mensual y el documento que la sustenta en la ficha del médico.* | **Horas ordinarias mensuales** y **Sustento de la jornada**. |
| *La programación de jefaturas requiere autorización y distribución de jornada específicas aún no registradas.* | Los jefes de servicio no se pueden programar por ahora en estos roles. |
| *Registre una especialidad activa compatible con el servicio del rol para generar cupos.* | Agregue al médico una especialidad que el servicio atienda. |
| *La especialidad del médico no está validada.* | La especialidad debe estar validada. |

### Límites de jornada

!!! important "Importante"
    En la categoría **Médicos**, los roles de **Horas Complementarias** y de **Retén** muestran hoy el error *Servicios complementarios y retén requieren reglas y autorizaciones específicas; no se pueden aprobar como jornada ordinaria.* Con el diagnóstico actual no es posible enviarlos ni aprobarlos.

| Regla | Mensaje |
|---|---|
| Las horas **ordinarias** del mes no pueden superar su jornada documentada. | *Acumula N horas ordinarias; su jornada documentada permite M horas mensuales.* |
| La **guardia ordinaria** no puede pasar de **60 horas al mes**. | *Supera 60 horas de guardia ordinaria mensual…* |
| Un turno de **Consulta Externa** no puede pasar de **4 horas continuas**. | *Consulta externa supera cuatro horas continuas. Separe las actividades de gestión clínica del turno de seis horas.* |
| Una **guardia** no puede pasar de **12 horas**. | *La guardia supera doce horas…* |
| No puede haber **horarios superpuestos**, ni dentro del rol ni con otros roles pendientes o aprobados del mismo médico. | *Tiene actividades o roles con horarios superpuestos.* |
| Tras una guardia que termina otro día, debe haber **descanso postguardia** en el siguiente día laborable (sin fines de semana ni feriados **nacionales** cargados en SIGARH). | *Incumple descanso postguardia o restricción previa a guardia nocturna del …* |
| El médico no puede estar ya programado en un rol aprobado de otro servicio a la misma hora. | *… choca con la programación ya aprobada de '…' (mismo día y franja horaria).* |
