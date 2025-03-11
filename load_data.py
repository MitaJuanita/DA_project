import pandas as pd
from sqlalchemy import create_engine

# Database connection parameters
db_config = {
    'user': 'shermintalawrence',  # Replace with your actual username
    'password': 'mita5466',  # Replace with your actual password
    'host': 'localhost',
    'port': '5432',
    'database': 'postgres'
}

# Create a database connection
engine = create_engine(f"postgresql+psycopg2://{db_config['shermintalawrence']}:{db_config['mita5466']}@{db_config['127.0.0.1']}:{db_config['5432']}/{db_config['postgres']}")

# Load patient_vitals data from CSV
patient_vitals_df = pd.read_csv('tests/patient_vitals.csv')
patient_vitals_df.to_sql('patient_vitals', engine, if_exists='append', index=False)

# Load encounters data from CSV
encounters_df = pd.read_csv('tests/encounters.csv')
encounters_df.to_sql('encounters', engine, if_exists='append', index=False)

print("Data loaded successfully.")
