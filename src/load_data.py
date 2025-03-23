import pandas as pd
from sqlalchemy import create_engine

def load_csv_to_sql(file_path, table_name, engine, if_exists='append'):
    """
    Load a CSV file into the specified SQL table.
    
    Parameters:
      - file_path: Path to the CSV file.
      - table_name: Target table name in the database.
      - engine: SQLAlchemy engine object.
      - if_exists: Action if the table already exists ('append', 'replace', or 'fail').
    """
    try:
        df = pd.read_csv(file_path)
        df.to_sql(table_name, engine, if_exists=if_exists, index=False)
        print(f"Loaded {len(df)} rows into '{table_name}' from '{file_path}'")
    except Exception as e:
        print(f"Error loading data from {file_path} into '{table_name}': {e}")

def main(): # def wrapper function
    # Database connection parameters
    db_config = {
        'user': 'shermintalawrence',  # Replace with your actual username if different
        'password': 'mita5466',       # Replace with your actual password
        'host': '127.0.0.1',
        'port': '5432',
        'database': 'postgres'        # Or your specific DB name
    }

    # Create a database connection using SQLAlchemy
    engine = create_engine(
        f"postgresql+psycopg2://{db_config['user']}:{db_config['password']}"
        f"@{db_config['host']}:{db_config['port']}/{db_config['database']}"
    )

    # Load patient_vitals data from CSV
    load_csv_to_sql('tests/patient_vitals.csv', 'patient_vitals', engine)

    # Load encounters data from CSV
    load_csv_to_sql('tests/encounters.csv', 'encounters', engine)

    #load patient_rx data from CSV
    load_csv_to_sql('tests/patient_rx.csv', 'patient_rx', engine)
    
    #load merged_dataframe.csv from CSV
    load_csv_to_sql('output/merged_dataframe.csv', 'merged_dataframe', engine)
    
    

    

    print("Data loaded successfully.")
    engine.dispose()

if __name__ == "__main__":
    main()
