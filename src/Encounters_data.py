from faker import Faker
import random
import csv
import datetime

fake = Faker()

# Set random seed for reproducibility
random.seed(42)
fake.seed_instance(42)

NUM_PATIENTS = 500

# List of possible hospital departments
HOSPITAL_DEPARTMENTS = [
    "Emergency", "Cardiology", "Neurology", "Pediatrics",
    "Orthopedics", "General Medicine", "Oncology", "Radiology", "Surgery", "Psychiatry"
]

def generate_encounter_summary(department, diagnosis_desc, length_of_stay):
    templates = [
        "Patient admitted to {department} for evaluation of {diagnosis_desc}. Stayed for {length_of_stay} days with appropriate interventions.",
        "Encounter in {department}: {diagnosis_desc} diagnosed, and patient required a {length_of_stay}-day stay for further treatment.",
        "In the {department} department, the patient was treated for {diagnosis_desc}. The length of stay was {length_of_stay} days."
    ]
    template = random.choice(templates)
    return template.format(department=department, diagnosis_desc=diagnosis_desc, length_of_stay=length_of_stay)

def generate_patient_data(num_records=50):
    records = []
    for _ in range(num_records):
        # ADT Data
        patient_id = fake.random_int(min=1, max=9999)
        encounter_id = f"E{fake.random_int(min=10001, max=99999)}"
        admission_date = fake.date_between(start_date="-2y", end_date="today")
        discharge_date = fake.date_between(start_date=admission_date, end_date="today")
        
        # Calculate length of stay in days
        length_of_stay = (discharge_date - admission_date).days
        
        # Diagnosis and procedure details
        diagnosis_code = random.choice(["E11", "I10", "J45", "Z00.0", ""])  # diabetes, hypertension, asthma, general exam
        diagnosis_desc = fake.sentence(nb_words=6)  # Short diagnosis description
        procedure_code = f"T{fake.random_int(min=1001, max=9999)}"
        
        # Additional details
        attending_physician = fake.name()
        hospital_department = random.choice(HOSPITAL_DEPARTMENTS)
        encounter_summary = generate_encounter_summary(hospital_department, diagnosis_desc, length_of_stay)
        
        records.append([
            patient_id,
            encounter_id,
            admission_date.strftime("%Y-%m-%d"),
            discharge_date.strftime("%Y-%m-%d"),
            diagnosis_code,
            diagnosis_desc,
            procedure_code,
            attending_physician,
            hospital_department,
            encounter_summary
        ])
        
    return records

# Generate and save to CSV
patient_data = generate_patient_data(NUM_PATIENTS)
with open("tests/encounters.csv", mode="w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow([
        "patient_id",
        "encounter_id",
        "admission_date",
        "discharge_date",
        "diagnosis_code",
        "diagnosis_desc",
        "procedure",
        "attending_physician",
        "hospital_department",
        "encounter_summary"
    ])
    writer.writerows(patient_data)

print("encounters.csv has been generated")
