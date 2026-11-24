# 6. Ejemplo completo: dar acceso a un médico

Este ejemplo recorre los tres pasos para que un médico pueda ingresar al Panel Hospitalario y atender en Consulta Externa. Los nombres son de ejemplo.

## 6.1 Antes de empezar

- El módulo **Consulta Externa** debe estar activo para el hospital (ERP › *Datos del hospital › Módulos*, manual ERP-01).
- El médico debe estar registrado como **empleado** con la profesión **Médico Cirujano** (manual SIG-01).
- Usted necesita el permiso **Administrar Seguridad**.

## 6.2 Paso 1: crear el rol

<ol class="pasos">
<li>Vaya a <strong>Mantenimiento › Roles del sistema</strong> y pulse <strong>Nuevo rol</strong>.</li>
<li><strong>Código interno:</strong> <code>MEDICO_CE</code>. <strong>Nombre visible:</strong> <em>Médico de consulta externa</em>.</li>
<li><strong>Panel:</strong> <em>Hospitalario</em>. <strong>Tipo de cuenta hospitalaria:</strong> <em>Médico</em>.</li>
<li>En <strong>Módulos permitidos</strong>, marque <strong>Consulta Externa</strong> (despliéguelo si solo quiere ciertos submódulos).</li>
<li>Pulse <strong>Crear Rol</strong>.</li>
</ol>

## 6.3 Paso 2: crear el perfil

<ol class="pasos">
<li>Vaya a <strong>Perfiles de usuario</strong> y pulse <strong>Nuevo perfil</strong>.</li>
<li><strong>Nombre:</strong> <em>Médico de consulta externa</em>. <strong>Rol del sistema:</strong> <em>Médico de consulta externa (Hospitalario)</em>.</li>
<li>En <strong>Módulos con acceso</strong> deje marcado lo que el médico usará.</li>
<li>Pulse <strong>Crear perfil</strong>.</li>
</ol>

## 6.4 Paso 3: crear el usuario

<ol class="pasos">
<li>Vaya a <strong>Usuarios</strong> y pulse <strong>Nuevo usuario</strong>.</li>
<li><strong>Usuario:</strong> <code>jperez</code>. <strong>Correo:</strong> el correo institucional del médico.</li>
<li><strong>Empleado vinculado:</strong> elija al médico (el que tiene programación aprobada).</li>
<li><strong>Perfil:</strong> <em>Médico de consulta externa (Hospitalario)</em>.</li>
<li>Pulse <strong>Generar contraseña segura</strong>, <strong>cópiela</strong> y pulse <strong>Crear usuario</strong>.</li>
<li>Entregue la contraseña al médico por un canal seguro.</li>
</ol>

## 6.5 Qué hace el médico después

1. Ingresa por `/app/login` con su correo y contraseña (manual GEN-00).
2. En **Mi perfil** registra su **firma electrónica** y su **PIN** (manual GEN-00, sección 4.5).
3. Ve en su menú solo los módulos de su perfil.

!!! tip "Consejo"
    Para el administrador de SIGARH el procedimiento es el mismo, pero con **Panel: SIGARH**, los módulos que administrará (por ejemplo, **Mantenimiento**) y los **permisos de acción** que le correspondan.

## 6.6 Quién puede modificar qué

| Acción | Requiere |
|---|---|
| Ver roles, perfiles y usuarios | Módulo Mantenimiento |
| Crear o editar roles, perfiles y usuarios | Permiso **Administrar Seguridad** |
| Crear o editar catálogos | Permiso **Administrar Mantenimiento** |
| Conceder un permiso de acción en un rol | Tener usted mismo ese permiso |
| Cambiar las autorizaciones de su propia cuenta | **Otra** persona administradora |
