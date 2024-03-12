import pandas as pd
from scipy.stats import f_oneway
from statsmodels.stats.multicomp import pairwise_tukeyhsd
import scipy.stats as stats

group1 = [25, 30, 35, 40, 45]
group2 = [20, 22, 25, 28, 30]
group3 = [15, 18, 20, 22, 25]

data = pd.DataFrame({'value': group1 + group2 + group3,
                     'group': ['Group1'] * 5 + ['Group2'] * 5 + ['Group3'] * 5})

f_statistic, p_value = f_oneway(group1, group2, group3)

print("One-way ANOVA results:")
print(f"F-statistic: {f_statistic}")
print(f"P-value: {p_value}")

posthoc = pairwise_tukeyhsd(data['value'], data['group'])

print("\nTukey-Kramer post-hoc test results:")
print(posthoc)

group4 = [10, 12, 15, 18, 20]
all_data = group1 + group2 + group3 + group4
group_labels = ['Group 1'] * len(group1) + ['Group 2'] * len(group2) + ['Group 3'] * len(group3) + ['Group 4'] * len(group4)

anova_result = stats.f_oneway(group1, group2, group3, group4)
print("\nOne-way ANOVA results for additional example:")
print(f"Statistic: {anova_result.statistic}")
print(f"P-value: {anova_result.pvalue}")

tukey_result = pairwise_tukeyhsd(all_data, group_labels)
print("\nTukey's HSD results for additional example:")
print(tukey_result)

tukey_result.plot_simultaneous()
