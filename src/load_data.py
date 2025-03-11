import pandas as pd
from sqlalchemy import create_engine

# Database connection parameters
db_config = {
    'user': 'shermintalawrence',  # Replace with your actual username if different
    'password': 'mita5466',       # Replace with your actual password
    'host': '127.0.0.1',
    'port': '5432',
    'database': 'postgres'        # Or your specific DB name
}

# Create a database connection
# Note how we use the dictionary keys: db_config['user'], db_config['password'], etc.
engine = create_engine(
    f"postgresql+psycopg2://{db_config['user']}:{db_config['password']}"
    f"@{db_config['host']}:{db_config['port']}/{db_config['database']}"
)

# Load patient_vitals data from CSV

patient_vitals_df = pd.read_csv('tests/patient_vitals.csv')
# 'append' means it will insert rows into an existing table or create one (if you have permissions).
patient_vitals_df.to_sql('patient_vitals', engine, if_exists='append', index=False)

# Load encounters data from CSV
encounters_df = pd.read_csv('tests/encounters.csv')
encounters_df.to_sql('encounters', engine, if_exists='append', index=False)

print("Data loaded successfully.")
