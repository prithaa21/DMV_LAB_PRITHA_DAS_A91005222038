#To draw a scatter plot(with already given inputs)
import matplotlib.pyplot as plt

# Sample data
x = [3, 12, 7, 18, 5, 10, 2, 15, 9, 6]
y = [78, 110, 89, 120, 84, 96, 70, 115, 93, 88]


# Create scatter plot
plt.scatter(x, y, color='pink', marker='o', s=100)  # s = size of points

# Add title and labels
plt.title("Static Scatter Plot")
plt.xlabel("X Axis")
plt.ylabel("Y Axis")

plt.grid(True)
plt.show()
