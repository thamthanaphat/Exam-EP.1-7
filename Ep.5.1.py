import numpy as np
import matplotlib.pyplot as plt

def create_scatter_plot_with_line(friends_data):
    names = list(friends_data.keys())
    ages = [friend.get("age", 0) for friend in friends_data.values()]
    incomes = [friend.get("income", 0) for friend in friends_data.values()]

    # Fit a linear regression line
    coefficients = np.polyfit(ages, incomes, 1)
    line = np.polyval(coefficients, ages)

    plt.scatter(ages, incomes, color='purple', marker='o', label='Data Points')
    plt.plot(ages, line, color='orange', label='Regression Line')

    plt.xlabel('Age')
    plt.ylabel('Income (in $)')
    plt.title('Scatter Plot with Regression Line: Age vs. Income of Friends')
    plt.legend()
    plt.show()

# Create a dictionary with names, ages, and incomes
friends = {
    "Alice": {"age": 25, "income": 50000},
    "Bob": {"age": 30, "income": 60000},
    "Charlie": {"age": 35, "income": 75000},
    "David": {"age": 28, "income": 55000},
    "Emma": {"age": 32, "income": 70000},
    "Frank": {"age": 40, "income": 80000},
    "Grace": {"age": 22, "income": 48000},
    "Henry": {"age": 38, "income": 90000},
    "Ivy": {"age": 27, "income": 62000},
    "Jack": {"age": 33, "income": 72000},
}

# Call the create_scatter_plot_with_line function
create_scatter_plot_with_line(friends)
