import scipy.stats as stats 

group1 = [25, 30, 35, 40, 45] 

group2 = [20, 22, 25, 28, 30] 

group3 = [15, 18, 20, 22, 25] 

statistic, p_value = stats.f_oneway(group1, group2, group3) 

print("One-way ANOVA results:") 

print(f"Statistic: {statistic}") 

print(f"P-value: {p_value}") 

alpha = 0.05 
if p_value < alpha: 
    print("Reject the null hypothesis. There are significant differences between group means.") 
else: 
    print("Fail to reject the null hypothesis. No significant differences between group means.") 

 

 

 

 

 

 

 
