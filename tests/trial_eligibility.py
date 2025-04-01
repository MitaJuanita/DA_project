# trial_eligibility.py
from typing import List, Dict
import pandas as pd
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def load_trial_criteria() -> pd.DataFrame:
    """Load trial criteria with versioning information.

    Returns:
        pd.DataFrame: Trial criteria with columns for group, age ranges,
                     diagnosis codes, and effective dates
    """
    data = [
        {
            "trial_group": "Group A",
            "min_age": 18,
            "max_age": 30,
            "diagnosis_code": "E11",
            "weight_loss_drug_required": True,
            "version": 1,
            "effective_date": "2023-01-01",
            "expiry_date": "2024-01-01",
        },
        {
            "trial_group": "Group A",
            "min_age": 10,
            "max_age": 35,
            "diagnosis_code": "E11",
            "weight_loss_drug_required": True,
            "version": 2,
            "effective_date": "2024-01-02",
            "expiry_date": "2099-12-31",
        },
        {
            "trial_group": "Group B",
            "min_age": 31,
            "max_age": 120,
            "diagnosis_code": "I10",
            "weight_loss_drug_required": True,
            "version": 1,
            "effective_date": "2023-01-01",
            "expiry_date": "2099-12-31",
        },
    ]
    df = pd.DataFrame(data)
    df["effective_date"] = pd.to_datetime(df["effective_date"])
    df["expiry_date"] = pd.to_datetime(df["expiry_date"])
    return df


def load_patient_data():
    data = [
        {
            "Patient_ID": 101,
            "Age": 25,
            "Diagnosis_Code": "E11",
            "Admission_Date": "2024-03-01",
            "Weight_Loss_Drug": "Ozempic",
            "Prescribed_Date": "2024-02-01",
        },
        {
            "Patient_ID": 102,
            "Age": 33,
            "Diagnosis_Code": "I10",
            "Admission_Date": "2024-03-15",
            "Weight_Loss_Drug": "Contrave",
            "Prescribed_Date": "2024-02-10",
        },
        {
            "Patient_ID": 103,
            "Age": 28,
            "Diagnosis_Code": "E11",
            "Admission_Date": "2023-06-01",
            "Weight_Loss_Drug": "Wegovy",
            "Prescribed_Date": "2023-05-01",
        },
        {
            "Patient_ID": 104,
            "Age": 9,
            "Diagnosis_Code": "R211",
            "Admission_Date": "2024-03-10",
            "Weight_Loss_Drug": "None",
            "Prescribed_Date": "2024-03-09",
        },
    ]
    df = pd.DataFrame(data)
    df["Admission_Date"] = pd.to_datetime(df["Admission_Date"])
    df["Prescribed_Date"] = pd.to_datetime(df["Prescribed_Date"])
    return df


def assign_trial_groups(
    patients_df: pd.DataFrame, criteria_df: pd.DataFrame
) -> pd.DataFrame:
    """Assign patients to trial groups based on criteria.

    Args:
        patients_df: DataFrame containing patient information
        criteria_df: DataFrame containing trial criteria

    Returns:
        pd.DataFrame: Eligible patients with assigned trial groups

    Raises:
        ValueError: If required columns are missing
    """
    logger.info(
        f"Processing {len(patients_df)} patients against {len(criteria_df)} criteria"
    )

    required_patient_cols = ["Patient_ID", "Age", "Diagnosis_Code", "Admission_Date"]
    required_criteria_cols = ["trial_group", "min_age", "max_age", "diagnosis_code"]

    if not all(col in patients_df.columns for col in required_patient_cols):
        raise ValueError(f"Missing required patient columns: {required_patient_cols}")

    merged = pd.merge(
        patients_df,
        criteria_df,
        left_on="Diagnosis_Code",
        right_on="diagnosis_code",
        how="inner",
    )

    eligible = merged[
        (merged["Diagnosis_Code"] == merged["diagnosis_code"])
        & (merged["Age"] >= merged["min_age"])
        & (merged["Age"] <= merged["max_age"])
        & (
            merged["weight_loss_drug_required"]
            == (merged["Weight_Loss_Drug"] != "None")
        )
        & (merged["Prescribed_Date"] <= merged["Admission_Date"])
        & (merged["Admission_Date"] >= merged["effective_date"])
        & (merged["Admission_Date"] <= merged["expiry_date"])
    ]

    eligible = eligible.sort_values("version").drop_duplicates(
        ["Patient_ID", "trial_group"], keep="last"
    )

    logger.info(f"Found {len(eligible)} eligible patients")
    return eligible[
        [
            "Patient_ID",
            "trial_group",
            "version",
            "Admission_Date",
            "Age",
            "Diagnosis_Code",
        ]
    ]


# Example usage (uncomment to test in notebook)
# criteria_df = load_trial_criteria()
# patients_df = load_patient_data()
# eligible_patients = assign_trial_groups(patients_df, criteria_df)
# print(eligible_patients)

