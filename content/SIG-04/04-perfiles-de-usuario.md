# 4. Perfiles de usuario

Un **perfil** es el conjunto de módulos que recibe un equipo de trabajo. Se apoya en un rol del sistema y **nunca puede tener más módulos que ese rol**. Cada usuario recibe sus accesos del perfil que se le asigna.

Ruta: **Mantenimiento › Perfiles de usuario**.

## 4.1 Listado

Muestra **Nombre** (con la etiqueta *Hospitalario* o *SIGARH*), **Descripción** y **Estado**. Funciona como se explica en el capítulo 2.

## 4.2 Crear un perfil

<figure class="captura"><div class="marco"><img src="img/mant-perfil-crear.png" alt="Formulario Nuevo perfil de usuario" data-ruta="/sigarh/mantenimiento/perfiles-usuario/create" data-perfil="Administrador SIGARH con Administrar Seguridad (datos de prueba)"></div>
<figcaption>Figura 3. Formulario Nuevo perfil de usuario.</figcaption></figure>

<ol class="pasos">
<li>Entre a <strong>Perfiles de usuario</strong> y pulse <strong>Nuevo perfil</strong>.</li>
<li>Escriba el <strong>Nombre</strong> y elija el <strong>Rol del sistema</strong>. Solo se ofrecen roles activos.</li>
<li>Marque los <strong>Módulos con acceso</strong>. El árbol solo muestra lo que el rol permite.</li>
<li>Pulse <strong>Crear perfil</strong> (o <strong>Crear y agregar otro</strong>).</li>
</ol>

| Campo | Obligatorio | Descripción |
|---|:-:|---|
| Nombre | <span class="si">Sí</span> | Por ejemplo, *Administrador*, *Supervisor*, *Consultor*. Si falta: *El nombre del perfil es requerido*. |
| Rol del sistema | <span class="si">Sí</span> | Define el techo de módulos del perfil. Se muestra con su panel, por ejemplo *Médico (Hospitalario)*. Si falta: *Seleccione un rol activo*. |
| Descripción | <span class="no">No</span> | Responsabilidades del perfil. |
| Módulos con acceso | — | Árbol de módulos y submódulos, acotado por el rol. Antes de elegir el rol indica *Seleccione primero un rol del sistema*. |
| Perfil activo | — | Los perfiles inactivos no estarán disponibles para asignar. |

Un panel lateral muestra el resumen: nombre, rol y cantidad de códigos de acceso marcados.

## 4.3 Reglas de los perfiles

- El perfil **hereda el panel** de su rol del sistema.
- **Nunca puede tener más módulos que su rol.** Si cambia el rol, se descartan los módulos que el nuevo rol no permite.
- Un perfil **inactivo no se puede asignar** a nuevos usuarios, y bloquea las solicitudes de las cuentas que ya lo tenían.
- Los módulos deben estar permitidos por el rol y habilitados en el hospital: *Los módulos deben estar permitidos por el rol y habilitados en el hospital*.
- Un perfil **sin rol** no puede tener módulos de acceso.

## 4.4 Editar un perfil

!!! important "Importante"
    **Editar un perfil afecta a todas las cuentas que lo tienen.** El cambio se aplica de inmediato.

| Regla | Mensaje del sistema |
|---|---|
| Un perfil **en uso** solo puede cambiar de rol si el nuevo rol conserva el mismo panel y tipo de cuenta. | *El nuevo rol debe conservar el panel y tipo de cuenta del perfil utilizado* |
| No puede modificar las autorizaciones del perfil que usted mismo usa. | *Otra persona administradora debe modificar sus propias autorizaciones* |

Para retirar un perfil, **desactívelo** (los perfiles no se eliminan).

!!! tip "Consejo"
    Cree perfiles **por función**, por ejemplo por especialidad o servicio, y limite los módulos a lo que cada equipo realmente usa.
