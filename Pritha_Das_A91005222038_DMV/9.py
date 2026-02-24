#To draw a bar chart(with already given inputs)
import matplotlib.pyplot as plt

# Sample data
categories = ['A', 'B', 'C', 'D', 'E']
values = [35, 20, 9, 14, 24]

# Create bar chart
plt.bar(categories, values, color='pink')

# Add title and labels
plt.title("Static Bar Chart")
plt.xlabel("Categories")
plt.ylabel("Values")

# Add grid lines
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Display chart
plt.show()
