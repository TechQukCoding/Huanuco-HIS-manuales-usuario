# 1. Introducción al panel ERP

<p class="lead">El panel ERP es la consola central desde la que se administra el hospital instalado: su identidad, los módulos que tiene contratados, las cuentas de acceso, los reportes y la auditoría de lo que ocurre en el sistema.</p>

## 1.1 Qué se hace en el ERP y qué no

| Se hace en el ERP | Se hace en otro panel |
|---|---|
| Registrar los datos del hospital y su logo | Crear empleados, roles de turno y catálogos de configuración: **SIGARH** |
| Activar y desactivar módulos del HIS y de SIGARH | Crear roles del sistema, perfiles de usuario y la mayoría de las cuentas del hospital: **SIGARH › Mantenimiento** |
| Crear y gestionar cuentas de administradores | Atender pacientes, farmacia, caja y demás procesos asistenciales: **HIS** |
| Consultar, activar o desactivar cuentas del hospital | |
| Consultar reportes mensuales y exportar datos | |
| Revisar la auditoría del sistema y del hospital | |

!!! note "Nota"
    En esta edición el sistema administra **un hospital**. El hospital se instala en el servidor con el script de instalación; el ERP permite completar y mantener sus datos, pero no instalarlo ni cambiar su nivel.

## 1.2 Tipos de cuenta administradora

| Tipo | Puede |
|---|---|
| **Administrador** | Consultar todo el panel y también crear, editar, activar, desactivar y eliminar. |
| **Administrador de solo lectura** (auditor) | Consultar y exportar todo el panel, pero no crear, editar, desactivar ni eliminar. El sistema rechaza esas acciones. |

## 1.3 Orden recomendado de puesta en marcha

<div class="flujo">
<span class="paso ok">1. Datos del hospital</span><span class="flecha">›</span>
<span class="paso ok">2. Activar módulos</span><span class="flecha">›</span>
<span class="paso">3. Cuentas administradoras</span><span class="flecha">›</span>
<span class="paso ko">4. Perfiles y usuarios en SIGARH</span>
</div>

1. Complete la identidad del hospital y su registro MINSA (capítulo 3).
2. Active los módulos que el hospital contrató (capítulo 4).
3. Cree las cuentas de los demás administradores (capítulo 5). Mantenga **al menos dos** cuentas administradoras: un administrador no puede restablecer su propia verificación MFA.
4. En SIGARH, el administrador del hospital crea los roles del sistema, los perfiles y los usuarios que usarán el HIS y SIGARH (manual SIG-04).

## 1.4 Acceso

El ingreso al ERP se describe en el manual **GEN-00** (verificación en dos pasos, perfil y contraseña). Este manual comienza una vez que usted ya está dentro.
