#!/usr/bin/env python3
"""Revisa los manuales antes de entregarlos.
  1) Caracteres que la fuente Inter no trae (salen como un hueco en el PDF: subíndices, flechas, etc.).
  2) Páginas casi vacías en medio de un manual (suele ser un aviso o una fila de tabla huérfana).
  3) Cuántas figuras llevan captura real y cuántas siguen como «CAPTURA PENDIENTE».
Uso (desde la raíz del repo, después de  python scripts/build.py):   python scripts/herramientas/revisar_pdfs.py"""
import pathlib, re, collections
from fontTools.ttLib import TTFont
import pymupdf

RAIZ = pathlib.Path(__file__).resolve().parents[2]
cmap = set(TTFont(RAIZ / "theme/fonts/inter-latin-400-normal.woff").getBestCmap().keys())
for carpeta in sorted((RAIZ / "content").iterdir()):
    if not (carpeta / "manual.yml").exists():
        continue
    md = list(carpeta.glob("*.md"))
    sin_glifo = collections.Counter(c for p in md for c in p.read_text(encoding="utf8") if ord(c) > 127 and ord(c) not in cmap)
    figuras = [re.search(r'src="img/([^"]+)"', t).group(1) for p in md
               for t in re.findall(r'<figure class="captura">.*?</figure>', p.read_text(encoding="utf8"), flags=re.S)
               if re.search(r'src="img/([^"]+)"', t)]
    reales = sum((carpeta / "img" / f).exists() for f in figuras)
    pdf = RAIZ / "dist" / (carpeta.name.split("-muestra")[0] + ".pdf")
    escasas = []
    if pdf.exists():
        d = pymupdf.open(pdf)
        escasas = [i + 1 for i, pg in enumerate(d) if len(pg.get_text().strip().split("\n")) < 14 and 0 < i < len(d) - 1]
    print(f"{carpeta.name:8} figuras {reales}/{len(figuras)} reales | sin glifo: {dict(sin_glifo) or 'ninguno'} | páginas escasas: {escasas or 'ninguna'}")
