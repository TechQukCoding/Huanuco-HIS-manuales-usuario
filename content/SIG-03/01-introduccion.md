# 1. Introducción

<p class="lead">Además de las personas, el hospital necesita sus <strong>espacios y listas de referencia</strong>: consultorios, pisos, camas, almacenes, tarifas, exámenes, diagnósticos. SIGARH es donde se configuran, y el Panel Hospitalario (HIS) los usa en su trabajo diario.</p>

## 1.1 Qué contiene

| Grupo del menú | Pantallas | Capítulo |
|---|---|---|
| **Infraestructura** | Catálogos, Consultorios | 2 |
| **Infraestructura Hospitalaria** | Pisos, Salas, Camas | 3 |
| **Config. Farmacia** | Almacenes / Farmacias, Medicamentos e Insumos | 4 |
| **Config. Financiera** | Seguros, Cajas, Tarifario | 5 |
| **Laboratorio** e **Imagenología** | Exámenes de Laboratorio, Exámenes de Imagenología | 6 |
| **General** | Diagnósticos CIE-10, Paquetes, Tiempos Procedimientos | 7 |

## 1.2 Orden recomendado de carga

Muchas pantallas dependen de otras. Siga este orden para no tener que volver atrás:

<div class="flujo">
<span class="paso ok">Catálogos</span><span class="flecha">›</span>
<span class="paso ok">Pisos</span><span class="flecha">›</span>
<span class="paso">Servicios (SIG-04)</span><span class="flecha">›</span>
<span class="paso">Salas</span><span class="flecha">›</span>
<span class="paso">Camas</span>
</div>
<div class="flujo">
<span class="paso">Consultorios</span><span class="flecha">›</span>
<span class="paso ko">Almacenes</span><span class="flecha">›</span>
<span class="paso ko">Medicamentos</span><span class="flecha">›</span>
<span class="paso">Seguros</span><span class="flecha">›</span>
<span class="paso">Cajas</span><span class="flecha">›</span>
<span class="paso">Tarifario</span>
</div>

## 1.3 Cómo se usan las listas

Todas las pantallas funcionan como las listas de Mantenimiento (manual SIG-04, capítulo 2): indicadores, búsqueda, pestañas de estado y menú **Ver y editar** / **Eliminar**. Los registros **inactivos** dejan de ofrecerse en los selectores, sin perder su historial.

!!! note "Nota"
    Su perfil debe incluir cada submódulo para ver su pantalla (manual SIG-04). Los módulos además deben estar activos para el hospital en el ERP (manual ERP-01).
