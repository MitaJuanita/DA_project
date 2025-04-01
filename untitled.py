import pytest
import pandas as pd
from datetime import datetime
from tests.trial_eligibility import load_trial_criteria, load_patient_data, assign_trial_groups

def test_assign_trial_groups():
    # Setup test data with multiple patients
    patients = pd.DataFrame([
        {
            "Patient_ID": 101,
            "Age": 25,
            "Diagnosis_Code": "E11",
            "Admission_Date": "2024-03-01",
            "Weight_Loss_Drug": "Ozempic",
            "Prescribed_Date": "2024-02-01"
        },
        {
            "Patient_ID": 102,
            "Age": 45,
            "Diagnosis_Code": "I10",
            "Admission_Date": "2024-03-01",
            "Weight_Loss_Drug": "Metformin",
            "Prescribed_Date": "2024-02-01"
        }
    ])

    criteria = load_trial_criteria()
    result = assign_trial_groups(patients, criteria)

    # Enhanced assertions
    assert len(result) == 2, "Should process all eligible patients"
    assert "trial_group" in result.columns, "Should add trial_group column"
    assert result.iloc[0]["trial_group"] == "Group A", "Young E11 patient should be Group A"
    assert result.iloc[1]["trial_group"] == "Group B", "Older I10 patient should be Group B"

@pytest.mark.parametrize("patient_data,expected_group", [
    ({
        "Age": 25, 
        "Diagnosis_Code": "E11"
    }, "Group A"),
    ({
        "Age": 45, 
        "Diagnosis_Code": "I10"
    }, "Group B"),
    ({
        "Age": 18, 
        "Diagnosis_Code": "Other"
    }, "Not eligible")
])
def test_group_assignment_rules(patient_data, expected_group):
    patient = pd.DataFrame([{
        "Patient_ID": 101,
        "Admission_Date": "2024-03-01",
        "Weight_Loss_Drug": "Ozempic",
        "Prescribed_Date": "2024-02-01",
        **patient_data
    }])
    
    criteria = load_trial_criteria()
    result = assign_trial_groups(patient, criteria)
    assert result.iloc[0]["trial_group"] == expected_group
