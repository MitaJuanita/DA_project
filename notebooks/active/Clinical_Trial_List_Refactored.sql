-- Common Table Expressions (CTEs) for better readability and maintenance
WITH 
-- 1. Filter patients by recent diagnoses
diagnosis_filter AS (
    SELECT
        e."Encounter_ID",
        e."Patient_ID",
        e."Admission_Date",
        e."Diagnosis_Code"
    FROM "encounters" e
    WHERE e."Admission_Date" >= CURRENT_DATE - INTERVAL '24 months'
      AND e."Diagnosis_Code" IN ('E11', 'I10')
),

-- 2. Get eligible patients with medications
medication_eligibility AS (
    SELECT DISTINCT
        v."Patient_ID",
        v."Age",
        rx."Weight_Loss_Drug",
        rx."Prescribed_Date"
    FROM "patient_vitals" v
    INNER JOIN Patient_RX rx 
        ON v."Patient_ID" = rx."Patient_ID"
    WHERE rx."Weight_Loss_Drug" IS NOT NULL
),

-- 3. Assign trial groups based on criteria
trial_assignment AS (
    SELECT
        d."Patient_ID",
        d."Encounter_ID",
        d."Admission_Date",
        d."Diagnosis_Code",
        m."Age",
        m."Weight_Loss_Drug",
        CASE
            WHEN m."Age" BETWEEN 18 AND 30 
             AND d."Diagnosis_Code" = 'E11' THEN 'Group A'
            WHEN m."Age" > 30 
             AND d."Diagnosis_Code" = 'I10' THEN 'Group B'
            ELSE 'Not eligible'
        END AS trial_group
    FROM diagnosis_filter d
    INNER JOIN medication_eligibility m 
        ON d."Patient_ID" = m."Patient_ID"
        AND m."Prescribed_Date" <= d."Admission_Date"
)

-- Final selection with clear filtering
SELECT DISTINCT
    "Patient_ID",
    "Encounter_ID",
    "Admission_Date",
    "Diagnosis_Code",
    "Age",
    "Weight_Loss_Drug",
    trial_group
FROM trial_assignment
WHERE trial_group IN ('Group A', 'Group B')
ORDER BY trial_group;