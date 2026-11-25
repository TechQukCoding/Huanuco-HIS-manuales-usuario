# Traspaso del proyecto: manuales de usuario del ERP Hospitalario

Documento para retomar el trabajo en una sesión nueva. Léalo completo antes de escribir nada.

## 1. Objetivo
Manuales de usuario (PDF) del ERP Hospitalario de Techquk (paneles **ERP**, **SIGARH** y **HIS**) para el Hospital de Nivel II – Huánuco. Se redactan en Markdown + CSS y se exportan a PDF con el estilo del brochure de Techquk. **El contenido sale del código del ERP, no del brochure** (del brochure solo se tomó el estilo).

## 2. Estado (al cierre de esta sesión)
18 manuales planificados (`config/manuales.yml`: mapa manual → grupos del menú; `scripts/cobertura.py` verifica que ningún grupo quede sin manual).

| Estado | Manuales |
|---|---|
| **Redactados (borrador 0.9), 236 págs, en GitHub** | GEN-00, ERP-01, SIG-01, SIG-02, SIG-03, SIG-04, HIS-01, HIS-02, HIS-03, HIS-04, HIS-05 |
| **Pendientes (7)** | HIS-06, HIS-07, HIS-08, HIS-09, HIS-10, HIS-11, NUT-01 |

Todos los manuales hechos tienen **70 figuras** que hoy salen como «CAPTURA PENDIENTE». Las capturas reales las toma el usuario en su equipo con `scripts/capturas/capturar.py` y viven en `content/<MANUAL>/img/` (**pueden no estar subidas a GitHub**: compruebe con `git ls-tree -r origin/main --name-only | grep "/img/"`).

### Orden sugerido para lo pendiente (por impacto)
HIS-08 Farmacia · HIS-09 Caja, Facturación y SIS · HIS-07 Laboratorio e Imágenes · HIS-11 Archivo Clínico, Firma, Seguridad, General y Auditoría · HIS-10 Informes, Epidemiología y Registro HIS · HIS-06 Servicios especializados · NUT-01 Nutrición (HIS + SIGARH).

### HIS-06 (empezado solo en lectura)
Pantallas: **Hemodiálisis** (Programa, Agenda de sesiones, Puestos, Indicadores; componentes `HemodialisisPanel` 402 líneas, `HemodialisisPaciente` 299, `HemodialisisSesion` 142), **Banco de Sangre** (Solicitud Transfusional, Movimientos; `BancoSangrePanel` 547), **Medicina Física** (6 pantallas; `MedicinaFisicaPanel` 507) y **Salud Ambiental** (Defunciones; `SaludAmbientalPanel` 194). Backend en `backend/app/hospital/{hemodialisis,banco_sangre,medicina_fisica,salud_ambiental}/`.

## 3. Método de trabajo (repetirlo igual)
1. Listar las pantallas del grupo en `frontend/composables/useHospitalNav.ts` (o `useSigarhNav.ts`) y sus páginas en `frontend/pages/`. Muchas páginas son envoltorios de 4 líneas: el contenido real está en `frontend/components/*Panel*.vue`.
2. Extraer textos con `scripts/herramientas/extraer_campos.py` (títulos, columnas, campos obligatorios, ayudas).
3. Leer el backend (`backend/app/hospital/<modulo>/service.py`, `schemas.py`) y recoger **los mensajes exactos** (`HTTPException(...)`, `ValueError(...)`): son la tabla «Regla | Mensaje».
4. Redactar en `content/<CODIGO>/`: `manual.yml` + capítulos `01-…md` (orden alfabético).
5. `python scripts/build.py <CODIGO>` y `python scripts/herramientas/revisar_pdfs.py` (glifos y páginas casi vacías).
6. Actualizar la tabla de estado de `README.md` y añadir puntos dudosos a `docs/pendientes-de-validacion.md`.
7. **Mostrar al usuario y pedir su aprobación antes de cada `git push`** (regla explícita del usuario).

### Estructura de un manual
`01-introduccion` (qué contiene, recorrido con diagrama de flujo, qué debe estar listo antes) · un capítulo por pantalla o grupo (ruta, figura, pasos, tabla de campos `Campo | Obligatorio | Descripción`, tabla de reglas `Regla | Mensaje`, avisos) · último capítulo «Problemas frecuentes» (`Situación | Causa | Qué hacer`). Referencias cruzadas a otros manuales por código (p. ej. «manual SIG-04, capítulo 3»). Tono formal («usted»).

