#3) Import an meaningful csv file for data analysis and perform data cleaning, and analysis for meaningful output

import pandas as pd

# Load Dataset
df = pd.read_csv("Cardiovascular_Disease_Dataset.csv")

print("First 5 Rows:\n")
print(df.head())

print("\nDataset Shape:")
print(df.shape)

print("\nColumn Names:")
print(df.columns)

print("\nMissing Values:")
print(df.isnull().sum())

print("\nDataset Information:\n")
print(df.info())


# Remove duplicates
df = df.drop_duplicates()

print("\nDuplicates Removed")

# Fill missing values with mean
numeric_columns = df.select_dtypes(include=['int64', 'float64']).columns

for col in numeric_columns:
    df[col] = df[col].fillna(df[col].mean())

print("\nMissing numeric values filled")


print("\nStatistical Summary:\n")
print(df.describe())

# Average of age
print("\nAverage Age:")
print(df['age'].mean())

# Max Cholesterol
print("\nHighest Cholesterol:")
print(df["serumcholestrol"].max())

# Count Patients
print("\nPatient Count:")
print(df['patientid'].value_counts())

# Patients with High BP
high_bp = df[df["restingBP"] > 140]
print("\nPatients with High Blood Pressure:")
print(high_bp)

# Top 5 oldest patients
oldest = df.sort_values(by="age", ascending=False)

print("\nTop 5 Oldest Patients:")
print(oldest.head())

#Save result
df.to_csv("cleaned_cardiovascular_data.csv", index=False)

print("\nCleaned dataset saved successfully")