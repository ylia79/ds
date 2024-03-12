import pandas as pd
from sklearn.preprocessing import StandardScaler, MinMaxScaler

# Read the CSV file
df_education = pd.read_csv('education_data.csv')

# Print the original data
print("Original Data:")
print(df_education)

# Define numerical and categorical columns
numerical_columns = ['YearsOfStudy', 'GPA', 'Income']
categorical_columns = ['EducationLevel', 'EmploymentStatus']

# Create a StandardScaler object
scaler_standard = StandardScaler()

# Create a copy of the dataframe for standardization
df_education_standardized = df_education.copy()

# Standardize numerical columns
df_education_standardized[numerical_columns] = scaler_standard.fit_transform(df_education[numerical_columns])

# Create a MinMaxScaler object
scaler_minmax = MinMaxScaler()

# Create a copy of the dataframe for normalization
df_education_normalized = df_education.copy()

# Normalize numerical columns
df_education_normalized[numerical_columns] = scaler_minmax.fit_transform(df_education[numerical_columns])

# Create a dataframe with dummies for categorical columns
df_dummies = pd.get_dummies(df_education, columns=categorical_columns)

# Print the data after feature dummification
print("\nData after Feature Dummification:")
print(df_dummies.T)
