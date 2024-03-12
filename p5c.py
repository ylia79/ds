import csv
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import ttest_ind

# Function to read dataset from CSV file
def read_from_csv(filename):
    data = []
    with open(filename, 'r') as csvfile:
        csv_reader = csv.reader(csvfile)
        next(csv_reader)  # Skip the header
        for row in csv_reader:
            data.append([float(row[0]), float(row[1])])
    return data

# Read the dataset from the CSV file
csv_filename = 'hypothesis_testing_dataset.csv'
dataset = read_from_csv(csv_filename)

# Extracting values for the t-test
control_group = np.array([row[0] for row in dataset])
treatment_group = np.array([row[1] for row in dataset])

# Conducting t-test
t_statistic, p_value = ttest_ind(control_group, treatment_group)

# Plotting the distributions
plt.figure(figsize=(18, 6))
plt.hist(control_group, alpha=0.85, label='Control Group')
plt.hist(treatment_group, alpha=0.5, label='Treatment Group')
plt.axvline(np.mean(control_group), color='blue', linestyle='dashed', linewidth=2, label='Control Mean')
plt.axvline(np.mean(treatment_group), color="orange", linestyle='dashed', linewidth=2, label='Treatment Mean')
plt.title('Distribution of Control and Treatment Groups')
plt.xlabel('Response Value')
plt.ylabel('Frequency')
plt.legend()
plt.grid(True)

# Highlight the statistically significant difference
if p_value < 0.05:
    plt.text(40, 12, f'Significant Difference\np-value: {p_value:.3f}', bbox=dict(facecolor='red', alpha=0.5))

plt.show()

# Determine conclusion based on p-value
alpha = 0.05  # Significance level
if p_value < alpha:
    print("\nConclusion: Reject the null hypothesis. There is significant evidence that the new drug has an effect.")
else:
    print("\nConclusion: Fail to reject the null hypothesis. There is insufficient evidence that the new drug has an effect.")
