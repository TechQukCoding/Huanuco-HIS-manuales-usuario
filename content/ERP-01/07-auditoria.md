# 7. Auditoría

La auditoría registra quién hizo qué y cuándo. Hay dos vistas con la misma estructura:

| Vista | Qué muestra |
|---|---|
| **Auditoría del sistema** | Eventos del propio ERP (por ejemplo, inicios de sesión de administradores y cambios en cuentas administradoras). |
| **Auditoría del hospital** | Eventos del hospital: inicios de sesión y cambios realizados por los usuarios del HIS y SIGARH. |

<figure class="captura"><div class="marco"><img src="img/erp-auditoria.png" alt="Auditoría del hospital" data-ruta="/admin/auditoria/hospital" data-perfil="Administrador (datos de prueba)"></div>
<figcaption>Figura 8. Auditoría del hospital.</figcaption></figure>

<ol class="leyenda">
<li><strong>Actualizar / Exportar página.</strong></li>
<li><strong>Resumen.</strong> Eventos registrados, Hoy y Usuarios distintos.</li>
<li><strong>Búsqueda y filtros por acción.</strong></li>
<li><strong>Tabla de eventos.</strong> Fecha, Usuario, Acción, Descripción e IP.</li>
</ol>

## 7.1 Buscar y filtrar

- Escriba en **Buscar en descripción, usuario o modelo**.
- Use las pestañas de acción, cada una con su cantidad: **Todos**, **Inicio de sesión**, **Creado**, **Actualizado**, **Eliminado** e **Intento fallido**.
- La tabla pagina de 20 en 20 eventos.

## 7.2 Ver el detalle de un evento

Haga clic en una fila. Se abre un panel lateral con:

- **Usuario**, **IP**, **Modelo** y **Origen** (*Hospital* o *Sistema*), y la **Descripción**.
- **Cambios**: una tabla con **Campo**, **Antes** y **Después**, que solo lista los campos que cambiaron. Si el evento no modificó datos, dice *Este evento no registra cambios de datos.*

## 7.3 Exportar

**Exportar página** descarga solo los eventos que se ven en la página actual. Para volcar más eventos use *Exportar datos › Auditoría* (capítulo 6), que permite 500, 1 000 o 5 000.

## 7.4 Eventos pendientes de reintento (Auditoría del sistema)

Si por una falla temporal algunos eventos no pudieron registrarse, aparece un aviso amarillo: *N evento(s) de auditoría esperan reintento*. Si quedaron en el archivo de emergencia porque la base de administración no respondió, el aviso lo indica.

<ol class="pasos">
<li>Pulse <strong>Reintentar ahora</strong>.</li>
<li>El aviso informa cuántos eventos se recuperaron y cuántos tuvieron error.</li>
<li>Si persisten errores, avise a soporte técnico para que revise los registros del servidor.</li>
</ol>

!!! note "Nota"
    El HIS tiene además su propia pantalla de auditoría por módulo y usuario (manual HIS-11). Esa es distinta de la auditoría del ERP.
