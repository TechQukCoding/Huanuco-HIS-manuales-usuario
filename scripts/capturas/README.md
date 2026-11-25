# Capturas de pantalla

1. Levante la aplicación con **datos de prueba** y cree una cuenta de prueba por panel (ERP, SIGARH y HIS).
2. Instale las dependencias (una sola vez):
   ```
   pip install playwright pyyaml pyotp
   playwright install chromium
   ```
3. Defina las credenciales **en la consola** (no en archivos):
   ```
   set CAP_ADMIN_USER=...  & set CAP_ADMIN_PASS=...  & set CAP_ADMIN_TOTP=...
   set CAP_SIGARH_USER=... & set CAP_SIGARH_PASS=...
   set CAP_HIS_USER=...    & set CAP_HIS_PASS=...
   ```
   (en Linux/Mac use `export` en lugar de `set`).
4. Ajuste `base_url` en `config/capturas.yml`.
5. Pruebe sin tomar nada: `python scripts/capturas/capturar.py --lista`
6. Tome las capturas: `python scripts/capturas/capturar.py` (o `--manual HIS-01`).
7. Revise `docs/capturas-resultado.md`: lo que falló se repite con `--archivo` o se toma a mano.
8. Suba los PNG: `git add content docs` · `git commit -m "Capturas"` · `git push`.

Cada imagen se guarda como `content/<MANUAL>/img/<archivo>.png`. Los manuales la usan sola al recompilar.
**Solo datos ficticios**: revise las imágenes antes de subirlas.