### Componentes de maquetación (Markdown + HTML)
- Avisos: `!!! important "Importante"`, `!!! tip "Consejo"`, `!!! note "Nota"` (contenido sangrado 4 espacios).
- Pasos: `<ol class="pasos"><li>…</li></ol>`. **Dentro de HTML no se renderiza `**negrita**`: use `<strong>`.**
- Flujo: `<div class="flujo"><span class="paso ok">…</span><span class="flecha">›</span>…</div>`.
- Figura: `<figure class="captura"><div class="marco"><img src="img/<archivo>.png" alt="…" data-ruta="/ruta" data-perfil="…"></div><figcaption>Figura N. …</figcaption></figure>` (el `data-*` alimenta `docs/capturas-pendientes.md`).
- Leyenda numerada: `<ol class="leyenda">` (hoy sin números de llamada sobre la imagen).

## 4. Lecciones aprendidas (evitan repetir errores)
- **Python 3.11 del usuario:** no repetir el mismo tipo de comillas dentro de un `f"…{…"…"}"`. Probar con 3.11 (`uv run --python 3.11 …`).
- **Fuente Inter:** no tiene `₂ ′ ⋮ → ⇄ ⌘ −`. Escribir `SO2`, `1 y 5 minutos`, `›`, `-3`. `revisar_pdfs.py` lo detecta.
- **Páginas casi vacías:** un aviso o una fila final que se desborda. Mover el aviso antes de la tabla o recortar texto.
- **Una captura con `AVISO` se guarda igual** (puede ser la pantalla de login): bórrela y repita con `--rehacer`.
- **No inventar:** si algo no se pudo confirmar en el código, anotarlo en `docs/pendientes-de-validacion.md` y no afirmarlo.
- **Menús sin tilde en la interfaz** («Creacion de Roles», «Imagenologia», «Hospitalizacion»…): los manuales las escriben con tilde; pendiente un repaso para que coincidan literalmente con la pantalla.

## 5. Capturas y entorno de pruebas
Guía paso a paso: `docs/GUIA-CAPTURAS.md` y `scripts/capturas/README.md`. Resumen:
- La app corre en el equipo del usuario (Windows, `cmd`): Docker (Postgres, Redis, RabbitMQ; el Postgres se movió al puerto **5434** porque en el equipo hay un PostgreSQL de Windows en el 5432 — confirmar con `DATABASE_URL` del `.env`), backend `uvicorn` y frontend `npm run preview` en `localhost:3000`.
- Cuentas de prueba: HIS `jefatura.prueba@prueba.huanuco.techquk.com` y roles (`medico.interna@…`, `enfermera.flores@…`, `admision.chavez@…`), todas con clave de prueba del script `seed_datos_prueba`; SIGARH `sigarh@prueba.huanuco.techquk.com`; ERP `admin@prueba.huanuco.techquk.com` (con MFA; el usuario usó un parche local `ERP_SIN_MFA`, **no incluido en el repo**).
- Las pantallas con `[id]` y las que necesitan datos se resuelven con **archivos SQL de datos ficticios** (`scripts/capturas/datos_*_prueba.sql`, validados contra el esquema real) y líneas en `config/capturas.local.yml` (no se sube a git).
- Faltan datos de prueba para HIS-05 en adelante (quirófano, obstetricia, esterilización, patología, farmacia, caja…): crear un SQL por módulo con el mismo método.
- Pendiente a mano: `gen-login-erp-mfa-qr.png` y `ce-receta.png` (paso 6 de la atención del médico).

## 6. Pendientes finales
1. Redactar los 7 manuales restantes.
2. Subir las capturas del usuario, tomar las faltantes y regenerar los PDF.
3. Colocar **números de llamada** sobre las capturas (`<span class="pin">` con posiciones en %).
4. Repaso de coherencia: nombres exactos de menú, glosario único, enlaces entre manuales.
5. Validación con la aplicación corriendo: `docs/pendientes-de-validacion.md` (más de 59 puntos, incluidas **posibles mejoras del producto** que conviene pasar a desarrollo).

## 7. Prompt para iniciar la sesión nueva
Está al final de este archivo y en la respuesta de la sesión anterior.

```
Continúa el proyecto de manuales de usuario del ERP Hospitalario. Repo: TechQukCoding/Huanuco-HIS-manuales-usuario (te paso un token de GitHub de solo contenido y el ZIP del ERP). Primero clona el repo y lee docs/CONTINUACION.md, README.md, config/manuales.yml y docs/pendientes-de-validacion.md. Están redactados 11 de 18 manuales; faltan HIS-06 a HIS-11 y NUT-01. Sigue el método y el estilo de docs/CONTINUACION.md y de los manuales existentes, el contenido sale del código del ERP, y pídeme aprobación antes de cada git push.
```
