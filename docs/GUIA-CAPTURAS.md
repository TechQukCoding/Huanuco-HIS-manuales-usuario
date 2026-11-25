# Guía paso a paso: levantar la aplicación y tomar las capturas

> Pensada para Windows con PowerShell. Se basa en el `README.md` del ERP y en los scripts del backend.
> Todo es **solo para pruebas locales** con datos ficticios.

## A. Requisitos (una sola vez)

- **Docker Desktop** (abierto y en ejecución), **Python 3.11 o superior**, **Node.js 20 o superior** y **Git**.
- Los dos repositorios clonados: el del **ERP** (`ERP--Hospital-Nivel-II--Huanuco-`) y el de **manuales** (`Huanuco-HIS-manuales-usuario`).

## B. Levantar el ERP

### 1. Backend: entorno y dependencias
```powershell
cd ERP--Hospital-Nivel-II--Huanuco-\backend
python -m venv venv
.\venv\Scripts\Activate.ps1
pip install -e ".[dev]"
Copy-Item .env.example .env
```
Abra `.env` y reemplace `SECRET_KEY` por cualquier texto largo (64 caracteres). Lo demás sirve tal cual para pruebas locales.

### 2. Infraestructura (base de datos, Redis, RabbitMQ)
```powershell
cd ..\infra
docker compose up -d postgres redis rabbitmq
docker ps
```
Deben aparecer `erp_postgres`, `erp_redis` y `erp_rabbitmq`. Espere unos 15 segundos.

### 3. Migraciones
```powershell
cd ..\backend
alembic upgrade head
```

### 4. Instalar el hospital de prueba
Elija contraseñas de prueba que tengan 8 o más caracteres con mayúscula, minúscula, número y símbolo.
```powershell
$env:INSTALAR_ADMIN_PASSWORD  = "Admin-Prueba-2026"
$env:INSTALAR_APP_PASSWORD    = "App-Prueba-2026"
$env:INSTALAR_SIGARH_PASSWORD = "Sigarh-Prueba-2026"
python -m scripts.instalar_hospital --dominio prueba.huanuco.techquk.com `
  --admin-email admin@prueba.huanuco.techquk.com `
  --app-email app@prueba.huanuco.techquk.com `
  --sigarh-email sigarh@prueba.huanuco.techquk.com
```
Termina con *Hospital: listo*. Si quedó en error, vuelva a ejecutarlo (reintenta).

### 5. Cargar los datos ficticios (en este orden)
```powershell
python -m scripts.seed_catalogos_base
python -m scripts.seed_datos_prueba
python -m scripts.demo_sigarh
```
- `seed_datos_prueba` crea médicos, enfermeras, pacientes, consultorios, camas, medicamentos, tarifas y la programación de las próximas dos semanas. Al final **imprime las cuentas del HIS**: todas con la contraseña `Prueba-Huanuco-2026` y, los médicos, **PIN de firma `123456`**.
- `demo_sigarh` carga empleados, roles y configuración de SIGARH.
- Si algún mensaje dice que falta algo (departamentos, actividades, guardias), ejecute también `python -m scripts.seed_departamentos`, `python -m scripts.seed_actividades` y `python -m scripts.seed_guardias`, y repita el paso que falló. Todos los scripts son seguros de repetir.

### 6. Arrancar el backend
```powershell
uvicorn main:app --reload --proxy-headers --forwarded-allow-ips 127.0.0.1,::1
```
Compruebe `http://localhost:8000/docs`. **Deje esta ventana abierta.**

### 7. Arrancar el frontend (otra ventana de PowerShell)
```powershell
cd ERP--Hospital-Nivel-II--Huanuco-\frontend
Copy-Item .env.example .env
npm install
npm run build
npm run preview
```
Use `build` + `preview` y no `npm run dev`, para que las capturas no muestren las herramientas de desarrollo. La aplicación queda en `http://localhost:3000` (si `preview` usa otro puerto, anótelo). **Deje esta ventana abierta.**

## C. Comprobar los accesos a mano (5 minutos)

Abra el navegador y entre a cada panel:

| Panel | Dirección | Usuario | Contraseña |
|---|---|---|---|
| ERP | `http://localhost:3000/admin/login` | `admin@prueba.huanuco.techquk.com` | `Admin-Prueba-2026` |
| SIGARH | `http://localhost:3000/sigarh/login` | `sigarh@prueba.huanuco.techquk.com` | `Sigarh-Prueba-2026` |
| HIS | `http://localhost:3000/app/login` | `app@prueba.huanuco.techquk.com` | `App-Prueba-2026` |

**El ERP pide MFA la primera vez.** En el paso *Escanea el código*, **copie y guarde la clave manual** que aparece bajo el QR: es el secreto que necesita el script (`CAP_ADMIN_TOTP`). Para confirmar el MFA puede escanear el QR con su teléfono, o generar el código con:
```powershell
python -c "import pyotp; print(pyotp.TOTP('PEGUE_AQUI_LA_CLAVE').now())"
```
(instale antes con `pip install pyotp`).

## D. Tomar las capturas

En una tercera ventana, dentro del repo de **manuales**:
```powershell
pip install playwright pyyaml pyotp
playwright install chromium
```
Defina las credenciales **solo en esta ventana**:
```powershell
$env:CAP_ADMIN_USER  = "admin@prueba.huanuco.techquk.com"
$env:CAP_ADMIN_PASS  = "Admin-Prueba-2026"
$env:CAP_ADMIN_TOTP  = "LA_CLAVE_MANUAL_DEL_PASO_C"
$env:CAP_SIGARH_USER = "sigarh@prueba.huanuco.techquk.com"
$env:CAP_SIGARH_PASS = "Sigarh-Prueba-2026"
$env:CAP_HIS_USER    = "app@prueba.huanuco.techquk.com"
$env:CAP_HIS_PASS    = "App-Prueba-2026"
```
Ajuste `base_url` en `config/capturas.yml` si su puerto no es 3000. Luego:
```powershell
python scripts/capturas/capturar.py --lista                       # solo muestra qué tomaría
python scripts/capturas/capturar.py --manual GEN-00 --headed      # prueba con un manual y navegador visible
python scripts/capturas/capturar.py                               # todas las pendientes
```
Revise `docs/capturas-resultado.md`. Lo que falló se repite con `--archivo nombre.png` o se toma a mano.

## E. Subir las capturas
```powershell
git add content docs
git commit -m "Capturas"
git push
```
y avise para que se inserten y se coloquen los números de llamada.

## Si algo falla

| Síntoma | Qué hacer |
|---|---|
| `docker compose` no responde | Abra Docker Desktop y espere a que diga *running*. |
| Puerto 5432, 6379 u 8000 ocupado | Cierre el programa que lo usa (otro Postgres, por ejemplo). |
| `alembic` no conecta | Revise `DATABASE_URL` en `.env` y que `erp_postgres` esté arriba. |
| `instalar_hospital` rechaza la contraseña | Use mayúscula, minúscula, número y símbolo; 8 o más caracteres. |
| El login de la aplicación no responde | Confirme que el backend corre (`/docs`) y `NUXT_PUBLIC_API_URL` en `frontend/.env`. |
| El script no inicia sesión | Pruebe con `--headed`; envíe el mensaje de error para ajustarlo. |
| Una captura sale vacía | Falta ese dato de prueba: tómela a mano o cargue el dato. |
