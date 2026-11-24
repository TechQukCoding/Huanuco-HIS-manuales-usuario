# 6. Reportes y exportación de datos

## 6.1 Reporte mensual

**Reporte mensual** resume indicadores del hospital por mes y los compara con el mes anterior.

<figure class="captura"><div class="marco"><img src="img/erp-reporte-mensual.png" alt="Reporte mensual" data-ruta="/admin/reportes/mensuales" data-perfil="Administrador (datos de prueba)"></div>
<figcaption>Figura 6. Reporte mensual.</figcaption></figure>

<ol class="pasos">
<li>Entre a <strong>Reporte mensual</strong>. Se muestra el mes actual.</li>
<li>Con el selector de mes elija otro mes (no se pueden elegir meses futuros).</li>
<li>Revise los indicadores por área y su variación respecto al mes anterior.</li>
<li>Pulse <strong>Exportar CSV</strong> para descargar el reporte.</li>
</ol>

- Las áreas son: **Pacientes, Consulta Externa, Emergencia, Hospitalización, Centro Quirúrgico, Centro Obstétrico, UCI, Apoyo al diagnóstico, Farmacia, SIS y Sistema**.
- Cada indicador muestra su valor y una etiqueta de variación: verde con flecha hacia arriba si aumentó, roja si disminuyó, o *Sin cambio*. Si el mes anterior tenía datos, se indica también el porcentaje.
- Los meses son **meses calendario de Lima**. Al pie se indica cuándo se generó el reporte.
- El archivo se llama `reporte_mensual_AAAA-MM.csv` y tiene las columnas **Área**, **Indicador**, el mes elegido y el mes anterior.
- Si no se puede consultar la base del hospital, se avisa y solo se muestran datos del sistema.

## 6.2 Exportar datos

**Exportar datos** descarga información en formato CSV (compatible con Excel).

<figure class="captura"><div class="marco"><img src="img/erp-exportar-datos.png" alt="Exportar datos" data-ruta="/admin/reportes/exportar" data-perfil="Administrador (datos de prueba)"></div>
<figcaption>Figura 7. Exportar datos.</figcaption></figure>

| Opción | Contenido del archivo | Nombre del archivo |
|---|---|---|
| **Datos del hospital y módulos** | Identidad del hospital, registro MINSA y cada módulo del nivel con su estado | `hospital_AAAA-MM-DD.csv` |
| **Cuentas** | Cuentas admin, del Panel Hospitalario y de SIGARH, con su rol y estado | `cuentas_AAAA-MM-DD.csv` |
| **Auditoría (sistema y hospital)** | Eventos con fecha y hora, usuario, origen, acción, modelo, descripción e IP | `auditoria_AAAA-MM-DD.csv` |

<ol class="pasos">
<li>Elija qué desea exportar.</li>
<li>Si elige Auditoría, indique cuántos eventos recientes incluir: <strong>500</strong>, <strong>1 000</strong> o <strong>5 000</strong>.</li>
<li>Pulse <strong>Descargar CSV</strong>. Al terminar aparece <em>Archivo descargado</em>.</li>
</ol>

!!! note "Nota"
    Los archivos se guardan en UTF-8 con marca de orden de bytes para que Excel muestre bien las tildes. Los valores que comienzan con `=`, `+`, `-` o `@` se prefijan con un apóstrofo, para que Excel no los interprete como fórmulas.

!!! tip "Consejo"
    Si el sistema avisa *No se pudo consultar la base del hospital*, el archivo de cuentas incluirá solo las cuentas administradoras.
