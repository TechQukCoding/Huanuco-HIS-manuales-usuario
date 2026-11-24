# 4. Módulos

Los módulos son las funciones que el hospital contrata. Un módulo inactivo no aparece en los menús de nadie, aunque el perfil de un usuario lo incluya.

## 4.1 Consultar el catálogo

La opción **Módulos** del menú muestra el catálogo disponible para el nivel del hospital.

<figure class="captura"><div class="marco"><img src="img/erp-modulos-catalogo.png" alt="Catálogo de módulos" data-ruta="/admin/modulos" data-perfil="Administrador (datos de prueba)"></div>
<figcaption>Figura 3. Catálogo de módulos del hospital.</figcaption></figure>

- Tres tarjetas resumen: **Disponibles**, **Activos** e **Inactivos**.
- Filtros: búsqueda por nombre o código, **Panel** (*Ambos paneles*, *Panel Hospitalario*, *SIGARH*) y **Estado** (*Todos*, *Activos*, *No activos*).
- La tabla muestra **Módulo**, **Código**, **Panel** y **En el hospital** (*Activo* / *No activo*).

Esta pantalla es de consulta. Para cambiar el estado use el botón **Configurar módulos**, que lleva a la pestaña *Módulos* de *Datos del hospital*.

## 4.2 Activar y desactivar módulos

<ol class="pasos">
<li>Entre a <strong>Datos del hospital</strong> y abra la pestaña <strong>Módulos</strong>.</li>
<li>Use el buscador <strong>Buscar módulo</strong> si lo necesita. Los módulos se agrupan en <strong>Panel Hospitalario</strong> y <strong>SIGARH</strong>; cada grupo indica cuántos están activos sobre el total (por ejemplo, 12 / 35).</li>
<li>Active o desactive el interruptor de cada módulo.</li>
<li>Pulse <strong>Guardar cambios</strong>. Hasta que guarde, los cambios no se aplican.</li>
</ol>

### Dependencias entre módulos

Algunos módulos requieren otros. El sistema lo resuelve automáticamente:

| Si usted… | El sistema… | Aviso |
|---|---|---|
| Activa un módulo que requiere otros | Activa también los requeridos | *Se activaron módulos requeridos* y la lista |
| Desactiva un módulo del que otros dependen | Desactiva también los dependientes | *Se desactivaron módulos que dependían de este* y la lista |

Bajo el nombre de cada módulo aparece **Requiere:** con los módulos de los que depende.

!!! important "Importante"
    Desactivar un módulo corta de inmediato el acceso de todos los usuarios a esas pantallas. Revise la lista de módulos dependientes que el sistema desactiva antes de guardar.

!!! note "Nota"
    Los módulos se contratan completos. Qué pantallas concretas ve cada persona dentro de un módulo lo define su perfil, que se administra en SIGARH.
