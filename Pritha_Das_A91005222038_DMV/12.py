#To draw a scatter plot(with user inputs)
import matplotlib.pyplot as plt

# Number of data points
n = int(input("Enter number of data points: "))

x = []
y = []

# Taking user input
for i in range(n):
    x_value = float(input(f"Enter x value {i+1}: "))
    y_value = float(input(f"Enter y value {i+1}: "))
    
    x.append(x_value)
    y.append(y_value)

# Plotting scatter plot
plt.scatter(x, y, color='pink')

plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.title("User Input Scatter Plot")

plt.show()
