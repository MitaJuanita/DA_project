import pandas as pd

# Read the CSV file
csv_file_path = "/Users/shermintalawrence/Downloads/Clinical_Trial Data.csv"
df = pd.read_csv(csv_file_path)

# Convert the DataFrame to HTML
html_output = df.to_html(index=False)

# Save the HTML content to a file
html_output_path = "/Users/shermintalawrence/DA_project/output/Clinical_Trial_Data.html"
with open(html_output_path, "w") as file:
    file.write(html_output)

print(f"HTML output saved to {html_output_path}")
