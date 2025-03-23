import os

# Read the SQL file
sql_file_path = "/Users/shermintalawrence/DA_project/src/JOIN_Drug_Trial_Eligibility"
with open(sql_file_path, "r") as file:
    sql_content = file.read()

# Convert the SQL content to HTML
html_content = f"<html><body><pre>{sql_content}</pre></body></html>"

# Save the HTML content to a file
html_output_path = "/Users/shermintalawrence/DA_project/output/JOIN_Drug_Trial_Eligibility.html"
os.makedirs(os.path.dirname(html_output_path), exist_ok=True)
with open(html_output_path, "w") as file:
    file.write(html_content)

print(f"HTML output saved to {html_output_path}")
