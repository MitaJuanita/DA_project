-- Query the encounters table for all columns where the diagnosis code is 'E11'
-- and join the patient_vitals table on patient_id to get the age, bmi, and blood_pressure_mmhg columns.
-- Return the encounter_id, admission_date, discharge_date, diagnosis_code, age, bmi, and blood_pressure_mmhg columns.
SELECT 
    e.encounter_id,
    e.admission_date,
    e.discharge_date,
    e.diagnosis_code,
    e.patient_id,
    v.age,
    v.bmi,
    v.blood_pressure_mmhg
FROM encounters e
JOIN patient_vitals v
    ON e.patient_id = v.patient_id
WHERE e.diagnosis_code = 'E11';