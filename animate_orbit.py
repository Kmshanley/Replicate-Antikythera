import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from datetime import datetime, timedelta
import Orbit


class Body:
    def __init__(self, name, orbit, color, draw_size, parent=None):
        self.name = name
        self.orbit = orbit
        self.color = color
        self.draw_size = draw_size
        self.parent = parent
        self.x_path = []
        self.y_path = []


def animate_solar_system(solar_system, start_date, length, step_length):
    frames = int(length / step_length)
    print(frames)

    plt.style.use('dark_background')
    fig, ax = plt.subplots(figsize=(5, 5))
    ax = plt.axes(xlim=(-2, 2), ylim=(-2, 2))

    ax.plot(0, 0, '.', markersize=20, color="yellow")
    plt.grid(True, lw=0.3)
    ss_plots = []

    for body in solar_system:
        plot_return, = ax.plot([], [], '.', markersize=body.draw_size, color=body.color)
        ss_plots.append(plot_return)
        print(body.name + " added to ss_plots")

        if body.parent is None:
            for frame_num in range(frames):
                coordinates = body.orbit.get_pos_at_date(start_date + (frame_num * step_length))
                body.x_path.append(coordinates[0])
                body.y_path.append(coordinates[1])

            ax.plot(body.x_path, body.y_path, '-', linewidth=0.75, color=body.color)

    def animate(i):
        if (i % 50) == 0 and i != 0:
            print("Rendering: " + str(int(i)) + "/" + str(frames) + " frames completed")

        for x in range(len(solar_system)):
            ss_plots[x].set_data(solar_system[x].x_path[i], solar_system[x].y_path[i])

        return ss_plots

    print("Begin Rendering")
    anim = FuncAnimation(fig, animate, frames=frames, interval=5, repeat=False)
    anim.save('rocky_planets.gif', writer='pillow')
    print("Rendering Complete - File Saved")
    plt.show()


mercury_orbit = Orbit.Orbit(0.38709843, 0, 0.20563661, 0.00002123, 7.00559432, -0.00590158,
                            252.25166724, 149472.67486623, 77.45771895, 0.15940013, 48.33961819, -0.12214182)

venus_orbit = Orbit.Orbit(0.72332102, -0.00000026, 0.00676399, -0.00005107, 3.39777545, 0.00043494,
                          181.97970850, 58517.81560260, 131.76755713, 0.05679648, 76.67261496, -0.27274174)

earth_orbit = Orbit.Orbit(1.000000018, -0.00000003, 0.01671123, -0.00003661, -0.00054346, 0.01337178,
                          100.46691572, 35999.37306329, 102.93005885, 0.31795260, -5.11260389, -0.24123856)

mars_orbit = Orbit.Orbit(1.52371243, 0.00000097, 0.09336511, 0.00009149, 1.85181869, -0.00724757,
                         -4.56813164, 19140.29934243, -23.91744784, 0.45223625, 49.71320984, -0.26852431)

mercury = Body("Mercury", mercury_orbit, "darkgoldenrod", 7)
venus = Body("Venus", venus_orbit, "bisque", 10)
earth = Body("Earth", earth_orbit, "skyblue", 10)
mars = Body("Mars", mars_orbit, "orangered", 9)

solar = [mercury, venus, earth, mars]

animate_solar_system(solar, datetime(2022, 7, 30), timedelta(days=1000), timedelta(days=1))
