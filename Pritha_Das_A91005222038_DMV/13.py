#To create a subplot
import matplotlib.pyplot as plt

# Given data
x = [5, 7, 8, 7, 2, 17, 2, 9, 4, 11]
y = [99, 86, 87, 88, 100, 86, 103, 87, 94, 78]

# Create figure with 2 subplots
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(8, 12))

# --- Bar Chart ---
ax1.bar(x, y, color='skyblue', edgecolor='black')
ax1.set_title("Bar Chart", fontsize=13)
ax1.set_ylabel("Values")
ax1.grid(axis='y', linestyle='--', alpha=0.6)

# --- Scatter Plot ---
ax2.scatter(x, y, color='pink', s=80, edgecolors='black')
ax2.set_title("Scatter Plot", fontsize=13)
ax2.set_ylabel("Values")
ax2.grid(True, linestyle='--', alpha=0.6)

# Overall title
fig.suptitle("Visualization of Given Dataset", fontsize=16, fontweight='bold')

# Adjust layout
plt.tight_layout()
plt.show()
