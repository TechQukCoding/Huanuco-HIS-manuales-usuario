# 1. Introducción

<p class="lead">El módulo <strong>Mantenimiento</strong> de SIGARH es donde el administrador del hospital define <strong>quién puede entrar al sistema y qué puede hacer</strong>, y donde mantiene los catálogos que el resto de SIGARH y del HIS utilizan.</p>

## 1.1 Qué contiene

| Grupo | Pantallas | Capítulo |
|---|---|---|
| **Seguridad** | Roles del sistema, Perfiles de usuario, Usuarios | 3, 4 y 5 |
| **Estructura del hospital** | Departamentos, Servicios (UPSS y servicios), Dependencias | 7 |
| **Personal** | Tipos de trabajador, Niveles remunerativos, Profesiones, Grupos ocupacionales | 7 |
| **Guardias y actividades** | Tipos de guardia, Horarios de guardia, Guardias valorizadas, Tipos de actividad, Actividades | 7 |

## 1.2 Roles › Perfiles › Usuarios

Toda cuenta del Panel Hospitalario (HIS) y de SIGARH se crea en tres pasos encadenados. **Cada paso se apoya en el anterior**, por eso no se puede saltar ninguno.

<div class="flujo">
<span class="paso ok">1. Rol del sistema</span><span class="flecha">›</span>
<span class="paso ok">2. Perfil de usuario</span><span class="flecha">›</span>
<span class="paso">3. Usuario</span>
</div>

| Paso | Qué define | Ejemplo |
|---|---|---|
| **Rol del sistema** | El **techo** de acceso: qué módulos, submódulos y acciones se pueden llegar a conceder, en qué panel y para qué tipo de cuenta. | Rol *Médico de consulta externa*, panel Hospitalario, tipo Médico. |
| **Perfil de usuario** | Un recorte del rol: los módulos que realmente usará un equipo. Nunca puede tener más que su rol. | Perfil *Médico de consulta externa* con solo Consulta Externa. |
| **Usuario** | La cuenta de una persona, con su usuario, correo, contraseña y el perfil que recibe. | *jperez*, perfil *Médico de consulta externa*, vinculado al empleado correspondiente. |

!!! note "Nota"
    Toda la gestión de cuentas del hospital se hace aquí, en SIGARH. Desde el ERP solo se consultan, activan o desactivan (manual ERP-01).

## 1.3 Permisos necesarios

Para entrar a estas pantallas su perfil debe incluir el módulo **Mantenimiento**. Además, la creación y edición dependen de dos **permisos de acción** que concede el rol:

| Permiso de acción | Permite |
|---|---|
| **Administrar Seguridad** | Crear, editar y desactivar **Usuarios, Perfiles y Roles del sistema**. Sin este permiso solo puede verlos. |
| **Administrar Mantenimiento** | Crear y editar los **catálogos** de Mantenimiento. |

Si le falta el permiso, los botones **Nuevo…** aparecen deshabilitados y, al pasar el cursor, el sistema indica *Necesitas el permiso Administrar Seguridad*. Si abre una pantalla de creación por la dirección, lo devuelve al listado.

!!! important "Importante"
    **No se puede otorgar lo que no se tiene.** Al crear o editar un rol, el sistema rechaza permisos de acción o alcance global que usted mismo no posea (*No puede otorgar permisos que usted mismo no tiene*). Así nadie puede crear una cuenta con más poder que el suyo.

## 1.4 Orden recomendado de puesta en marcha

1. Confirmar que el ERP tenga activos los módulos que el hospital usará (manual ERP-01).
2. Cargar los catálogos de personal y estructura (capítulo 7): grupos ocupacionales, profesiones, departamentos, servicios y demás.
3. Crear los **roles del sistema** necesarios (capítulo 3).
4. Crear los **perfiles** por función (capítulo 4).
5. Crear los **usuarios** y asignarles su perfil (capítulo 5).
