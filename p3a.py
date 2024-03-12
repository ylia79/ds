import pandas as pd
from sklearn.preprocessing import StandardScaler, MinMaxScaler

# Read data from CSV
df_education = pd.read_csv('education_data.csv')

print("Original Data:")
print(df_education)

# Define numerical and categorical columns
numerical_columns = ['YearsOfStudy', 'GPA', 'Income']
categorical_columns = ['EducationLevel', 'EmploymentStatus']

# Standardize numerical columns
scaler_standard = StandardScaler()
df_education_standardized = df_education.copy()
df_education_standardized[numerical_columns] = scaler_standard.fit_transform(df_education[numerical_columns])

# Normalize numerical columns
scaler_minmax = MinMaxScaler()
df_education_normalized = df_education.copy()
df_education_normalized[numerical_columns] = scaler_minmax.fit_transform(df_education[numerical_columns])

print("\nData after Standardization:")
print(df_education_standardized)

print("\nData after Normalization:")
print(df_education_normalized)
