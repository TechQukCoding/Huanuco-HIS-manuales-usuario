# 8. Problemas frecuentes

| Mensaje o situación | Causa | Qué hacer |
|---|---|---|
| Los botones **Nuevo…** están deshabilitados | Su rol no incluye **Administrar Seguridad** (o **Administrar Mantenimiento** en catálogos). | Solicite el permiso a un administrador que lo tenga. |
| *No puede otorgar permisos que usted mismo no tiene* | Intenta conceder en un rol un permiso de acción que usted no posee. | Pida a alguien con ese permiso que cree el rol. |
| *Otra persona administradora debe modificar sus propias autorizaciones* | Intenta cambiar el rol, el perfil o los permisos que usted mismo usa. | Pida a otra persona administradora que lo haga. |
| *Administrar requiere el módulo Mantenimiento* | Marcó un permiso de administración sin el módulo Mantenimiento. | Marque también el módulo **Mantenimiento** en el rol. |
| *Aprobar turnos requiere el módulo Roles Pendientes* | Marcó *Aprobar roles de turno* sin el módulo. | Marque el módulo **Roles Pendientes**. |
| *Los módulos deben existir y estar habilitados…* | Un módulo del rol o del perfil no está activo en el hospital. | Pida a un administrador central que lo active en el ERP, o quítelo. |
| *No cambie el panel o tipo de cuenta de un rol utilizado; cree otro rol* | El rol ya está asignado a perfiles. | Cree un rol nuevo con el panel o tipo deseado. |
| *El nuevo rol debe conservar el panel y tipo de cuenta del perfil utilizado* | Quiere cambiar el rol de un perfil en uso a uno de otro panel o tipo. | Cree un perfil nuevo. |
| *Seleccione un perfil del panel hospitalario* | Falta elegir perfil en la cuenta hospitalaria. | Elija un perfil activo. |
| *Vincule un empleado con profesión Médico Cirujano* / *… Enfermería* | La cuenta médica o de enfermería no tiene el vínculo correcto. | Registre al empleado con esa profesión (SIG-01) y vincúlelo. |
| *El usuario o correo ya existe en el panel hospitalario* | Duplicado. | Use otro usuario o correo, o reactive la cuenta existente. |
| *La contraseña no cumple los requisitos mínimos* | Falta algún requisito. | Use **Generar contraseña segura** o corrija los marcados en rojo. |
| *El usuario requiere un perfil y rol activos* (al ingresar) | Se desactivó su perfil o su rol. | Reactive el perfil y el rol, o asigne otro perfil. |
| *El catálogo ya está utilizado. Conserve el registro y cree una nueva versión* | Intenta cambiar un registro de catálogo que otros ya usan. | Solo puede editar la **Descripción**; cree un registro nuevo para lo demás. |
| *No puede eliminar un catálogo utilizado por otros registros* | El registro está en uso. | Déjelo como está; no se elimina. |
| *Las cuentas y permisos se desactivan; no se eliminan para conservar auditoría* | Intentó eliminar un usuario, perfil o rol. | Use el interruptor **Activo** para desactivarlo. |
| *La tarifa ya inició su vigencia; cierre su período y cree una nueva tarifa* | Intenta modificar una guardia valorizada vigente. | Ponga fecha en **Vigente hasta** y cree una tarifa nueva. |
