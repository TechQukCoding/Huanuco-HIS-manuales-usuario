#!/usr/bin/env python3
"""Genera los PDF de los manuales.  Uso:  python scripts/build.py [CODIGO ...]
Cada manual vive en content/<CODIGO>/ con manual.yml + capítulos .md (orden alfabético)."""
import sys, re, pathlib, yaml, markdown, html, urllib.parse
from jinja2 import Template
from weasyprint import HTML

ROOT = pathlib.Path(__file__).resolve().parent.parent
PROY = yaml.safe_load((ROOT / "config/proyecto.yml").read_text(encoding="utf8"))

def slug(s):
    s = re.sub(r"[^\w\s-]", "", s.lower(), flags=re.U)
    return re.sub(r"[\s_]+", "-", s).strip("-")

PLANTILLA = Template(r"""<!doctype html><html lang="es"><head><meta charset="utf-8">
<title>{{ m.codigo }} · {{ m.titulo }}</title>
<link rel="stylesheet" href="theme/theme.css"></head><body>
<div class="running">{{ m.codigo }} · {{ m.titulo }}</div>

<section class="cover">
  <svg class="formas" viewBox="0 0 210 297" xmlns="http://www.w3.org/2000/svg">
    <polygon points="190,-34 252,28 190,90 128,28" fill="#00D7FE" stroke="#00D7FE" stroke-width="10" stroke-linejoin="round"/>
    <polygon points="206,52 250,96 206,140 162,96" fill="#B3A7FC" stroke="#B3A7FC" stroke-width="10" stroke-linejoin="round" opacity=".92"/>
    <polygon points="210,297 120,297 210,237" fill="#181980" stroke="#181980" stroke-width="8" stroke-linejoin="round"/>
    <polygon points="-6,303 -6,258 40,303" fill="#2B2BA8" stroke="#2B2BA8" stroke-width="8" stroke-linejoin="round"/>
  </svg>
  <div class="marca"><img src="theme/logo/techquk-icono.svg"><span>TECHQUK</span></div>
  <div class="bloque">
    <div class="codigo">{{ m.codigo }}</div>
    <div class="titulo">{{ m.titulo }}</div>
    <p class="subtitulo">{{ m.subtitulo }}</p>
  </div>
  <div class="para">Preparado para: {{ p.cliente }}</div>
  <div class="panel"><h5>Qué cubre este manual</h5>
    {% for x in m.modulos %}<span class="chip">{{ x }}</span>{% endfor %}
  </div>
  <div class="pie">Integramos tecnología,<br><b>impulsamos tu transformación digital.</b></div>
  <div class="version">VERSIÓN {{ m.version }} · {{ p.fecha_edicion }}</div>
</section>

<section class="ficha-doc">
  <h1 class="sin-salto" style="page-break-before:avoid">Ficha del documento</h1>
  <table class="ficha">
    <tr><th>Manual</th><td>{{ m.codigo }} — {{ m.titulo }}</td></tr>
    <tr><th>Producto</th><td>{{ p.producto }} · versión del sistema {{ p.version_sistema }}</td></tr>
    <tr><th>Dirigido a</th><td>{{ m.publico }}</td></tr>
    <tr><th>Versión / fecha</th><td>{{ m.version }} · {{ p.fecha_edicion }}</td></tr>
    <tr><th>Estado</th><td>{{ m.estado }}</td></tr>
    <tr><th>Proveedor</th><td>{{ p.proveedor }} — {{ p.contacto.correo }}</td></tr>
  </table>
  <h2>Cómo leer este manual</h2>
  <div class="tarjetas">
    <div class="tarjeta"><h4>Capturas numeradas</h4><p>Cada círculo de la imagen corresponde al mismo número de la leyenda que la acompaña.</p></div>
    <div class="tarjeta v"><h4>Pasos</h4><p>Los procedimientos se presentan como pasos numerados que puede seguir en el mismo orden.</p></div>
    <div class="tarjeta"><h4>Consejo</h4><p>Recomendaciones para trabajar con mayor rapidez o evitar errores.</p></div>
    <div class="tarjeta v"><h4>Importante</h4><p>Advertencias sobre acciones que no se pueden deshacer o que afectan a otros usuarios.</p></div>
  </div>
  <div class="admonition note"><p class="admonition-title">Nota</p>
  <p>Las pantallas disponibles dependen del perfil de cada usuario y de los módulos contratados por el hospital. Si no ve una opción descrita en este manual, solicite el permiso al administrador.</p></div>
</section>

<section class="indice"><h1>Contenido</h1>
<ul class="toc">
{% for c in capitulos %}{% for t in c.toc %}
<li class="n{{ t.level }}"><a href="#{{ t.id }}">{{ t.name }}</a></li>
{% endfor %}{% endfor %}
</ul></section>

{% for c in capitulos %}{{ c.html|safe }}{% endfor %}

<section class="back"><div class="centro">
  <img src="theme/logo/techquk-icono-fondo-oscuro.svg">
  <div class="back-titulo">Techquk, <em>empresa proveedora</em> de la solución</div>
  <p>Profesional · Cercana · Eficiente · Inteligente</p>
  <div class="datos">{{ p.contacto.correo }}<br>{{ p.contacto.web }}<br>{{ p.contacto.direccion }}</div>
</div></section>
</body></html>""")

