from faker import Faker
import random
import datetime
import csv

fake = Faker()

# Set random seed for reproducibility
random.seed(42)
fake.seed_instance(42)

NUM_PATIENTS = 500

# List of possible doctor specialties
DOCTOR_SPECIALTIES = [
    "General Practice", "Cardiology", "Dermatology", 
    "Neurology", "Pediatrics", "Endocrinology", 
    "Psychiatry", "Orthopedics", "Ophthalmology", "Oncology"
]

def generate_physician_note():
    # List of realistic note templates
    templates = [
        "Patient reported {symptom} and {symptom2}. Recommended {treatment} and follow-up in {days} days.",
        "Encounter focused on {symptom}. Advised {treatment} and monitoring for any changes.",
        "Patient presented with {symptom} and mild {symptom2}. No immediate intervention required, but schedule a follow-up.",
        "Reviewed symptoms: {symptom} and {symptom2}. Initiated {treatment} and provided education on home care."
    ]
    symptoms = ["headache", "nausea", "dizziness", "fatigue", "cough", "sore throat"]
    treatments = ["rest", "hydration", "over-the-counter medication", "increased physical activity", "dietary modifications"]
    template = random.choice(templates)
    note = template.format(
        symptom=random.choice(symptoms),
        symptom2=random.choice(symptoms),
        treatment=random.choice(treatments),
        days=random.randint(3, 14)
    )
    return note

def generate_encounter_summary(doctor_specialty, encounter_type):
    # List of encounter summary templates that incorporate specialty and type
    templates = [
        "The encounter was a {encounter_type} visit where the {doctor_specialty} evaluated the patient's condition thoroughly.",
        "During this {encounter_type} appointment, the {doctor_specialty} conducted a detailed assessment and provided personalized recommendations.",
        "In a {encounter_type} session, the {doctor_specialty} performed a comprehensive evaluation, leading to a clear treatment plan.",
        "This {encounter_type} encounter with the {doctor_specialty} resulted in a focused discussion on symptoms and follow-up care."
    ]
    template = random.choice(templates)
    return template.format(doctor_specialty=doctor_specialty, encounter_type=encounter_type)

def generate_patient_data(num_records=50):
    records = []
    for _ in range(num_records):
        # ADT Data
        patient_id = fake.random_int(min=1, max=9999)
        encounter_id = f"E{fake.random_int(min=1005, max=99999)}"
        
        # Telemedicine details
        platform = random.choice(["MyChart", "Cell/Phone", "TTY/Chat"]) 
        encounter_type = random.choice(["New Patient", "Routine", "Follow-up", "Urgent"])
        physician_name = fake.name()
        doctor_specialty = random.choice(DOCTOR_SPECIALTIES)
        physician_notes = generate_physician_note()
        encounter_summary = generate_encounter_summary(doctor_specialty, encounter_type)
        appointment_date = fake.date_between(start_date="-2y", end_date="today")

        # Generate realistic start and end times
        start_time = fake.date_time_between(start_date="-1y", end_date="now")
        duration_minutes = random.randint(15, 60)  # Duration between 15 and 60 minutes
        end_time = start_time + datetime.timedelta(minutes=duration_minutes)
        
        records.append([
            patient_id,
            encounter_id,
            appointment_date.strftime("%Y-%m-%d"),
            start_time.strftime("%Y-%m-%d %H:%M:%S"),
            end_time.strftime("%Y-%m-%d %H:%M:%S"),
            platform,
            encounter_type,
            physician_name,
            doctor_specialty,
            physician_notes,
            encounter_summary
        ])
        
    return records

# Generate and save to CSV
patient_data = generate_patient_data(NUM_PATIENTS)
with open("tests/telemedicine_encounters.csv", mode="w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow([
        "patient_id",
        "encounter_id",
        "start_time",
        "end_time",
        "platform",
        "encounter_type",
        "physician_name",
        "doctor_specialty",
        "physician_notes",
        "encounter_summary"
    ])
    writer.writerows(patient_data)

print("telemedicine_encounters.csv has been generated")
