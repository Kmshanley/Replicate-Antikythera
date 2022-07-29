# Earth Sun Moon

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation


class Body:
    def __init__(self, name, radius_of_orbit, orbit_time_in_years, color, draw_size, parent=None):
        self.name = name
        self.radius_of_orbit = radius_of_orbit
        self.orbit_time_in_years = orbit_time_in_years
        self.color = color
        self.draw_size = draw_size
        self.parent = parent

        n_points = 40000
        theta = np.linspace(0, 400 * np.pi, n_points)
        if parent is None:
            self.x = (radius_of_orbit * np.sin((1 / orbit_time_in_years) * theta))
            self.y = (radius_of_orbit * np.cos((1 / orbit_time_in_years) * theta))
        else:
            self.x = (radius_of_orbit * np.sin((1 / orbit_time_in_years) * theta)) + parent.x
            self.y = (radius_of_orbit * np.cos((1 / orbit_time_in_years) * theta)) + parent.y


plt.style.use('dark_background')

solar_system = []
days = 365.26

solar_system.append(Body("Mercury", 1.5, (89.97 / days), "darkgoldenrod", 7))
solar_system.append(Body("Venus", 3, (224.7 / days), "cornsilk", 10))
solar_system.append(Body("Earth", 4.5, 1, "skyblue", 10))
solar_system.append(Body("Moon", 0.75, 27 / days, "lightgray", 5, parent=solar_system[2]))
solar_system.append(Body("Mars", 6, 1.88, "orangered", 9))
solar_system.append(Body("Jupiter", 7.5, 11.86, "sandybrown", 20))
solar_system.append(Body("Saturn", 9, 29.46, "khaki", 17))
solar_system.append(Body("Uranus", 10.5, 84.01, "paleturquoise", 12))
solar_system.append(Body("Neptune", 12, 164.79, "mediumblue", 15))

fig, ax = plt.subplots(figsize=(5, 5))
ax = plt.axes(xlim=(-15, 15), ylim=(-15, 15))
ss_plots = []

for body in solar_system:
    plot_return, = ax.plot([], [], '.', markersize=body.draw_size, color=body.color)
    ss_plots.append(plot_return)

ax.plot(0, 0, '.', markersize=20, color="yellow")
plt.grid(True, lw=0.3)

for body in solar_system:
    if body.parent is None:
        ax.plot(body.x, body.y, '--', linewidth=0.75, color=body.color)


def animate(i):
    if (i % 50) == 0 and i != 0:
        print("Rendering: " + str(int(i / 10)) + "%")

    for x in range(len(solar_system)):
        ss_plots[x].set_data(solar_system[x].x[i], solar_system[x].y[i])

    return ss_plots


print("Begin Rendering")
anim = FuncAnimation(fig, animate, frames=1000, interval=5, repeat=False)
anim.save('solar_system.gif', writer='pillow')
print("Rendering Complete - File Saved")
plt.show()
