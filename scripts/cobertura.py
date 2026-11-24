#!/usr/bin/env python3
"""Verifica que cada grupo del menú del ERP esté asignado a un manual.
Uso: python scripts/cobertura.py /ruta/al/repo-del-ERP   (genera docs/cobertura.md)"""
import re, sys, pathlib, yaml
ROOT = pathlib.Path(__file__).resolve().parent.parent
erp = pathlib.Path(sys.argv[1]) / "frontend/composables"

def grupos(archivo, prefijo):
    t = (erp / archivo).read_text(encoding="utf8")
    res = {}
    for bloque in re.split(r"\n    \{\n      label: '", t)[1:]:
        nombre = bloque.split("'")[0]
        res[nombre] = len(re.findall(rf"path: [`']{prefijo}", bloque))
    return res

his, sig = grupos("useHospitalNav.ts", "/app"), grupos("useSigarhNav.ts", "/sigarh")
mapa = yaml.safe_load((ROOT / "config/manuales.yml").read_text(encoding="utf8"))
asig_his = {g: k for k, v in mapa.items() for g in v.get("his", [])}
asig_sig = {g: k for k, v in mapa.items() for g in v.get("sigarh", [])}
lineas = ["# Cobertura de manuales\n", "| Panel | Grupo del menú | Accesos | Manual |", "|---|---|:-:|---|"]
faltan = []
for panel, g, a in (("HIS", his, asig_his), ("SIGARH", sig, asig_sig)):
    for nombre, n in g.items():
        m = a.get(nombre, "**SIN MANUAL**")
        if nombre not in a: faltan.append((panel, nombre))
        lineas.append(f"| {panel} | {nombre} | {n} | {m} |")
sobran = [(p, x) for p, a, g in (("HIS", asig_his, his), ("SIGARH", asig_sig, sig)) for x in a if x not in g]
lineas += ["", f"HIS: {len(his)} grupos / {sum(his.values())} accesos · SIGARH: {len(sig)} grupos / {sum(sig.values())} accesos", ""]
(ROOT / "docs").mkdir(exist_ok=True)
(ROOT / "docs/cobertura.md").write_text("\n".join(lineas), encoding="utf8")
print("\n".join(lineas[-2:-1]))
print("Grupos sin manual:", faltan or "ninguno"); print("Nombres que no existen en el ERP:", sobran or "ninguno")
sys.exit(1 if faltan or sobran else 0)
