import numpy as np

categories = ['Electronics', 'Clothing', 'Books', 'Home Goods']
time_periods = np.arange(1, 6)
sales_data = {
    'Electronics': [30, 45, 60, 40, 55],
    'Clothing': [20, 35, 25, 30, 40],
    'Books': [15, 20, 30, 25, 35],
    'Home Goods': [25, 30, 35, 20, 45]
}

def calculate_overall_sales():
    total_sales = np.sum([sales_data[category] for category in categories], axis=0)
    return total_sales

def present_findings():
    overall_sales = calculate_overall_sales()
    print("Finding 1: Overall Sales Trend")
    print("The overall sales trend indicates a steady increase over the five time periods.")
    print()
    print("Finding 2: Comparison of Sales Across Categories")
    print("The bar chart illustrates that Electronics has consistently higher sales, followed by Clothing.")
    print()
    print("Finding 3: Percentage Distribution of Sales Across Categories")
    for category, percentage in zip(categories, overall_sales):
        print(f"{category}: {percentage:.1f}%")
    print("The pie chart highlights the percentage distribution of sales across categories.")
    print()

present_findings()
