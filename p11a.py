import matplotlib.pyplot as plt
import numpy as np

categories = ['Category A', 'Category B', 'Category C', 'Category D']
values1 = [30, 45, 25, 50]
values2 = [20, 35, 40, 30]

def plot_bar_chart():
    plt.figure(figsize=(8, 6))
    plt.bar(categories, values1, label='Dataset 1', color='blue', alpha=0.7)
    plt.bar(categories, values2, label='Dataset 2', color='orange', alpha=0.7, bottom=values1)
    plt.xlabel('Categories')
    plt.ylabel('Values')
    plt.title('Comparison of Dataset 1 and Dataset 2')
    plt.legend()
    plt.show()

def plot_line_chart():
    time_periods = np.arange(1, 6)
    trend1 = [10, 25, 30, 20, 35]
    trend2 = [15, 30, 25, 40, 30]
    plt.figure(figsize=(8, 6))
    plt.plot(time_periods, trend1, marker='o', label='Trend 1', linestyle='-', color='green')
    plt.plot(time_periods, trend2, marker='s', label='Trend 2', linestyle='--', color='purple')
    plt.xlabel('Time Periods')
    plt.ylabel('Values')
    plt.title('Trends Over Time')
    plt.legend()
    plt.show()

def plot_pie_chart():
    plt.figure(figsize=(8, 8))
    plt.pie(values1, labels=categories, autopct='%1.1f%%', startangle=90, colors=['red', 'yellow', 'blue', 'green'])
    plt.title('Percentage Distribution of Categories')
    plt.show()

plot_bar_chart()
plot_line_chart()
plot_pie_chart()
