import pandas as pd
from sqlalchemy import create_engine

# FETCH DATA in Pandas: Database connection parameters
engine = create_engine(
    'postgresql://shermintalawrence:mita5466@localhost:5432/postgres'
)
# Display the first 5 rows of the DataFrame
vitals_df = pd.read_sql('SELECT * FROM patient_vitals', engine)
encounters_df = pd.read_sql('SELECT * FROM encounters', engine)

