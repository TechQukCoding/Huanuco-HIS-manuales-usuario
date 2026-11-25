-- Datos FICTICIOS de Hospitalizacion para las capturas del manual HIS-04.
-- Crea 1 paciente internado (HOSP-PRUEBA-0001) en una cama libre de una sala GENERAL, con 2 ordenes medicas,
-- 2 administraciones de kardex, 1 plan de cuidados, 3 registros de balance hidrico y 2 notas de evolucion.
-- Es seguro repetirlo: si ya existe, no hace nada. Usa un paciente y un medico/enfermera que ya existan.
--
-- Ejecutar desde la carpeta del repo de manuales (cmd):
--   docker exec -i -e PGPASSWORD=erp_password erp_postgres psql -U erp_user -d his_prueba < scripts\capturas\datos_hospitalizacion_prueba.sql
DO $$
DECLARE
  tid uuid; pid uuid; cid uuid; hid uuid; med uuid; enf uuid; ord1 uuid;
  ahora timestamp := (now() AT TIME ZONE 'America/Lima');
  utc   timestamp := (now() AT TIME ZONE 'utc');
BEGIN
  IF EXISTS (SELECT 1 FROM hospitalizaciones WHERE numero_hospitalizacion = 'HOSP-PRUEBA-0001') THEN
    RAISE NOTICE 'La hospitalizacion de prueba ya existe: no se repite.';
    RETURN;
  END IF;

  SELECT p.id, p.tenant_id INTO pid, tid
    FROM patients p
   WHERE p.is_active
     AND NOT EXISTS (SELECT 1 FROM hospitalizaciones h WHERE h.patient_id = p.id AND h.estado = 'internado')
   ORDER BY p.dni DESC LIMIT 1;
  IF pid IS NULL THEN RAISE EXCEPTION 'No hay pacientes activos en la base.'; END IF;

  SELECT c.id INTO cid
    FROM sigarh_camas c JOIN sigarh_salas s ON s.id = c.sala_id
   WHERE c.tenant_id = tid AND c.is_active AND c.estado = 'DISPONIBLE' AND s.is_active AND s.tipo = 'GENERAL'
   ORDER BY c.codigo LIMIT 1;
  IF cid IS NULL THEN RAISE EXCEPTION 'No hay una cama DISPONIBLE en una sala GENERAL. Libere una cama o cree una (SIG-03).'; END IF;

  SELECT e.id INTO med FROM sigarh_empleados e JOIN sigarh_profesiones pr ON pr.id = e.profesion_id
   WHERE e.tenant_id = tid AND pr.nombre ILIKE 'M_dico Cirujano%' ORDER BY e.id LIMIT 1;
  IF med IS NULL THEN SELECT id INTO med FROM sigarh_empleados WHERE tenant_id = tid ORDER BY id LIMIT 1; END IF;
  SELECT e.id INTO enf FROM sigarh_empleados e JOIN sigarh_profesiones pr ON pr.id = e.profesion_id
   WHERE e.tenant_id = tid AND pr.nombre ILIKE 'Enfermer%' ORDER BY e.id LIMIT 1;
  IF enf IS NULL THEN enf := med; END IF;
  IF med IS NULL THEN RAISE EXCEPTION 'No hay empleados registrados (SIG-01).'; END IF;

  hid := gen_random_uuid();
  INSERT INTO hospitalizaciones (id, tenant_id, patient_id, cama_id, numero_hospitalizacion, numero_cuenta,
                                 fecha_ingreso, estado, registrado_por)
  VALUES (hid, tid, pid, cid, 'HOSP-PRUEBA-0001', 'CTA-PRUEBA-0001', ahora - interval '2 days', 'internado', 'Datos de prueba');
  UPDATE sigarh_camas SET estado = 'OCUPADA', updated_at = utc WHERE id = cid;

  ord1 := gen_random_uuid();
  INSERT INTO hosp_ordenes_medicas (id, tenant_id, hospitalizacion_id, tipo, descripcion, dosis, via, frecuencia_horas,
                                    indicacion, inicio_at, estado, medico_id, registrado_por, created_at)
  VALUES (ord1, tid, hid, 'MEDICAMENTO', 'Ceftriaxona 1 g EV cada 12 horas', '1 g', 'EV', 12,
          'Infeccion respiratoria baja (dato ficticio)', ahora - interval '30 hours', 'ACTIVA', med, 'Datos de prueba', utc),
         (gen_random_uuid(), tid, hid, 'DIETA', 'Dieta blanda hiposodica', NULL, NULL, NULL,
          'Control de liquidos', ahora - interval '2 days', 'ACTIVA', med, 'Datos de prueba', utc);

  INSERT INTO hosp_administraciones (id, tenant_id, orden_id, hora, estado, enfermero_id, registrado_por, created_at)
  VALUES (gen_random_uuid(), tid, ord1, ahora - interval '13 hours', 'CUMPLIDO', enf, 'Datos de prueba', utc),
         (gen_random_uuid(), tid, ord1, ahora - interval '1 hour',  'CUMPLIDO', enf, 'Datos de prueba', utc);

  INSERT INTO hosp_planes_cuidado (id, tenant_id, hospitalizacion_id, diagnostico_enfermeria, objetivo, intervenciones,
                                   estado, enfermero_id, registrado_por, created_at, updated_at)
  VALUES (gen_random_uuid(), tid, hid, 'Riesgo de infeccion', 'Mantener al paciente afebril durante la hospitalizacion',
          'Control de funciones vitales cada 6 horas; higiene de manos; vigilancia de la via venosa',
          'ACTIVO', enf, 'Datos de prueba', utc, utc);

  INSERT INTO hosp_balances (id, tenant_id, hospitalizacion_id, hora, tipo, concepto, volumen_ml, registrado_por, created_at)
  VALUES (gen_random_uuid(), tid, hid, ahora - interval '5 hours', 'INGRESO', 'SOLUCIONES_EV', 500, 'Datos de prueba', utc),
         (gen_random_uuid(), tid, hid, ahora - interval '3 hours', 'INGRESO', 'VIA_ORAL', 300, 'Datos de prueba', utc),
         (gen_random_uuid(), tid, hid, ahora - interval '2 hours', 'EGRESO',  'DIURESIS', 450, 'Datos de prueba', utc);

  INSERT INTO hosp_notas_evolucion (id, tenant_id, hospitalizacion_id, autor_id, tipo, pulso, temperatura,
                                    presion_sistolica, presion_diastolica, saturacion_o2, contenido, plan_indicaciones,
                                    registrado_por, created_at)
  VALUES (gen_random_uuid(), tid, hid, med, 'MEDICA', 88, 36.8, 120, 78, 96,
          'Paciente estable, afebril, tolera via oral. Evolucion favorable (dato ficticio).',
          'Continuar antibiotico y control de funciones vitales.', 'Datos de prueba', utc - interval '6 hours'),
         (gen_random_uuid(), tid, hid, enf, 'ENFERMERIA', 84, 36.6, NULL, NULL, 97,
          'Descansa con tranquilidad. Se cumple medicacion segun kardex.',
          NULL, 'Datos de prueba', utc - interval '2 hours');

  RAISE NOTICE 'Hospitalizacion de prueba creada.';
END $$;

\pset format unaligned
\pset tuples_only on
\echo
\echo === Copie esta linea en config/capturas.local.yml, debajo de la linea rutas: ===
SELECT '  "hosp-expediente.png": "/app/hospitalizacion/expediente/' || id || '"'
  FROM hospitalizaciones WHERE numero_hospitalizacion = 'HOSP-PRUEBA-0001';
