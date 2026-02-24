#To draw a pie chart (with already given inputs)
import matplotlib.pyplot as plt

# Sample data
labels = ['Fiction', 'Young-Adult', 'Thriller', 'Romance',' Fantasy']
sizes = [35, 15, 20, 10, 20]  # Percentages or values
colors = ['pink', 'lightblue', 'maroon', 'red', 'purple']

# Drawing pie chart
plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=90)

# Making the pie chart a circle
plt.axis('equal')

plt.title("BOOK GENRES")
plt.show()
