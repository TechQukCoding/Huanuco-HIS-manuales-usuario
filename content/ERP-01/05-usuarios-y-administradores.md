# 5. Usuarios y administradores

El ERP maneja dos listas de cuentas: **Usuarios del hospital** (cuentas del Panel Hospitalario y de SIGARH) y **Administradores** (cuentas del ERP).

## 5.1 Listado de cuentas

<figure class="captura"><div class="marco"><img src="img/erp-usuarios-listado.png" alt="Listado de cuentas" data-ruta="/admin/usuarios" data-perfil="Administrador (datos de prueba)"></div>
<figcaption>Figura 4. Listado de usuarios del hospital.</figcaption></figure>

<ol class="leyenda">
<li><strong>Nueva cuenta / Nuevo administrador.</strong></li>
<li><strong>Tarjetas resumen.</strong> Cuentas, Activas e Inactivas.</li>
<li><strong>Búsqueda y filtros.</strong> Por nombre o correo; pestañas <em>Todas</em>, <em>Activas</em> e <em>Inactivas</em> con su cantidad.</li>
<li><strong>Tabla.</strong> Cuenta, Rol, Panel, Estado, Creada y menú de acciones (tres puntos).</li>
</ol>

- La lista muestra **20 cuentas por página**.
- Las cuentas de **solo lectura** llevan la etiqueta *Solo lectura* junto al rol.
- Haga clic en una fila para abrir el detalle.
- Si no se puede consultar la base del hospital, el sistema avisa y muestra solo las cuentas administradoras.

### Acciones por cuenta (menú de tres puntos)

| Acción | Disponible para | Efecto |
|---|---|---|
| **Editar** / **Ver detalle** | Todas | Abre la cuenta. Las administradoras se editan; las del hospital solo se consultan. |
| **Activar** / **Desactivar** | Todas | Cambia el estado. Una cuenta inactiva no puede iniciar sesión. |
| **Eliminar** | Solo cuentas administradoras | Pide confirmación (*No se puede deshacer*). |

!!! important "Importante"
    Las cuentas del hospital **no se eliminan, solo se desactivan**, para conservar la autoría de todo lo que firmaron o registraron.

## 5.2 Crear un administrador

<ol class="pasos">
<li>Entre a <strong>Administradores</strong> y pulse <strong>Nuevo administrador</strong>.</li>
<li>Complete el formulario (tabla siguiente).</li>
<li>Pulse <strong>Crear cuenta</strong>. Aparece el mensaje <em>Cuenta creada</em> y el sistema vuelve al listado.</li>
</ol>

| Campo | Obligatorio | Descripción |
|---|:-:|---|
| Nombre completo | <span class="si">Sí</span> | Nombres y apellidos. |
| Correo electrónico | <span class="si">Sí</span> | Será el usuario de ingreso. |
| Contraseña | <span class="si">Sí</span> | Debe cumplir los requisitos de contraseña (ver GEN-00, sección 4.1). |
| Confirmar contraseña | <span class="si">Sí</span> | Idéntica a la contraseña. |
| Cuenta activa | — | Activada por defecto. Una cuenta inactiva no puede iniciar sesión. |
| Solo lectura (auditor) | — | Desactivado por defecto. Si se activa, la cuenta puede consultar y exportar todo, pero no crear, editar, desactivar ni eliminar. |

La persona configurará su verificación en dos pasos (MFA) la primera vez que inicie sesión.

## 5.3 Crear una cuenta del hospital desde el ERP

El botón **Nueva cuenta** de *Usuarios del hospital* permite crear una cuenta del Panel Hospitalario con estos campos adicionales: **Rol** y **Empleado vinculado** (un médico necesita este vínculo para firmar sus atenciones).

!!! important "Importante"
    Desde el ERP solo se puede crear la cuenta hospitalaria de tipo **Administrativo**. Para los demás roles (médico, enfermera, farmacéutico, cajero, etc.) el sistema exige un **perfil hospitalario** y rechaza la creación con el mensaje *Seleccione un perfil hospitalario para este usuario*. Esas cuentas se crean en **SIGARH › Mantenimiento**: Rol del sistema › Perfil de usuario › Usuario (manual SIG-04).

## 5.4 Ver y editar una cuenta

### Cuentas administradoras

<figure class="captura"><div class="marco"><img src="img/erp-usuario-detalle-admin.png" alt="Detalle de una cuenta administradora" data-ruta="/admin/usuarios/[id]?tipo=admin" data-perfil="Administrador (datos de prueba)"></div>
<figcaption>Figura 5. Detalle de una cuenta administradora.</figcaption></figure>

Puede cambiar el nombre, el correo, la contraseña (déjela vacía para no cambiarla), el estado y la opción de solo lectura. Pulse **Guardar cambios**.

Además dispone de dos botones:

- **Restablecer MFA.** Obliga a la persona a volver a configurar su aplicación autenticadora en su próximo ingreso. Úselo si perdió o cambió el teléfono. Pide confirmación y muestra *MFA restablecido* al terminar.
- **Eliminar.** Elimina la cuenta de forma definitiva, previa confirmación.

!!! important "Importante"
    No puede restablecer su **propio** MFA: el sistema responde que se lo pida a otro administrador. Por eso se recomienda mantener al menos dos administradores.

### Cuentas del hospital y de SIGARH

Se muestran en modo consulta con el aviso **Gestionada desde SIGARH**: panel, rol, empleado vinculado y estado. Desde aquí solo puede **Activar** o **Desactivar** la cuenta. Para cambiar su perfil o datos, use SIGARH.

## 5.5 Casos frecuentes

| Situación | Qué hacer |
|---|---|
| Un administrador perdió su teléfono | Otro administrador abre su cuenta y pulsa **Restablecer MFA**. |
| Una persona dejó el hospital | **Desactive** su cuenta (no se elimina; conserva la autoría). |
| Un auditor necesita revisar sin riesgo de cambios | Cree o edite su cuenta con **Solo lectura (auditor)**. |
| Aparece *Tu cuenta tiene acceso de solo lectura* | Su cuenta es de solo lectura; pida a un administrador completo que realice la acción. |
