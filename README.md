# Telemedicine Patient Risk Prediction & Data Modeling Portfolio

## About Me

Hello!

My name is Sherminta Lawrence, and I am a Data Analyst/Interface Analyst with over 10 years of experience in hospital data analytics and EMR integration. This repository showcases my skills, projects, and progress in healthcare data analytics.

In my spare time, I explore new tools and techniques to gain insights into solving complex problems. 

[View My Resume/CV](#)

---

## Table of Contents

1. [Overview](#overview)  
2. [Features](#features)  
3. [Tech Stack](#tech-stack)  
4. [Database Setup](#database-setup)  
5. [Data Analysis with Python](#data-analysis-with-python)  
6. [Sample Dashboards](#sample-dashboards)  
7. [Project Scenarios](#project-scenarios)  
8. [Contributing / Feedback](#contributing--feedback)  
9. [License](#license)

---

## Overview

This project demonstrates an end-to-end approach to healthcare data analytics by:
- **Designing and managing** a relational database (PostgreSQL) for healthcare data.
- **Writing and optimizing SQL queries** to generate insights (e.g., readmission rates, common diagnoses).
- **Performing data analysis** with Python for data cleaning, visualization, and predictive modeling.
- **Building interactive dashboards** using Power BI to communicate key findings.

---

## Features

- **SQL Queries:** Examples of advanced JOINs, window functions, and aggregations on patient data.
- **Python EDA & Modeling:** Jupyter notebooks detailing data wrangling, exploratory analysis, and a sample logistic regression model for readmission prediction.
- **Data Simulation:** Use of Python Faker to generate realistic dummy datasets for demonstration and training.
- **Dashboard:** An interactive Power BI dashboard showcasing KPI trends (readmissions, length of stay, etc.).

---

## Tech Stack

- **Database:** PostgreSQL 14+  
- **Programming Language:** Python 3.13+ (libraries include `pandas`, `sqlalchemy`, `matplotlib`, `scikit-learn`, `faker`)
- **Data Visualization:** Power BI (or Tableau as an alternative)

---

## Database Setup

- **Datasets Overview:**  
  - **Patient_vitals.csv:** Clinical measurements (e.g., BMI, heart rate, blood pressure).  
  - **Encounters.csv:** In-patient hospital admission details (admission/discharge dates, diagnosis codes).  
  - **Telemedicine_encounters.csv:** Remote consultation records (appointment dates, contact methods).  
  - **Patient_RX.csv:** Medication history (e.g., drugs for diabetes, hypertension).

Detailed documentation for setting up the database schema and populating the datasets is provided in the `/db` directory.

---

## Data Analysis with Python

### Project 1: Exploratory Data Analysis (EDA) & SQL Integration
- **Data Source:** Public hospital readmissions dataset.
- **Tools:** PostgreSQL, Python (Pandas).
- **Deliverables:**  
  - Optimized SQL queries (e.g., calculating readmission rates).  
  - An in-depth EDA report in Jupyter Notebook, highlighting key metrics and trends.

### Project 2: Predictive Modeling for Readmission Risk
- **Objective:** Predict the likelihood of a patient being readmitted within 30 days.
- **Data Integration:** Merging data from Patient_vitals, Encounters, and Patient_RX.
- **Key Steps:**  
  - **Data Cleaning:** Handle missing values, encode categorical variables, and standardize numerical values.
  - **Feature Engineering:**  
    - *Length of Stay* (derived from Admission_Date and Discharge_Date).  
    - *Time to Follow-Up* (difference between Discharge_Date and subsequent encounter date).  
    - *Medication Count* (number of medications prescribed).  
    - *Vital Sign Metrics* (BMI, heart rate, blood pressure).
  - **Modeling:**  
    - Target Variable: Readmission within 30 days.
    - Model: Logistic Regression (80/20 train-test split).
    - Evaluation: Accuracy, ROC AUC, and feature importance analysis.
- **Outcome:** A predictive model that identifies high-risk patients, with results exported for visualization in Power BI.

---

## Sample Dashboards

The Power BI dashboard illustrates:
- **Overview Metrics:** Readmission rates, average length of stay, and vital sign distributions.
- **Trend Analysis:** Interactive visuals showing the relationship between in-person encounters, follow-up telemedicine consultations, and patient outcomes.
- **Risk Segmentation:** Visual breakdown of patients by predicted readmission risk (low, medium, high).
- **Drill-Down Analysis:** The ability to click through from aggregated KPIs to individual patient journeys.

Screenshots and interactive examples are available in the `/dashboards` directory.

---

## Project Scenarios

### Scenario 1: Comprehensive Patient Journey Analysis

Using three datasets—Patient_vitals, Encounters, and Telemedicine_encounters—we analyze the entire care journey over the past two years. This scenario explores:
- **Integration:** How in-person clinical encounters drive follow-up telemedicine consultations.
- **Correlation:** The relationship between patient vitals and the likelihood of scheduling a telemedicine follow-up.
- **Insight:** Feature engineering (e.g., calculating the time gap between discharge and follow-up) to understand patient behavior and identify trends.

### Scenario 2: Predictive Modeling Analysis – Readmission Risk

In this scenario, I demonstrate an end-to-end data analytics workflow:
- **Data Integration:** Merging Patient_vitals.csv, Encounters.csv, and Patient_RX.csv on Patient_ID.
- **Data Preparation:** Cleaning, encoding, and feature engineering to create a dataset for modeling.
- **Exploratory Data Analysis (EDA):** Visual representation of key variables like length of stay and medication count against readmission outcomes.
- **Predictive Modeling:** Training a logistic regression model to predict readmission within 30 days.
- **Outcome Visualization:** Exporting model predictions for interactive exploration in Power BI, highlighting actionable insights for clinical interventions.

---

## Contributing / Feedback

Contributions and feedback are welcome! Please feel free to open an issue or submit a pull request if you have suggestions or improvements.

---

## License

This project is licensed under the 
