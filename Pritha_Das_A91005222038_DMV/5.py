# To draw an animated line
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

fig, ax = plt.subplots()

ax.set_xlim(0, 10)
ax.set_ylim(0, 100)

x_data = []
y_data = []

line, = ax.plot([], [], color='pink')

def update(frame):
    x_data.append(frame)
    y_data.append(frame * frame)   # y = x²
    line.set_data(x_data, y_data)
    return line,

ani = FuncAnimation(fig, update, frames=range(0, 11), interval=300)

plt.title("Animated Line Graph (y = x^2)")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.show()

