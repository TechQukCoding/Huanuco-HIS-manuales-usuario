# 3. Datos del hospital

Desde **Datos del hospital** se mantiene la identidad institucional, el registro MINSA, la misión y visión, y los módulos activos. Toda la pantalla se guarda con un solo botón.

<figure class="captura"><div class="marco"><img src="img/erp-hospital-identidad.png" alt="Datos del hospital, pestaña Identidad" data-ruta="/admin/hospital" data-perfil="Administrador (datos de prueba)"></div>
<figcaption>Figura 2. Datos del hospital, pestaña Identidad.</figcaption></figure>

<ol class="leyenda">
<li><strong>Encabezado.</strong> Nombre, nivel y código RENIPRESS (o el aviso <em>Falta código RENIPRESS</em>).</li>
<li><strong>Descartar / Guardar cambios.</strong> Se habilitan solo cuando hay cambios.</li>
<li><strong>Pestañas.</strong> Identidad, Misión y visión, Módulos.</li>
<li><strong>Identidad visual.</strong> Logo institucional.</li>
<li><strong>Información general y Registro MINSA.</strong></li>
</ol>

## 3.1 Pestaña Identidad

### Logo institucional

Suba una imagen **PNG, JPG o WebP de hasta 2 MB**. El sistema conserva la proporción de la imagen. El logo se usa en la portada pública, en los paneles y en los documentos del hospital.

### Información general

| Campo | Obligatorio | Descripción |
|---|:-:|---|
| Nombre oficial | <span class="si">Sí</span> | Nombre del establecimiento. Si queda vacío: *El nombre es requerido*. |
| Dominio | — | Solo lectura. Se asigna durante la instalación. |
| Nivel del establecimiento | — | Solo lectura. Es una configuración fija de esta edición. |
| RUC | <span class="no">No</span> | 11 dígitos. Si no cumple: *El RUC tiene 11 dígitos*. |
| Teléfono | <span class="no">No</span> | Teléfono de contacto. |
| Correo institucional | <span class="no">No</span> | Correo del hospital. |
| Dirección | <span class="no">No</span> | Dirección del establecimiento. |

### Registro MINSA

| Campo | Obligatorio | Descripción |
|---|:-:|---|
| Código RENIPRESS | <span class="no">No</span> | Código único de IPRESS de SUSALUD, **8 dígitos**. Si no cumple: *El código RENIPRESS tiene 8 dígitos*. Mientras falte, el Escritorio muestra una advertencia. |
| Resolución de categorización | <span class="no">No</span> | Hasta 120 caracteres. Ej.: R.D. N.° 000-2024-GRH-DRS. |
| DIRESA / GERESA | <span class="no">No</span> | Hasta 120 caracteres. |
| Red de salud | <span class="no">No</span> | Hasta 120 caracteres. |

## 3.2 Pestaña Misión y visión

Contiene los campos **Misión**, **Visión** y **Valores**. La misión se muestra en la portada pública del hospital.

## 3.3 Guardar los cambios

<ol class="pasos">
<li>Edite los campos que necesite. Aparecen habilitados <strong>Guardar cambios</strong> y <strong>Descartar</strong>.</li>
<li>Pulse <strong>Guardar cambios</strong>. El sistema primero guarda los datos del hospital y después los módulos.</li>
<li>Aparece el mensaje <em>Datos del hospital guardados</em>.</li>
<li>Para deshacer lo que no guardó, pulse <strong>Descartar</strong>: vuelve a cargar los datos guardados.</li>
</ol>

!!! important "Importante"
    Si los datos se guardan pero los módulos no, el sistema lo indica: *Los datos se guardaron, pero los módulos no*, seguido del motivo. Revise la pestaña **Módulos** y vuelva a guardar.

Si el hospital está instalándose, la pantalla muestra *El hospital todavía se está instalando*. Si la instalación falló, muestra *La instalación del hospital falló* con el motivo.

Al pie de la pantalla, **Accesos a los paneles** abre en otra pestaña la **Portada pública**, el **Panel Hospitalario** y **SIGARH**.
