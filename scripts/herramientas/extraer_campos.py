#!/usr/bin/env python3
"""Extrae de archivos .vue del ERP los textos que se documentan en un manual:
título, descripción, columnas, etiquetas, campos (con * si son obligatorios), ayudas, validaciones y placeholders.
Uso:  python scripts/herramientas/extraer_campos.py <carpeta-base> <archivo.vue> [<archivo.vue> ...]
Ej.:  python scripts/herramientas/extraer_campos.py ERP/frontend/pages/app emergencia/admisiones/create.vue
Es solo un ayudante: lo que se escribe en el manual debe contrastarse leyendo el código y los mensajes del backend."""
import re,sys,pathlib
base=pathlib.Path(sys.argv[1]); 
def uniq(l):
    o=[]; [o.append(x) for x in l if x not in o]; return o
for rel in sys.argv[2:]:
    f=base/rel
    if not f.exists(): print('##',rel,'(no existe)'); continue
    t=f.read_text(encoding='utf8')
    print('##',rel)
    comps=uniq(re.findall(r'<(S[A-Z][A-Za-z]+Campos|S[A-Z][A-Za-z]+Form[A-Za-z]*)',t))
    if comps: print('  componentes:',comps)
    for k,pat in (('title',r'<HospitalPage[^>]*?title="([^"]*)"'),('desc',r'<HospitalPage[^>]*?description="([^"]*)"')):
        m=re.search(pat,t,flags=re.S); 
        if m: print(' ',k,':',m.group(1)[:140])
    hdr=uniq(re.findall(r"header: '([^']+)'",t)); 
    if hdr: print('  columnas:',[h for h in hdr if h.strip()])
    kp=uniq(re.findall(r"label: '([^']{2,40})'",t)); 
    if kp: print('  labels:',kp[:30])
    ff=re.findall(r'<UFormField([^>]*)>',t)
    out=[]
    for a in ff:
        lab=re.search(r'label="([^"]*)"',a); 
        if not lab: continue
        req=' *' if re.search(r'\brequired\b',a) else ''
        h=re.search(r'(?:help|hint)="([^"]*)"',a)
        out.append(lab.group(1)+req+(' ['+h.group(1)[:90]+']' if h else ''))
    if out: print('  campos:',out)
    err=uniq(re.findall(r"'((?:El|La|Los|Las|Ingresa|Selecciona|Seleccione|Debe|No puede|Completa)[^']{4,100})'",t))
    if err: print('  validaciones:',err[:14])
    ph=uniq(re.findall(r'placeholder="([^"]{3,70})"',t)); 
    if ph: print('  placeholders:',ph[:8])
    ds=uniq(re.findall(r'description="([A-ZÁÉÍÓÚ][^"]{10,140})"',t))
    if ds: print('  textos:',ds[:5])
    rg=re.findall(r":reglas=\"\[([^\]]*)\]\"",t); 
    if rg: print('  reglas panel:',rg[0][:500])
    tp=re.findall(r'tip="([^"]*)"',t)
    if tp: print('  tip:',tp[0][:200])
