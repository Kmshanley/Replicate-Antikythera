import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from datetime import datetime, timedelta
import Orbit

plt.style.use('dark_background')
fig, ax = plt.subplots(figsize=(5, 5))
ax = plt.axes(xlim=(-2, 2), ylim=(-2, 2))

ax.plot(0, 0, '.', markersize=20, color="yellow")
plt.grid(True, lw=0.3)

plot, = ax.plot([], [], '.', markersize=10, color="skyblue")

x_pos = []
y_pos = []


earth = Orbit.Orbit(1.000000018, -0.00000003, 0.01671123, -0.00003661, -0.00054346, 0.01337178,
                    100.46691572, 35999.37306329, 102.93005885, 0.31795260, -5.11260389, -0.24123856)

target_date = datetime(2000,1,1)
step_size = timedelta(days=1)

for i in range(365):
    print(target_date)
    pos = earth.get_pos_at_date(target_date)
    print(pos)
    x_pos.append(pos[0])
    y_pos.append(pos[1])
    target_date = target_date + step_size

ax.plot(x_pos, y_pos, '--', linewidth=0.75, color="skyblue")

def animate(i):
    if (i % 50) == 0 and i != 0:
        print("Rendering: " + str(int(i / 10)) + " frames complete")

    return plot.set_data(x_pos[i], y_pos[i])

print("Begin Rendering")
anim = FuncAnimation(fig, animate, frames=365, interval=5, repeat=False)
anim.save('earth.gif', writer='pillow')
print("Rendering Complete - File Saved")
plt.show()



