# Data Analytics Portfolio

## About Me

Hello!

My name is Sherminta Lawrence, and I am a Data Analyst/Interface Analyst with over 10 years of experience in hospital data analytics and EMR integration. This repository showcases my skills, projects, and progress in healthcare data analytics.

[View My Resume/CV](#)

---

## Overview

This portfolio demonstrates an end-to-end approach to healthcare data analytics by:
- **Designing and managing** a relational database (PostgreSQL) for healthcare data.
- **Writing and optimizing SQL queries** to generate insights (e.g., readmission rates, common diagnoses).
- **Performing data analysis** with Python for data validation, cleaning, visualization, and predictive modeling.
- **Building interactive dashboards** using Power BI to communicate key findings.
## Data Modeling & ER Diagram



### Overview

In this project, a robust data model forms the foundation for our healthcare analytics workflow. The model integrates key datasets—including patient vitals, hospital encounters, and prescription records—into a unified schema. This comprehensive view allows for advanced feature engineering and predictive modeling, such as forecasting readmission risk, while also supporting the creation of interactive dashboards in Power BI.

### Key Entities and Relationships

1. **Patient**
   - **Primary Key:** `Patient_ID`
   - **Description:** Represents the core patient record. Although our current dataset focuses on clinical metrics, encounters, and prescriptions, this entity could be expanded to include demographic details.

2. **Patient_Vitals**
   - **Foreign Key:** `Patient_ID` (references Patient)
   - **Attributes:** Age, Gender, Height, Weight, BMI, Temperature, Heart Rate, Blood Pressure, etc.
   - **Relationship:** A single patient can have multiple vital sign measurements over time.

3. **Encounters**
   - **Primary Key:** `Encounter_ID`
   - **Foreign Key:** `Patient_ID` (references Patient)
   - **Attributes:** Admission Date, Discharge Date, Diagnosis Code, Diagnosis Description, Procedure, etc.
   - **Relationship:** Each patient may experience multiple hospital or clinical encounters.

4. **Patient_RX**
   - **Foreign Key:** `Patient_ID` (references Patient)
   - **Attributes:** Weight Loss Drug, Hypertension Drug, Diabetes Drug, Cholesterol Drug, etc.
   - **Relationship:** This table captures the medication profile for each patient, either as a single aggregated record or as multiple entries depending on the clinical scenario.

### ER Diagram

The following diagram illustrates the relationships between the entities:

      +--------------+
      |   Patient    |
      |--------------|
      | Patient_ID   |◄─────────┐
      +--------------+          │
                               │  One-to-Many
                               │
      +-------------------+    │
      |  Patient_Vitals   |    │
      |-------------------|    │
      | Patient_ID (FK)   |────┘
      | ...               |
      +-------------------+

      +--------------+
      |  Encounters  |
      |--------------|
      | Encounter_ID |◄─────────┐
      | Patient_ID   |──────────┤
      | ...          | One-to-Many
      +--------------+          │
                               │
                               │
      +-------------+          │
      |  Patient_RX |          │
      |-------------|          │
      | Patient_ID  |──────────┘
      | ...         |
      +-------------+



---

## Features

- **SQL Queries:** Examples of advanced JOINs, window functions, and aggregations on patient data.
- **Python EDA & Modeling:** Jupyter notebooks detailing data wrangling, exploratory analysis, and a sample logistic regression model for readmission prediction.
- **Data Simulation:** Use of Python Faker to generate realistic dummy datasets for demonstration and training.
- **Dashboard:** An interactive Power BI dashboard showcasing KPI trends (readmissions, length of stay, etc.).

---

## Tech Stack

- **Database:** PostgreSQL 14+  
- **Programming Language:** SQL, Python 3.13+ (libraries include `pandas`, `sqlalchemy`, `matplotlib`, `scikit-learn`, `faker`, `fhirclient`)
- **Data Visualization:** 

---

## Database Setup

- **Datasets Overview:**  
  - **Patient_vitals.csv:** Clinical measurements (e.g., BMI, heart rate, blood pressure).  
  - **Encounters.csv:** In-patient hospital admission details (admission/discharge dates, diagnosis codes).  
  - **Telemedicine_encounters.csv:** Remote consultation records (appointment dates, contact methods).  
  - **Patient_RX.csv:** Medication history (e.g., drugs for diabetes, hypertension).

Detailed documentation for setting up the database schema and populating the datasets is provided in the `/db` directory.

---

## Projects

#### Project 1: Clinical Trial Patient List (JOIN + CASE) 

#### Project 2: FHIR Resource Validation Lite 

---

## Contributing / Feedback

Contributions and feedback are welcome! Please feel free to open an issue or submit a pull request if you have suggestions or improvements.

---


