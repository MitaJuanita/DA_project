--Random trial candidates: 
--group A: ages 18 to 30, weightloss drugs, dx with diabetes, admited in the last six months
--group B: over the age of 30, weightloss, dx with hypertention, admited in the last 12 months
SELECT 
    v.Patient_ID,
    e.Encounter_ID,
    e.Admission_Date,
    e.Diagnosis_Code,
    CASE
        WHEN 
            -- Group A conditions
            v.Age BETWEEN 18 AND 30
            AND rx.Weight_Loss_Drug = 'Y'
            AND e.Diagnosis_Code = 'E11'  -- Diabetes
            AND e.Admission_Date >= CURRENT_DATE - INTERVAL '6 months'
        THEN 'Group A'

        WHEN 
            -- Group B conditions
            v.Age > 30
            AND rx.Weight_Loss_Drug = 'Y'
            AND e.Diagnosis_Code = 'I10'  -- Hypertension
            AND e.Admission_Date >= CURRENT_DATE - INTERVAL '12 months'
        THEN 'Group B'

        ELSE 'Not eligible'
    END AS trial_group

FROM patient_vitals v
JOIN patient_rx rx 
      ON v.Patient_ID = rx.Patient_ID
JOIN encounters e 
      ON v.Patient_ID = e.Patient_ID


