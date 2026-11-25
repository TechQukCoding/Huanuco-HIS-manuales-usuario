-- Datos FICTICIOS de Emergencia para las capturas del manual HIS-03.
-- Crea 2 admisiones: EME-PRUEBA-0001 (admitido, sin triaje) y EME-PRUEBA-0002 (en triaje, con triaje registrado).
-- Es seguro repetirlo: no duplica nada. Usa dos pacientes que ya existan en la base.
--
-- Ejecutar desde la carpeta del repo de manuales (cmd):
--   docker exec -i -e PGPASSWORD=erp_password erp_postgres psql -U erp_user -d his_prueba < scripts\capturas\datos_emergencia_prueba.sql
BEGIN;

WITH pac AS (
  SELECT id, tenant_id, row_number() OVER (ORDER BY dni) AS n
  FROM (SELECT id, tenant_id, dni FROM patients WHERE is_active ORDER BY dni LIMIT 2) q
), seg AS (
  SELECT id, nombre FROM sigarh_seguros WHERE is_active ORDER BY nombre LIMIT 1
)
INSERT INTO admisiones_emergencia
  (id, tenant_id, patient_id, numero_cuenta, servicio_emergencia, fuente_financiamiento, seguro_id,
   estado, hora_llegada, procedencia, medio_llegada, observaciones, created_at)
SELECT gen_random_uuid(), pac.tenant_id, pac.id,
       CASE pac.n WHEN 1 THEN 'EME-PRUEBA-0001' ELSE 'EME-PRUEBA-0002' END,
       'Emergencia General', seg.nombre, seg.id,
       CASE pac.n WHEN 1 THEN 'admitido' ELSE 'en_triaje' END,
       (now() AT TIME ZONE 'America/Lima') - interval '35 minutes',
       'DOMICILIO', 'PROPIOS_MEDIOS',
       'Admision ficticia para las capturas del manual HIS-03',
       now() AT TIME ZONE 'utc'
FROM pac LEFT JOIN seg ON true
ON CONFLICT (numero_cuenta) DO NOTHING;

INSERT INTO triajes_emergencia
  (id, tenant_id, admision_id, prioridad, pulso, temperatura, presion_sistolica, presion_diastolica,
   frecuencia_cardiaca, frecuencia_respiratoria, peso, talla, saturacion_o2, observacion, created_at)
SELECT gen_random_uuid(), a.tenant_id, a.id, 'II', 96, 37.8, 125, 80,
       96, 20, 72.5, 170, 96, 'Triaje ficticio para las capturas del manual HIS-03',
       now() AT TIME ZONE 'utc'
FROM admisiones_emergencia a
WHERE a.numero_cuenta = 'EME-PRUEBA-0002'
ON CONFLICT (admision_id) DO NOTHING;

COMMIT;

\pset format unaligned
\pset tuples_only on
\echo
\echo === Copie estas 3 lineas en config/capturas.local.yml, debajo de la linea rutas: ===
SELECT '  "emer-triaje.png": "/app/emergencia/triaje/' || id || '"'
  FROM admisiones_emergencia WHERE numero_cuenta = 'EME-PRUEBA-0001';
SELECT '  "emer-episodio.png": "/app/emergencia/episodio/' || id || '"'
  FROM admisiones_emergencia WHERE numero_cuenta = 'EME-PRUEBA-0002';
SELECT '  "emer-atencion.png": "/app/emergencia/atencion/' || id || '"'
  FROM admisiones_emergencia WHERE numero_cuenta = 'EME-PRUEBA-0002';
