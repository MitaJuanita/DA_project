import pandas as pd

# Read CSV into a DataFrame
df = pd.read_csv('tests/patient_vitals.csv')

# For SQL data, you could do:
# df = pd.read_sql("SELECT * FROM table_name", your_engine)

df.info()
df.describe()
df.head()
df.tail()
df.sample(5)
df.shape
df.columns
df.dtypes
df.isnull().sum()
df.nunique()