PENDIENTES = []   # (manual, archivo, ruta, perfil, descripcion)

def placeholder(nombre, ruta):
    svg = (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1280 640" font-family="Inter,Arial,sans-serif">'
      '<rect width="1280" height="640" fill="#F4F6FB"/><rect width="230" height="640" fill="#fff"/>'
      '<rect x="24" y="24" width="30" height="30" rx="6" fill="#7C6EFF"/><rect x="66" y="32" width="90" height="14" rx="4" fill="#C9CFEA"/>'
      '<rect x="20" y="96" width="190" height="34" rx="8" fill="#ECE9FE"/><rect x="20" y="150" width="170" height="14" rx="4" fill="#E3E8F4"/>'
      '<rect x="20" y="184" width="170" height="14" rx="4" fill="#E3E8F4"/><rect x="20" y="218" width="170" height="14" rx="4" fill="#E3E8F4"/>'
      '<rect x="230" y="0" width="1050" height="64" fill="#fff"/><rect x="260" y="96" width="740" height="500" rx="14" fill="#fff" stroke="#E3E8F4"/>'
      '<rect x="1030" y="96" width="220" height="500" rx="14" fill="#fff" stroke="#E3E8F4"/>'
      '<rect x="380" y="250" width="520" height="56" rx="28" fill="#ECE9FE"/>'
      '<text x="640" y="286" text-anchor="middle" font-size="24" font-weight="700" fill="#181980" letter-spacing="2">CAPTURA PENDIENTE</text>'
      f'<text x="640" y="345" text-anchor="middle" font-size="20" fill="#5B5F8D">{html.escape(ruta or nombre)}</text></svg>')
    return "data:image/svg+xml;utf8," + urllib.parse.quote(svg)

def construir(carpeta: pathlib.Path):
    m = yaml.safe_load((carpeta / "manual.yml").read_text(encoding="utf8"))
    capitulos = []
    for i, md_file in enumerate(sorted(carpeta.glob("*.md"))):
        md = markdown.Markdown(
            extensions=["tables", "admonition", "attr_list", "md_in_html", "toc", "sane_lists"],
            extension_configs={"toc": {"slugify": (lambda v, s, i=i: f"c{i}-{slug(v)}"), "toc_depth": "1-2"}})
        cuerpo = md.convert(md_file.read_text(encoding="utf8"))
        toc = []
        def aplanar(tokens):
            for t in tokens:
                toc.append({"level": t["level"], "id": t["id"], "name": html.unescape(re.sub("<[^>]+>", "", t["name"]))})
                aplanar(t["children"])
        aplanar(md.toc_tokens)
        capitulos.append({"html": cuerpo, "toc": toc})
    out = PLANTILLA.render(m=m, p=PROY, capitulos=capitulos)
    # las rutas del repo son relativas a la raíz
    (ROOT / "dist").mkdir(exist_ok=True)
    (ROOT / f"dist/{m['codigo']}.html").write_text(out, encoding="utf8")
    # img/ de cada manual se resuelve respecto a su carpeta
    def resolver(mo):
        tag = mo.group(0); ar = re.search(r'src="img/([^"]+)"', tag)
        if not ar: return tag
        archivo = ar.group(1); ruta = (re.search(r'data-ruta="([^"]*)"', tag) or [None, ""])[1]
        perfil = (re.search(r'data-perfil="([^"]*)"', tag) or [None, ""])[1]
        desc = (re.search(r'alt="([^"]*)"', tag) or [None, ""])[1]
        real = carpeta / "img" / archivo
        if real.exists():
            return tag.replace('src="img/', f'src="content/{carpeta.name}/img/')
        PENDIENTES.append((m["codigo"], archivo, ruta, perfil, desc))
        return tag.replace(ar.group(0), f'src="{placeholder(archivo, ruta)}"')
    out = re.sub(r"<img[^>]*>", resolver, out)
    pdf = ROOT / f"dist/{m['codigo']}.pdf"
    HTML(string=out, base_url=str(ROOT) + "/").write_pdf(pdf)
    print("OK", pdf.relative_to(ROOT))

def escribir_pendientes():
    L = ["# Capturas pendientes\n", "Generado por `scripts/build.py`. Guardar cada archivo en `content/<manual>/img/`.\n",
         "| Manual | Archivo | Ruta | Perfil | Qué debe mostrar |", "|---|---|---|---|---|"]
    for r in PENDIENTES: L.append("| " + " | ".join(x.replace("|", "/") for x in r) + " |")
    (ROOT / "docs").mkdir(exist_ok=True)
    (ROOT / "docs/capturas-pendientes.md").write_text("\n".join(L) + "\n", encoding="utf8")
    print(f"Capturas pendientes: {len(PENDIENTES)} (docs/capturas-pendientes.md)")

if __name__ == "__main__":
    pedidos = sys.argv[1:]
    for c in sorted((ROOT / "content").iterdir()):
        if (c / "manual.yml").exists() and (not pedidos or any(c.name.startswith(p) for p in pedidos)):
            construir(c)
    escribir_pendientes()
