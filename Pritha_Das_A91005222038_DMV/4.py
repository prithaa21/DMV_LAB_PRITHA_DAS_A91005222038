# To draw a moving circle animated

import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Creating figure and axis
fig, ax = plt.subplots()

ax.set_xlim(0, 10)
ax.set_ylim(0, 10)

# Creating circle
circle = plt.Circle((0, 5), 0.5, color='pink')
ax.add_patch(circle)

# Animation function
def update(frame):
    circle.center = (frame, 5)
    return circle,

# Creating animation
ani = FuncAnimation(fig, update, frames=range(0, 11), interval=200)

plt.title("Moving Circle Animation")
plt.xlabel("X-AXIS")
plt.ylabel("Y-AXIS")
plt.show()
