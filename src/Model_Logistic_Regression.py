import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, roc_auc_score, classification_report

# Assume df is your merged DataFrame with a 'readmitted' column (1 if readmitted within 30 days, else 0)
# And that you have already engineered features like 'length_of_stay', 'medication_count', etc.
src = 'src'  # Define the path to your CSV file
df = pd.read_csv(src + '/readmission_risk.csv')  # Add this line to define df
features = ['BMI', 'Heart_Rate', 'Blood_Pressure', 'length_of_stay', 'medication_count']
X = df[features]
y = df['readmitted']

# Splitting the data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Model training
model = LogisticRegression()
model.fit(X_train, y_train)

# Predictions and evaluation
y_pred = model.predict(X_test)
y_prob = model.predict_proba(X_test)[:, 1]

print("Accuracy:", accuracy_score(y_test, y_pred))
print("ROC AUC:", roc_auc_score(y_test, y_prob))
print(classification_report(y_test, y_pred))
