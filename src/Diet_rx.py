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
        
        # Drug Data
        weightloss_rx = random.choice(["Phentermine", "Semaglutide", "Naltrexone", "Lorcaserin", ""]) 
        hypertention_rx = random.choice(["Lisinopril", "Metoprolol", "Amlodipine", ""])
        diabetes_rx = random.choice(["Metformin", "Insulin", "Glipizide", ""])
        cholesterol_rx = random.choice(["Atorvastatin", "Simvastatin", "Rosuvastatin", ""])
        
        records.append([
            patient_id,
            weightloss_rx,
            hypertention_rx,
            diabetes_rx,
            cholesterol_rx,
            
        ])
        
    return records

# Generate and save to CSV
patient_data = generate_patient_data(NUM_PATIENTS)
with open("tests/Patient_RX.csv", mode="w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow([
        "patient_id",
        "weight_loss_drug",
        "hypertension_drug",
        "diabetes_drug",
        "cholesterol_drug",
    ])
    writer.writerows(patient_data)

print("Patient_RX.csv has been generated")
