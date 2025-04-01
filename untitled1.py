# trial_eligibility_summary.ipynb (for use in Jupyter)

import pandas as pd
import matplotlib.pyplot as plt
from trial_eligibility import load_patient_data, load_trial_criteria, assign_trial_groups

# Step 1: Load data
patients = load_patient_data()
criteria = load_trial_criteria()

# Step 2: Run assignment with reason tracking
results = assign_trial_groups(patients, criteria, return_reasons=True)

# Step 3: View eligible patients
eligible_patients = results[results['eligible']]
display(eligible_patients)

# Step 4: View ineligible patients with reasons
ineligible = results[~results['eligible'] & results['ineligibility_reason'].notna()]
display(ineligible[['Patient_ID', 'trial_group', 'ineligibility_reason']])

# Step 5: Explode and count ineligibility reasons
ineligible_exploded = ineligible.copy()
ineligible_exploded['reason_list'] = ineligible_exploded['ineligibility_reason'].str.split('; ')
reason_counts = ineligible_exploded.explode('reason_list')['reason_list'].value_counts()

# Step 6: Plot reasons
plt.figure(figsize=(8, 5))
reason_counts.plot(kind='barh', color='salmon', edgecolor='black')
plt.title("Top Ineligibility Reasons")
plt.xlabel("Number of Patients")
plt.ylabel("Reason")
plt.tight_layout()
plt.grid(axis='x', linestyle='--', alpha=0.5)
plt.show()
