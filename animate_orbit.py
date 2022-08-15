import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from datetime import datetime, timedelta
def animate_solar_system(solar_system, start_date: datetime, length: timedelta,
                         step_length: timedelta, size, fileout_name=None, command=None):
    frames = int(length / step_length)
    print(frames)
    plt.style.use('dark_background')
    fig, ax = plt.subplots(figsize=(5, 5))
    ax = plt.axes(xlim=((0 - size), size), ylim=((0 - size), size))

    ax.plot(0, 0, '.', markersize=20, color="yellow")
    plt.grid(True, lw=0.3)
    ss_plots = []

    for body in solar_system:
        plot_return, = ax.plot([], [], '.', markersize=body.draw_size, color=body.color)
        ss_plots.append(plot_return)

        # if body.parent is None:
        #     for frame_num in range(frames):
        #         coordinates = body.orbit.get_pos_at_date(start_date + (frame_num * step_length))
        #         body.x_path.append(coordinates[0])
        #         body.y_path.append(coordinates[1])

        #     ax.plot(body.x_path, body.y_path, '-', linewidth=0.75, color=body.color)

    def animate(i):
        if (i % 50) == 0 and i != 0:
            print("Rendering: " + str(int(i)) + "/" + str(frames) + " frames completed")
            command()
        
        plt.title(str(start_date.date() + (step_length * i)))

        for x in range(len(solar_system)):
            ss_plots[x].set_data(solar_system[x].x_path[i], solar_system[x].y_path[i])
        return ss_plots
    
    #print("Begin Rendering")
    #anim = FuncAnimation(fig, animate, frames=frames, interval=5, repeat=False)
    #if fileout_name is not None:
        #anim.save(fileout_name, writer='pillow')
    #print("Rendering Complete - File Saved")
    command()

    plt.show()
