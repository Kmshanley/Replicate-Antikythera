# Earth Sun Moon

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation

plt.style.use('dark_background')

n_points=40000
theta = np.linspace(0,400 * np.pi, n_points)
mercury_radius = 1.5
v_radius = 3
e_radius = 4.5
moon_radius = 0.75
mars_radius = 6
j_radius = 7.5
s_radius = 9
u_radius = 10.5
n_radius = 12

days = 365.26
mercury_x = (mercury_radius * np.sin((1/(89.97/days))*theta))
mercury_y = (mercury_radius * np.cos((1/(89.97/days))*theta))

v_x = (v_radius * np.sin((1/(224.7/days))*theta))
v_y = (v_radius * np.cos((1/(224.7/days))*theta))

e_x = e_radius * np.sin(theta)
e_y = e_radius * np.cos(theta)

moon_x = (moon_radius * np.sin(30*theta)) + e_x
moon_y = (moon_radius * np.cos(30*theta)) + e_y
 
mars_x = (mars_radius * np.sin(1/1.88*theta))   
mars_y = (mars_radius * np.cos(1/1.88*theta)) 

j_x = (j_radius * np.sin(1/11.86*theta))
j_y = (j_radius * np.cos(1/11.86*theta))

s_x = (s_radius * np.sin(1/29.46*theta))
s_y = (s_radius * np.cos(1/29.46*theta))

u_x = (u_radius * np.sin(1/84.01*theta))
u_y = (u_radius * np.cos(1/84.01*theta))

n_x = (n_radius * np.sin(1/164.79*theta))
n_y = (n_radius * np.cos(1/164.79*theta))

fig, ax = plt.subplots(figsize=(5, 5))
ax = plt.axes(xlim=(-15, 15), ylim=(-15, 15))
mercury, = ax.plot([],[],'r.', markersize = 10)
venus, = ax.plot([],[], 'b.', markersize=10)
earth, = ax.plot([], [], 'g.', markersize=15)
moon, = ax.plot([], [], 'w.', markersize=5)
mars, = ax.plot([], [], 'r.', markersize=12)
jupiter, = ax.plot([], [], '.', markersize=17,color="maroon")
saturn, = ax.plot([], [], '.', markersize=18,color="peru")
uranus, = ax.plot([], [], '.', markersize=19,color="lightcyan")
netpune, = ax.plot([], [], '.', markersize=17,color="royalblue")
ax.plot(0, 0, '.', markersize=20, color="yellow")
plt.grid(True, lw=0.3)
ax.plot(mercury_x, mercury_y, 'r-')
ax.plot(e_x, e_y, 'g-')
ax.plot(v_x, v_y, 'b-')
ax.plot(mars_x,mars_y,'r-')
ax.plot(j_x,j_y,'-',color="maroon")
ax.plot(s_x,s_y,'-',color="peru")
ax.plot(u_x,u_y,'-',color="lightcyan")
ax.plot(n_x,n_y,'-',color="royalblue")
def animate(i):
        mercury.set_data(mercury_x[i],mercury_y[i])
        earth.set_data(e_x[i], e_y[i])
        moon.set_data(moon_x[i], moon_y[i])
        venus.set_data(v_x[i], v_y[i])
        mars.set_data(mars_x[i],mars_y[i])
        jupiter.set_data(j_x[i],j_y[i])
        saturn.set_data(s_x[i],s_y[i])
        uranus.set_data(u_x[i],u_y[i])
        netpune.set_data(n_x[i],n_y[i])
        return mercury,earth,moon,venus,mars,jupiter,saturn,uranus,netpune
anim = FuncAnimation(fig, animate, frames=1000, interval=5, repeat=False)
anim.save('cirlce_ani.gif', writer='pillow')
plt.show()