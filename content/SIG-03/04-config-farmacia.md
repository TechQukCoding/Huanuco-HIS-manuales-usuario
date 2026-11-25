# 4. Configuración de farmacia

Define **dónde** se guardan y despachan los productos (almacenes y farmacias) y **qué** productos existen (medicamentos e insumos). Las existencias, lotes y movimientos se manejan en el HIS (manual HIS-08); aquí solo se configura el catálogo.

## 4.1 Almacenes y farmacias

Ruta: **Config. Farmacia › Almacenes / Farmacias** (*Establecimientos y depósitos que manejan existencias*).

<figure class="captura"><div class="marco"><img src="img/farm-almacenes.png" alt="Almacenes y farmacias" data-ruta="/sigarh/config-farmacia/almacenes" data-perfil="Administrador SIGARH (datos de prueba)"></div>
<figcaption>Figura 3. Almacenes y farmacias.</figcaption></figure>

- **Indicadores:** Total, Activos, Despachan recetas e Inactivos.
- **Filtros:** buscador, **Todos los tipos** y **Despacho: todos** (con las opciones *Solo despachan recetas* y *No despachan*).
- **Tabla:** Código, Nombre, Tipo, Financiamiento, Despacha recetas y Estado.

| Campo | Obligatorio | Descripción |
|---|:-:|---|
| Código interno | <span class="si">Sí</span> | Hasta 20 caracteres, **único** en el hospital. Se guarda en mayúsculas. Ej.: *FAR-001*. |
| Nombre | <span class="si">Sí</span> | Hasta 100 caracteres. Ej.: *Farmacia Principal*. |
| Tipo | <span class="si">Sí</span> | **Farmacia**, **Almacén Central**, **Laboratorio** o **Dispensación**. |
| Fuente de financiamiento | <span class="no">No</span> | **SISMED**, **Donaciones** o **Mixto**. Por defecto *Sin especificar*. |
| Ubicación física | <span class="no">No</span> | Texto libre: **no se vincula** con pisos, salas ni camas. |
| Despacha recetas médicas | — | Si está activo, el almacén aparece en el selector de despacho. |
| Almacén activo | — | Los inactivos salen de los selectores. |

!!! tip "Consejo"
    Use prefijos consistentes: **FAR-** para farmacias, **ALM-** para almacenes y **DIS-** para dispensación.

!!! important "Importante"
    **Registrar un almacén no le asigna existencias**: eso ocurre por los procesos de inventario. Un almacén con stock mayor que cero **no se puede desactivar ni eliminar** (*No se puede desactivar: el almacén tiene existencias con stock mayor que cero*), ni uno usado en operaciones de farmacia (*No se puede eliminar: el almacén está siendo usado en operaciones de farmacia*). Si el código ya existe: *Ya existe un almacén con el código …*

## 4.2 Medicamentos e insumos

Ruta: **Config. Farmacia › Medicamentos e Insumos** (*Catálogo de productos que utiliza el hospital*).

- **Indicadores:** Productos, Controlados, Fiscalizados DIGEMID, Cadena de frío, Activos e Inactivos.
- **Filtros:** *Nombre, código, DCI…*, **Condición**, **Forma**, y los interruptores **Controlado**, **DIGEMID**, **SISMED** y **Cadena de frío**.
- **Tabla:** Código, Producto, Presentación, Forma, Cond. venta, Marcas y Mín. (stock mínimo). El menú ofrece **Ver y editar** y **Desactivar**.

### Alta por pasos

El alta de un producto es un asistente de **cuatro pasos** (en la edición se muestran como pestañas):

<div class="flujo">
<span class="paso ok">1. Identificación</span><span class="flecha">›</span>
<span class="paso ok">2. Registro y procedencia</span><span class="flecha">›</span>
<span class="paso">3. Clasificación y control</span><span class="flecha">›</span>
<span class="paso">4. Cadena de frío</span>
</div>

| Paso | Campos |
|---|---|
| **1. Identificación** | **Código interno / DIGEMID** (obligatorio), **Nombre comercial** (obligatorio), **Nombre genérico** (obligatorio), DCI (principio activo), Presentación, Unidad, Concentración, Forma farmacéutica, Vía de administración y Código ATC. |
| **2. Registro y procedencia** | N.° de registro sanitario, Laboratorio / fabricante, País de origen y **Condición de venta** (obligatoria). |
| **3. Clasificación y control** | Tipo de producto, Precio de referencia (S/), **Stock mínimo de alerta** (1 o mayor), Precio de referencia SISMED, y los interruptores **Requiere receta**, **Controlado**, **Fiscalizado DIGEMID**, **Reportar SISMED** y **Producto activo**. |
| **4. Cadena de frío** | **Requiere cadena de frío** y, si aplica, **Temperatura mínima** y **máxima** (°C). |

Listas de opciones:

- **Forma farmacéutica:** Tableta, Cápsula, Ampolla, Frasco ampolla, Jarabe, Suspensión, Solución, Crema, Pomada, Gel, Parche, Supositorio, Colirio, Inhalador, Polvo para reconstituir y Otro.
- **Vía de administración:** Oral, Intravenosa, Intramuscular, Subcutánea, Tópica, Oftálmica, Inhalada, Rectal, Sublingual, Nasal y Otro.
- **Condición de venta:** Sin receta, Con receta médica simple, Con receta retenida en farmacia y Bajo estricto control médico. Si la condición exige receta, **Requiere receta** se marca automáticamente.
- **Tipo de producto:** viene del catálogo *Tipos de producto* (capítulo 2). Si no hay ninguno, el formulario avisa *No hay tipos definidos*.

| Interruptor | Significado |
|---|---|
| Controlado | Psicotrópicos y estupefacientes. |
| Fiscalizado DIGEMID | Sujeto a reporte ante DIGEMID. |
| Reportar SISMED | Incluye el precio de referencia SISMED. |
| Producto activo | Los inactivos **no se pueden recetar ni despachar**. |

| Regla | Mensaje |
|---|---|
| Código repetido. | *Ya existe un producto con el código …* |
| La temperatura mínima no puede superar la máxima. | *La temperatura mínima no puede ser mayor que la máxima* |
| Stock mínimo no válido. | *El stock mínimo debe ser 1 o mayor* |
| El producto tiene existencias. | *No se puede desactivar: el producto tiene existencias con stock mayor que cero* |

!!! note "Nota"
    El **precio de referencia no es el precio de venta de cada lote**: el stock por lote, el vencimiento y el costo se manejan en el inventario del hospital. El precio SISMED solo aplica si se marca **Reportar SISMED**.
