SELECT DISTINCT
    v."Patient_ID",
    e."Encounter_ID",
    e."Admission_Date",
    e."Diagnosis_Code",
	v."Age",
	rx."Weight_Loss_Drug",
	
    CASE
        WHEN 
            v."Age" BETWEEN 18 AND 30
            AND rx."Weight_Loss_Drug" IS NOT NULL
            AND e."Diagnosis_Code" = 'E11'
            AND e."Admission_Date" >= CURRENT_DATE - INTERVAL '24 months'
        THEN 'Group A'

        WHEN 
            v."Age" > 30
            AND rx."Weight_Loss_Drug" IS NOT NULL
            AND e."Diagnosis_Code" = 'I10'
            AND e."Admission_Date" >= CURRENT_DATE - INTERVAL '24 months'
        THEN 'Group B'

        ELSE 'Not eligible'
    END AS "trial_group"

FROM "patient_vitals" AS v
JOIN Patient_RX AS rx 
      ON v."Patient_ID" = rx."Patient_ID"
JOIN "encounters" AS e 
      ON v."Patient_ID" = e."Patient_ID"
ORDER by "trial_group";
