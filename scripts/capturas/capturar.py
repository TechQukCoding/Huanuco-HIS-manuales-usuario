#!/usr/bin/env python3
"""Toma las capturas de pantalla de los manuales con Playwright.

Lee docs/capturas-pendientes.md (que genera scripts/build.py), inicia sesión en cada panel
con una cuenta de PRUEBA y guarda cada PNG en content/<MANUAL>/img/<archivo>.

Uso:
  python scripts/capturas/capturar.py --lista                 # solo muestra qué se tomaría
  python scripts/capturas/capturar.py                         # todas las pendientes
  python scripts/capturas/capturar.py --manual HIS-01         # solo un manual
  python scripts/capturas/capturar.py --archivo adm-citados.png
  python scripts/capturas/capturar.py --headed                # con navegador visible
  python scripts/capturas/capturar.py --rehacer               # vuelve a tomar las que ya existen
"""
import argparse, os, re, sys, pathlib, time
import yaml

ROOT = pathlib.Path(__file__).resolve().parents[2]
CFG = yaml.safe_load((ROOT / "config/capturas.yml").read_text(encoding="utf8"))


def leer_pendientes():
    filas = []
    for l in (ROOT / "docs/capturas-pendientes.md").read_text(encoding="utf8").splitlines():
        if l.startswith("| ") and not l.startswith("| Manual") and not l.startswith("|---"):
            c = [x.strip() for x in l.strip().strip("|").split("|")]
            if len(c) >= 5:
                filas.append(dict(manual=c[0], archivo=c[1], ruta=c[2], perfil=c[3], desc=c[4]))
    return filas


def panel_de(ruta):
    for nombre, p in CFG["paneles"].items():
        if ruta.startswith(p["prefijo"]):
            return nombre
    return None


def credenciales(panel):
    pre = CFG["paneles"][panel]["env"]
    usr, pwd = os.environ.get(pre + "_USER"), os.environ.get(pre + "_PASS")
    if not usr or not pwd:
        sys.exit(f"Faltan las variables de entorno {pre}_USER y {pre}_PASS (cuenta de PRUEBA del panel {panel}).")
    return usr, pwd, os.environ.get(pre + "_TOTP")


def iniciar_sesion(pw, browser, panel):
    from playwright.sync_api import TimeoutError as PWTimeout
    ctx = browser.new_context(viewport={"width": CFG["viewport"]["ancho"], "height": CFG["viewport"]["alto"]}, locale="es-PE")
    page = ctx.new_page()
    usr, pwd, totp = credenciales(panel)
    page.goto(CFG["base_url"] + CFG["paneles"][panel]["login"])
    page.get_by_label(re.compile("correo", re.I)).first.fill(usr)
    page.get_by_label(re.compile("contraseña", re.I)).first.fill(pwd)
    page.get_by_role("button", name=re.compile("iniciar sesión|ingresar", re.I)).first.click()
    if panel == "admin":
        # Verificación en dos pasos: el código de 6 dígitos se completa solo al escribir el sexto número.
        try:
            page.wait_for_timeout(1200)
            if "login" in page.url:
                if not totp:
                    sys.exit("El panel ERP pide MFA: defina CAP_ADMIN_TOTP (secreto TOTP de la cuenta de prueba).")
                import pyotp
                page.keyboard.press("Tab")
                page.keyboard.type(pyotp.TOTP(totp).now(), delay=60)
                page.get_by_role("button", name=re.compile("verificar", re.I)).first.click(timeout=3000)
        except PWTimeout:
            pass
    try:
        page.wait_for_url(lambda u: "login" not in u, timeout=15000)
    except PWTimeout:
        sys.exit(f"No se pudo iniciar sesión en el panel {panel}. Revise usuario, contraseña y base_url.")
    return ctx


