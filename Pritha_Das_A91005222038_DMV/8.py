#To draw a pie chart (with user inputs)
import matplotlib.pyplot as plt

# Number of categories
n = int(input("Enter number of categories: "))

labels = []
values = []

# Taking user input
for i in range(n):
    label = input(f"Enter label for category {i+1}: ")
    value = float(input(f"Enter value for {label}: "))
    
    labels.append(label)
    values.append(value)

# Plotting pie chart
plt.pie(values, labels=labels, autopct='%1.1f%%')

plt.title("Dynamic Pie Chart")
plt.show()
