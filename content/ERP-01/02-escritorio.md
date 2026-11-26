# 2. Escritorio

El **Escritorio** es la primera pantalla del ERP. Resume el estado del hospital y ofrece accesos rápidos.

<figure class="captura"><div class="marco"><img src="img/erp-escritorio.png" alt="Escritorio del panel ERP" data-ruta="/admin" data-perfil="Administrador (datos de prueba)"></div>
<figcaption>Figura 1. Escritorio del panel ERP.</figcaption></figure>

<ol class="leyenda">
<li><strong>Cabecera.</strong> Logo, nombre y nivel del hospital, código RENIPRESS, fecha de hoy y estado de los servicios.</li>
<li><strong>Accesos rápidos.</strong> Datos del hospital, Auditoría, Reporte mensual y Nueva cuenta.</li>
<li><strong>Alertas.</strong> Avisos que requieren acción (ver 2.2).</li>
<li><strong>Indicadores principales.</strong> Tarjetas que llevan a la pantalla correspondiente.</li>
<li><strong>Operación del hospital.</strong> Ocupación de camas, cifras del día y gráfico de los últimos 7 días.</li>
</ol>

## 2.1 Cabecera y estado de servicios

- Si el hospital no tiene código RENIPRESS, aparece el enlace **Registrar código RENIPRESS**, que lleva a *Datos del hospital*.
- Debajo de la fecha se indica el estado de los servicios: **Servicios operativos** o **Hay servicios por revisar**. Mientras se comprueba, dice *Verificando servicios…*.

## 2.2 Alertas

| Alerta | Cuándo aparece | Qué hacer |
|---|---|---|
| *El hospital no terminó de instalarse* / *La instalación del hospital falló* | La instalación no concluyó. | Pulse **Revisar** y, si falló, comuníquese con soporte técnico de Techquk para que repitan la instalación. |
| *No se pudo consultar la base del hospital* | El ERP no logra leer los datos del hospital. Las cifras de cuentas y la actividad no están disponibles. | Avise a soporte técnico. |
| *N evento(s) de auditoría por recuperar* | Hay eventos de auditoría pendientes de registrarse. | Pulse **Revisar** y reintente desde *Auditoría del sistema* (capítulo 7). |

## 2.3 Indicadores principales

| Tarjeta | Qué muestra | Lleva a |
|---|---|---|
| **Usuarios del hospital** | Total de cuentas, con el desglose entre Panel Hospitalario y SIGARH. | Usuarios del hospital |
| **Administradores** | Total de cuentas administradoras y cuántas tienen acceso activo. | Administradores |
| **Módulos activos** | Módulos activos frente a los disponibles para el nivel del hospital. | Módulos |
| **Eventos de auditoría** | Eventos registrados en las últimas 24 horas. | Auditoría del hospital |

## 2.4 Operación del hospital

- **Ocupación de camas.** Barras con camas ocupadas sobre el total y el porcentaje de ocupación. Cambia de color al llegar al 75 % (advertencia) y al 90 % (crítico). Si no hay camas registradas, indica *Sin camas registradas en SIGARH*.
- **Cifras del día.** Internados, Citas de hoy, Emergencias en 24 h, Pacientes, **FUA por enviar** y **FUA observados** (esta última se resalta cuando es mayor que cero).
- **Últimos 7 días.** Gráfico de **Emergencias** e **Ingresos a hospitalización**.

Debajo se muestran además un resumen de las cuentas creadas recientemente (con el enlace **Ver todas**) y de la auditoría.