def resolver_ruta(page, fila):
    """Devuelve la dirección final. Para rutas con [id] usa el override de config o entra al primer registro."""
    ruta = CFG.get("rutas", {}).get(fila["archivo"]) or fila["ruta"]
    if "[id]" not in ruta:
        return ruta
    lista = re.sub(r"/\[id\].*$", "", ruta)
    page.goto(CFG["base_url"] + lista)
    page.wait_for_load_state("networkidle")
    fila_tabla = page.locator("table tbody tr").first
    if fila_tabla.count() == 0:
        return None
    fila_tabla.click()
    page.wait_for_load_state("networkidle")
    return page.url.replace(CFG["base_url"], "")


def capturar(page, fila, destino):
    ruta = resolver_ruta(page, fila)
    if ruta is None:
        return "no hay registros de prueba para abrir"
    if not page.url.endswith(ruta):
        page.goto(CFG["base_url"] + ruta)
    page.wait_for_load_state("networkidle")
    for texto in CFG.get("clics", {}).get(fila["archivo"], []) or []:
        page.get_by_text(texto, exact=False).first.click()
        page.wait_for_load_state("networkidle")
    page.wait_for_timeout(CFG.get("pausa_ms", 900))
    destino.parent.mkdir(parents=True, exist_ok=True)
    page.screenshot(path=str(destino), full_page=False)
    return None


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--manual"); ap.add_argument("--archivo")
    ap.add_argument("--lista", action="store_true"); ap.add_argument("--headed", action="store_true")
    ap.add_argument("--rehacer", action="store_true")
    a = ap.parse_args()

    filas = [f for f in leer_pendientes()
             if (not a.manual or f["manual"] == a.manual) and (not a.archivo or f["archivo"] == a.archivo)]
    if not a.rehacer:
        filas = [f for f in filas if not (ROOT / "content" / f["manual"] / "img" / f["archivo"]).exists()]
    if a.lista:
        for f in filas:
            print(f"{f['manual']:7} {f['archivo']:36} {f['ruta']:58} [{panel_de(f['ruta']) or 'público'}]  {f['perfil']}")
        print(f"\n{len(filas)} captura(s)."); return
    if not filas:
        print("No hay capturas pendientes."); return

    from playwright.sync_api import sync_playwright
    resultado, sesiones = [], {}
    with sync_playwright() as pw:
        browser = pw.chromium.launch(headless=not a.headed)
        publico = browser.new_context(viewport={"width": CFG["viewport"]["ancho"], "height": CFG["viewport"]["alto"]}, locale="es-PE")
        for f in filas:
            panel = None if f["archivo"] in CFG.get("sin_sesion", []) else panel_de(f["ruta"])
            if f["perfil"].lower().startswith("administrador sin mfa"):
                resultado.append((f, "tome esta captura a mano (cuenta sin MFA configurado)")); continue
            if panel and panel not in sesiones:
                sesiones[panel] = iniciar_sesion(pw, browser, panel)
            ctx = sesiones[panel] if panel else publico
            page = ctx.new_page()
            destino = ROOT / "content" / f["manual"] / "img" / f["archivo"]
            try:
                err = capturar(page, f, destino)
            except Exception as e:                      # una captura fallida no detiene al resto
                err = f"{type(e).__name__}: {str(e)[:120]}"
            page.close()
            resultado.append((f, err))
            print(("OK   " if not err else "FALLO"), f["manual"], f["archivo"], err or "")
        browser.close()
    L = ["# Resultado de la última captura\n", "| Manual | Archivo | Resultado |", "|---|---|---|"]
    for f, e in resultado: L.append(f"| {f['manual']} | {f['archivo']} | {'OK' if not e else e} |")
    (ROOT / "docs/capturas-resultado.md").write_text("\n".join(L) + "\n", encoding="utf8")
    print(f"\n{sum(1 for _, e in resultado if not e)} de {len(resultado)} capturas tomadas. Detalle en docs/capturas-resultado.md")


if __name__ == "__main__":
    main()
