#To draw a bar chart(with user inputs)
import matplotlib.pyplot as plt

# Number of categories
n = int(input("Enter number of languages: "))

labels = []
values = []

# Taking user input
for i in range(n):
    label = input(f"Enter language {i+1}: ")
    value = float(input(f"Enter score for {label}: "))
    
    labels.append(label)
    values.append(value)

# Plotting bar chart
plt.bar(labels, values, color = 'pink')

plt.xlabel("Languages")
plt.ylabel("Scores")
plt.title("Dynamic Bar Chart")

plt.show()
