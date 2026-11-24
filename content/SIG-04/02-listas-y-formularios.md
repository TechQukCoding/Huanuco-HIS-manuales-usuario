# 2. Cómo funcionan las listas y formularios

Casi todas las pantallas de Mantenimiento comparten el mismo funcionamiento. Se explica una sola vez aquí y los capítulos siguientes solo describen lo propio de cada pantalla.

## 2.1 Las listas

<figure class="captura"><div class="marco"><img src="img/mant-lista-generica.png" alt="Lista de Mantenimiento con indicadores, búsqueda y pestañas" data-ruta="/sigarh/mantenimiento/profesiones" data-perfil="Administrador SIGARH (datos de prueba)"></div>
<figcaption>Figura 1. Lista de un catálogo de Mantenimiento.</figcaption></figure>

<ol class="leyenda">
<li><strong>Botón de alta.</strong> <em>Nuevo rol</em>, <em>Nuevo perfil</em>, <em>Nuevo usuario</em>, <em>Nuevo tipo</em>, etc.</li>
<li><strong>Indicadores.</strong> Total, Activos e Inactivos del catálogo.</li>
<li><strong>Búsqueda.</strong> Escriba el nombre o el código; la lista se actualiza sola a los 0,3 segundos.</li>
<li><strong>Pestañas de estado.</strong> Todos, Activos e Inactivos, con su cantidad.</li>
<li><strong>Tabla.</strong> Muestra 10 registros por página, con paginación al pie.</li>
<li><strong>Menú de acciones</strong> (tres puntos, al final de cada fila): <strong>Editar</strong> y <strong>Eliminar</strong>.</li>
</ol>

También puede abrir un registro haciendo clic en su fila. Si la lista no carga, aparece un aviso con el botón **Reintentar**.

## 2.2 Los formularios

| Botón | Qué hace |
|---|---|
| **Crear** (o *Crear rol*, *Crear usuario*…) | Guarda y vuelve a la lista. |
| **Crear y agregar otro** | Guarda y deja el formulario limpio para el siguiente registro; muestra *Se creó el perfil «…»*. |
| **Cancelar** | Vuelve a la lista sin guardar. |

El interruptor **Activo** de cada formulario decide si el registro puede asignarse: los inactivos no aparecen para asignar. En usuarios, perfiles y roles del sistema es la forma de retirarlos sin perder su historia.

## 2.3 Reglas sobre registros en uso y eliminación

Estas reglas protegen la información ya usada por otras pantallas:

| Situación | Qué ocurre |
|---|---|
| Un registro de catálogo **ya lo usan otros registros** y usted intenta cambiar sus datos | Solo puede cambiar la **Descripción**. Para lo demás el sistema responde *El catálogo ya está utilizado. Conserve el registro y cree una nueva versión*. |
| Intenta eliminar un catálogo en uso | *No puede eliminar un catálogo utilizado por otros registros*. |
| Intenta eliminar un **usuario, perfil o rol del sistema** | El sistema responde *Las cuentas y permisos se desactivan; no se eliminan para conservar auditoría*. Use el interruptor **Activo**. |
| Intenta eliminar una **profesión base** | *Las profesiones base se desactivan; no se eliminan*. |

!!! important "Importante"
    Aunque el menú de acciones muestre **Eliminar** en usuarios, perfiles y roles, esos registros **nunca se eliminan**: se desactivan, y la desactivación se puede revertir volviendo a activar el registro.

!!! tip "Consejo"
    Un registro duplicado se rechaza con *Ya existe un registro con ese …* o *Los datos duplican un registro o tienen una relación inválida*. Revise nombre y código antes de crear.
