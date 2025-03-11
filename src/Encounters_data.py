from faker import Faker
import random
import csv

fake = Faker()

# Set random seed for reproducibility
random.seed(42)
fake.seed_instance(42)

NUM_PATIENTS = 500

def generate_patient_data(num_records=50):
    records = []
    for _ in range(num_records):
        # ADT Data
        patient_id = fake.random_int(min=1, max=9999)
        encounter_id = f"E{fake.random_int(min=10001, max=99999)}"
        admission_date = fake.date_between(start_date="-2y", end_date="today")
        discharge_date = fake.date_between(start_date=admission_date, end_date="today")
        
        # diagnosis and procedure codes
        diagnosis_code = random.choice(["E11", "I10", "J45", "Z00.0",""])  # diabetes, hypertension, asthma, general exam        ##diagnosis_desc = fake.sentence()
        ##procedure_code = f"T{fake.random_int(min=1001, max=9999)}"
        
        records.append([
            patient_id,
            encounter_id,
            admission_date,
            discharge_date,
            diagnosis_code,
            ##procedure_code,
        ])
        
    return records

# Generate and save to CSV
patient_data = generate_patient_data(NUM_PATIENTS)
with open("tests/encounters.csv", mode="w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow([
        "Patient_ID",
        "Encounter_ID",
        "Admission_Date",
        "Discharge_Date",
        "Diagnosis_Code",
        ##"Diagnosis_Desc",
       ## "Procedure",
    ])
    writer.writerows(patient_data)

print("encounters.csv has been generated")
