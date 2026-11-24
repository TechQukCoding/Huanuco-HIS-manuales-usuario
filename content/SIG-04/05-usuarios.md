# 5. Usuarios

Un **usuario** es la cuenta de una persona. Recibe su rol y sus módulos del **perfil** que se le asigna. Esta pantalla administra tanto las cuentas de SIGARH como las del Panel Hospitalario (HIS).

Ruta: **Mantenimiento › Usuarios**.

## 5.1 Listado

<figure class="captura"><div class="marco"><img src="img/mant-usuarios-listado.png" alt="Listado de usuarios de SIGARH" data-ruta="/sigarh/mantenimiento/usuarios" data-perfil="Administrador SIGARH (datos de prueba)"></div>
<figcaption>Figura 4. Listado de usuarios.</figcaption></figure>

Muestra **Usuario** (con la etiqueta *Hospitalario* o *SIGARH*), **Correo** y **Estado**. Se busca por nombre o correo. Funciona como se explica en el capítulo 2.

## 5.2 Crear un usuario

<ol class="pasos">
<li>Pulse <strong>Nuevo usuario</strong>.</li>
<li>Escriba el <strong>Usuario (login)</strong> y el <strong>Correo electrónico</strong>.</li>
<li>Si la cuenta es de una persona del personal, elija el <strong>Empleado vinculado</strong>.</li>
<li>Elija el <strong>Perfil</strong>. El panel de la cuenta se toma del perfil.</li>
<li>Escriba la <strong>Contraseña</strong>, o pulse <strong>Generar contraseña segura</strong>.</li>
<li>Pulse <strong>Crear usuario</strong> (o <strong>Crear y agregar otro</strong>).</li>
</ol>

| Campo | Obligatorio | Descripción |
|---|:-:|---|
| Usuario (login) | <span class="si">Sí</span> | De 3 a 100 caracteres: letras, números, punto, guion y guion bajo (sin espacios). Se guarda en minúsculas. Ej.: `jperez`. |
| Correo electrónico | <span class="si">Sí</span> | Con formato de correo. Se guarda en minúsculas. Es el dato con el que la persona inicia sesión. |
| Empleado vinculado | <span class="no">Según el perfil</span> | Buscador sobre el personal registrado. Por defecto *Sin vincular*. Ver 5.3. |
| Perfil | <span class="si">Sí</span> | Solo se ofrecen perfiles activos, con su panel. El rol y los módulos se toman del perfil. |
| Contraseña | <span class="si">Sí</span> (al crear) | Ver 5.4. |
| Usuario activo | — | Un usuario inactivo no puede iniciar sesión. |

Mensajes de validación: *El usuario es requerido*, *El correo es requerido*, *El perfil es requerido*, *La contraseña no cumple los requisitos mínimos* y *La contraseña no puede ser igual al usuario ni al correo*. Si el usuario o el correo ya existen: *El usuario o correo ya existe en el panel hospitalario*.

## 5.3 Empleado vinculado

El vínculo con un empleado es indispensable para algunas cuentas:

| Cuenta | Requisito del empleado |
|---|---|
| **Médico** | Debe tener la profesión **Médico Cirujano**; elija al empleado que tiene la programación aprobada. Mensaje: *Vincule un empleado con profesión Médico Cirujano*. Sin este vínculo no puede firmar sus atenciones. |
| **Enfermería** | Debe tener la profesión **Enfermería**. Mensaje: *Vincule un empleado con profesión Enfermería*. |
| Cualquier cuenta con rol que restringe grupos ocupacionales | El empleado debe pertenecer a un grupo permitido por el rol: *El empleado no pertenece a los grupos permitidos por el rol*. |

El empleado se registra antes en **SIGARH › Recursos Humanos › Empleados** (manual SIG-01).

## 5.4 Contraseña

- Entre **8 y 72 caracteres**.
- Al menos una **minúscula**, una **mayúscula**, un **número** y un **carácter especial**. Debajo del campo, cada requisito se marca al cumplirse.
- **No puede ser igual al usuario ni al correo.**
- **Generar contraseña segura** crea una contraseña aleatoria de 16 caracteres y la muestra en pantalla.

!!! important "Importante"
    La contraseña generada **no vuelve a mostrarse** después de guardar. Cópiela antes de crear el usuario y entréguela a la persona por un canal seguro.

## 5.5 Editar y desactivar

Abra el usuario con **Editar**. En la edición, el campo se llama **Nueva contraseña**: déjelo vacío para no cambiarla.

!!! important "Importante"
    Si cambia la **contraseña, el perfil, el empleado vinculado, el estado, el usuario o el correo**, las **sesiones abiertas de esa cuenta se cierran** y la persona debe iniciar sesión de nuevo.

- **Desactivar** impide el ingreso, pero conserva todo lo que esa persona registró. Para retirar a alguien, desactive su cuenta: los usuarios **no se eliminan**.
- No puede modificar las autorizaciones de **su propia** cuenta: otra persona administradora debe hacerlo.

## 5.6 Cómo ingresa el usuario

- Las cuentas del **Panel Hospitalario** ingresan por `/app/login`; las de **SIGARH**, por `/sigarh/login` (manual GEN-00).
- La pantalla de ingreso pide el **correo institucional** con formato de correo.
- Si el perfil o el rol de la cuenta se desactivan, o el módulo requerido por el rol se deshabilita, el ingreso se rechaza (*El usuario requiere un perfil y rol activos* o *El módulo requerido por el rol no está habilitado*).
