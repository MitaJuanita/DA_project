SELECT DISTINCT
    e."Encounter_ID",
    e."Admission_Date",
    e."Discharge_Date",
    e."Diagnosis_Code",
    e."Patient_ID",
    v."Age",
    v."BMI"
   
FROM encounters AS e
JOIN patient_vitals AS v
    ON e."Patient_ID" = v."Patient_ID"
WHERE e."Diagnosis_Code" = 'E11';
