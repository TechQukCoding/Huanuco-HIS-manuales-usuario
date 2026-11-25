# 1. Introducción

<p class="lead">Admisión es la <strong>puerta de entrada</strong> del paciente: aquí se registra su identidad, se le asigna una cita, se ordena su espera y, si hace falta, se le deriva a otro establecimiento.</p>

## 1.1 Qué contiene

| Grupo del menú | Pantallas | Capítulo |
|---|---|---|
| **Admisión** | Pacientes | 2 |
| | Agendamiento, Citados | 3 |
| | Programación Médica | 4 |
| | Altas de Pacientes, Lista de Espera, Anuncios, Mensajito | 5 |
| **Turnero** | Emitir Ticket, Llamado, Configuración | 6 |
| **Referencias** | Referencias | 7 |
| **Servicio Social** | Servicio Social | 8 |

## 1.2 El camino del paciente

<div class="flujo">
<span class="paso ok">Registrar paciente</span><span class="flecha">›</span>
<span class="paso ok">Agendar cita</span><span class="flecha">›</span>
<span class="paso">Ticket y espera</span><span class="flecha">›</span>
<span class="paso ko">Confirmar y atender (HIS-02)</span>
</div>

1. **Registro:** se busca al paciente; si no existe, se registra (capítulo 2).
2. **Cita:** se elige un cupo de una programación médica y se agenda (capítulos 3 y 4).
3. **Llegada:** en el kiosko o con el personal se emite un ticket y la pantalla de sala lo llama (capítulo 6).
4. **Atención:** la cita se confirma, se hace el triaje y el médico atiende (manual HIS-02).

## 1.3 Qué debe estar listo antes

- **Roles de turno aprobados** en SIGARH (manual SIG-02): sin ellos no hay programación ni cupos.
- **Servicios y especialidades** configurados (SIG-04) y **consultorios** (SIG-03).
- **Seguros** registrados (SIG-03) para elegir la fuente de financiamiento de la cita.

!!! note "Nota"
    Las pantallas que verá dependen de su perfil (manual SIG-04). Admisión requiere el módulo *Admisión*; Turnero, Referencias y Servicio Social son módulos aparte que el hospital puede o no tener activos (manual ERP-01).
