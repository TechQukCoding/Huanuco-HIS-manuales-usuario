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
   (en PowerShell: `$env:NOMBRE="valor"`; en Linux/Mac: `export`). Guía completa: `docs/GUIA-CAPTURAS.md`.
4. Ajuste `base_url` en `config/capturas.yml`.
5. Pruebe sin tomar nada: `python scripts/capturas/capturar.py --lista`
6. Tome las capturas: `python scripts/capturas/capturar.py` (o `--manual HIS-01`).
7. Revise `docs/capturas-resultado.md`: lo que falló se repite con `--archivo` o se toma a mano.
8. Suba los PNG: `git add content docs` · `git commit -m "Capturas"` · `git push`.

Cada imagen se guarda como `content/<MANUAL>/img/<archivo>.png`. Los manuales la usan sola al recompilar.
**Solo datos ficticios**: revise las imágenes antes de subirlas.

## Pantallas de detalle (`[id]`)
Para abrir un registro concreto, cree `config/capturas.local.yml` (no se sube a git) con la dirección exacta:
```yaml
rutas:
  "roles-editor.png": "/sigarh/creacion-roles/medicos/ordinario/<id-de-un-rol-borrador>"
  "aprobados-solicitar.png": "/sigarh/roles-aprobados/<id-de-un-rol-aprobado>"
clics:
  "aprobados-solicitar.png": ["Solicitar incorporación"]
```

## Datos de Emergencia para las capturas de HIS-03
Si la base no tiene admisiones de emergencia, cree dos ficticias con un solo comando (desde la carpeta de manuales):
```
docker exec -i -e PGPASSWORD=erp_password erp_postgres psql -U erp_user -d his_prueba < scripts\capturas\datos_emergencia_prueba.sql
```
Imprime tres líneas para `config/capturas.local.yml`. Es seguro repetirlo. Para borrarlas:
```
docker exec -e PGPASSWORD=erp_password erp_postgres psql -U erp_user -d his_prueba -c "delete from admisiones_emergencia where numero_cuenta like 'EME-PRUEBA-%'"
```

