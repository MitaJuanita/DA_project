import pandas as pd

print("Reading encounters.csv")
encounters_df = pd.read_csv("tests/encounters.csv")
print("Reading patient_vitals.csv")
patient_vitals_df = pd.read_csv("tests/patient_vitals.csv")
print("Reading patient_rx.csv")
patient_rx_df = pd.read_csv("tests/patient_rx.csv")

print("Merging encounters and patient vitals")
merged_1 = pd.merge(
    encounters_df,
    patient_vitals_df,
    on="patient_id",   # shared key column name
    how="left"        
)
print("Merging with patient_rx")
merged_df = pd.merge(
    merged_1,
    patient_rx_df,
    on="patient_id",
    how="left"
)

print("Merged DataFrame created")

# Show a summary of the DataFrame (column types, non-null counts)
merged_df.info()

# Basic descriptive statistics for numeric columns
merged_df.describe()

# Show first few rows
merged_df.head()

# Show last few rows
merged_df.tail()

# Random sample of 5 rows
merged_df.sample(5)

# Shape (rows, columns)
merged_df.shape

# Column names
merged_df.columns

# Data types of each column
merged_df.dtypes

# Count missing values in each column
merged_df.isnull().sum()

# Number of unique values in each column
merged_df.nunique()

# Save the DataFrame as an HTML file
html_output = merged_df.to_html()
with open("output/merged_dataframe.html", "w") as file:
    file.write(html_output)
print("HTML output saved to output/merged_dataframe.html")

# Save the DataFrame as a CSV file
csv_output = "output/merged_dataframe.csv"
merged_df.to_csv(csv_output, index=False)
print(f"CSV output saved to {csv_output}")
