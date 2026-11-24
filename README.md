# Manuales de usuario · ERP Hospitalario (Techquk)

Documentación de usuario del ERP Hospitalario (paneles **ERP**, **HIS** y **SIGARH**).
Se redacta en Markdown + CSS y se exporta a PDF con el estilo del brochure de Techquk.

## Uso rápido

```bash
pip install weasyprint markdown jinja2 pyyaml pymupdf
python scripts/build.py            # genera dist/*.pdf de todos los manuales
python scripts/build.py HIS-08     # solo uno
python scripts/cobertura.py ../ERP--Hospital-Nivel-II--Huanuco-   # ¿algún grupo del menú sin manual?
```

No requiere navegador: el PDF se genera con WeasyPrint.

## Estructura

```
config/proyecto.yml     datos del cliente/versión (portada, contraportada)
config/manuales.yml     mapa de los 18 manuales -> grupos del menú del ERP
theme/                  theme.css, fuentes (Sora, Inter) y logos
content/<CODIGO>/       manual.yml + capítulos .md (orden alfabético) + img/
capturas/               capturas originales por manual
scripts/                build.py, cobertura.py
docs/cobertura.md       generado: grupo del ERP -> manual
dist/                   salida (PDF ignorados por git; publicar como releases)
```

## Los 18 manuales

GEN-00 · ERP-01 · SIG-01…04 · HIS-01…11 · NUT-01 (ver `config/manuales.yml`).

## Reglas de estilo

- Marca Techquk; el hospital aparece solo como "Preparado para" (`config/proyecto.yml`).
- Capturas con llamadas numeradas (`<span class="pin">`) y su leyenda (`<ol class="leyenda">`).
- Procedimientos en `<ol class="pasos">`; avisos con `!!! tip|important|note`.
- Solo datos ficticios en capturas y ejemplos. Nunca datos reales de pacientes.
- Cada manual indica la versión del ERP contra la que se validó.

## Estado

| Manual | Estado |
|---|---|
| ERP-01 | Muestra de estilo (`content/ERP-01-muestra`), contenido preliminar |
| Resto | Pendiente |
