# 1. Conceptos básicos

<p class="lead">El ERP Hospitalario se compone de tres paneles independientes. Cada persona trabaja en el panel que corresponde a su cuenta y solo ve las opciones que su perfil le permite.</p>

## 1.1 Los tres paneles

| Panel | Para quién | El enlace termina en | Verificación al ingresar |
|---|---|---|---|
| **ERP** (administración central) | Administradores centrales del sistema | `/admin/login` | Contraseña y código MFA |
| **HIS** (Panel Hospitalario) | Personal asistencial y administrativo del hospital: admisión, consulta externa, emergencia, hospitalización, farmacia, caja y demás áreas | `/app/login` | Contraseña |
| **SIGARH** | Personal de recursos humanos, roles de turno e infraestructura y configuración institucional | `/sigarh/login` | Contraseña |

Su hospital le indicará el **enlace** de cada panel: es la dirección del sitio web del hospital seguida de ese final. Si no lo tiene, solicítelo al administrador de su hospital y guárdelo en los favoritos del navegador.

!!! important "Importante"
    Cada cuenta pertenece a **un solo panel**. Con una cuenta del HIS no se puede ingresar a SIGARH ni al ERP, y al revés. Si con una sesión abierta usted escribe la dirección de otro panel, el sistema cierra la sesión y lo lleva al inicio de sesión de ese panel.

## 1.2 Qué puede ver cada usuario

Las opciones del menú dependen de dos condiciones:

1. **Módulos contratados por el hospital.** Un módulo solo aparece si está activo para el hospital. Lo activa un administrador central en el ERP (*Datos del hospital › Módulos*).
2. **Perfil de la cuenta.** El perfil define el rol y los permisos de cada persona. Lo asigna el administrador del hospital desde SIGARH (*Mantenimiento › Roles del sistema, Perfiles de usuario y Usuarios*).

Por esta razón, dos personas del mismo hospital pueden ver menús distintos. Si falta una opción que usted necesita, no es una falla: debe solicitar el permiso a su administrador.

- **HIS:** si usted escribe la dirección de una pantalla para la que no tiene permiso, el sistema lo devuelve al escritorio.
- **SIGARH:** un grupo del menú aparece aunque usted tenga acceso a una sola de sus pantallas; dentro del grupo solo se listan las pantallas que puede usar.

## 1.3 Portada pública del hospital

Cada hospital dispone de una página pública en la raíz de su dirección, con su identidad institucional (logo, misión, visión y valores) e información de contacto. Esos datos se editan en el ERP (*Datos del hospital*). No requiere iniciar sesión.

## 1.4 Convenciones de este manual

- Los nombres de botones, menús y campos aparecen en **negrita**, tal como se ven en pantalla.
- Una ruta como *Datos del hospital › Módulos* indica el orden de las opciones a elegir.
- Los campos marcados como **obligatorios** no se pueden dejar vacíos.
