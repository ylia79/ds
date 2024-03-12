import csv
from scipy.stats import ttest_ind

def read_from_csv(filename):
    data = []
    with open(filename, 'r') as csvfile:
        csv_reader = csv.reader(csvfile)
        next(csv_reader)  # Skip the header
        for row in csv_reader:
            data.append([float(row[0]), float(row[1])])
    return data

# Read the dataset
csv_filename = 'hypothesis_testing_dataset.csv'
dataset = read_from_csv(csv_filename)

# Extract control and treatment groups
control_group = [row[0] for row in dataset]
treatment_group = [row[1] for row in dataset]

# Perform t-test
t_statistic, p_value = ttest_ind(control_group, treatment_group)

print(f"Test Statistic: {t_statistic:.2f}")
print(f"P-value: {p_value:.2f}")

# Set significance level
alpha = 0.85

# Compare p-value with alpha to make a conclusion
if p_value < alpha:
    print("\nConclusion: Reject the null hypothesis. There is significant evidence that the new drug has an effect.")
else:
    print("\nConclusion: Fail to reject the null hypothesis. There is insufficient evidence that the new drug has an effect.")
