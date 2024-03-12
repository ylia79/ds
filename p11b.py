import matplotlib.pyplot as plt
import numpy as np

categories = ['Electronics', 'Clothing', 'Books', 'Home Goods']
time_periods = np.arange(1, 6)
sales_data = {
    'Electronics': [30, 45, 60, 40, 55],
    'Clothing': [20, 35, 25, 30, 40],
    'Books': [15, 20, 30, 25, 35],
    'Home Goods': [25, 30, 35, 20, 45]
}

def plot_overall_trend():
    plt.figure(figsize=(10, 6))
    for category in categories:
        plt.plot(time_periods, sales_data[category], marker='o', label=category)
    plt.xlabel('Time Periods')
    plt.ylabel('Sales')
    plt.title('Overall Sales Trend Over Time')
    plt.legend()
    plt.show()

def plot_category_comparison():
    plt.figure(figsize=(8, 6))
    for i, category in enumerate(categories):
        plt.bar(time_periods + i * 0.2, sales_data[category], width=0.2, label=category)
    plt.xlabel('Time Periods')
    plt.ylabel('Sales')
    plt.title('Comparison of Sales Across Categories')
    plt.legend()
    plt.show()

def plot_percentage_distribution():
    total_sales = np.sum([sales_data[category] for category in categories], axis=0)
    labels = [f'{category}: {percentage:.1f}%' for category, percentage in zip(categories, total_sales)]
    plt.figure(figsize=(8, 8))
    plt.pie(total_sales, labels=labels, autopct='%1.1f%%', startangle=90)
    plt.title('Percentage Distribution of Sales Across Categories')
    plt.show()

plot_overall_trend()
plot_category_comparison()
plot_percentage_distribution()
