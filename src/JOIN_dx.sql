--Join the encounters table with the patient_vitals table to get the following columns for patients with a diagnosis code of 'E11':
--
SELECT 
    e."Encounter_ID",
    e."Admission_Date",
    e."Discharge_Date",
    e."Diagnosis_Code",
    e."Patient_ID",
    v."Age",
    v."BMI",
    v."Blood_Pressure_MMHG"
FROM encounters AS e
JOIN patient_vitals AS v
    ON e."Patient_ID" = v."Patient_ID"
WHERE e."Diagnosis_Code" = 'E11';
