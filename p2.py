import pandas as pd

# Read data from CSV into a data frame
df = pd.read_csv('random_data.csv')

# Display the original data frame
print("Original Data Frame:")
print(df)

# Handling missing values
df['Marks'] = df['Marks'].fillna(df['Marks'].mean())

# Display data after handling missing values
print("\nData Frame after handling missing values:")
print(df)

# Sorting the data frame by 'Age' in descending order
df_sorted = df.sort_values(by='Age', ascending=False)

# Display data after sorting
print("\nData Frame after sorting by Age in descending order:")
print(df_sorted)

# Filtering the data frame for students with marks greater than 75
df_filtered = df[df['Marks'] > 75]

# Display data after filtering
print("\nData Frame after filtering for students with marks > 75:")
print(df_filtered)

# Grouping data by 'Gender' and calculating mean age for each group
df_grouped = df.groupby('Gender')['Age'].mean()

# Display data after grouping
print("\nMean Age grouped by Gender:")
print(df_grouped)
