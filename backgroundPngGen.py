import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import planets
from datetime import datetime, timedelta

def get_angle(x0, y0, x1, y1):
    ''' Calculate the angle from horizontal, counterclockwise '''
    angle = np.rad2deg(np.arctan2(y1-y0, x1-x0))
    return angle

def hypotenuse(x0, y0, x1, y1):
    ''' Returns the length of the straight line vector between two points '''
    hyp = np.hypot(x1-x0, y1-y0)
    return hyp

def get_r_theta(xs, ys):
    ''' Convert x and y coordinates to r-theta plots '''
    rs = [hypotenuse(0, 0, x, y) for x, y in zip(xs, ys)]
    rs = [np.log10(r) - min10 for r in rs]
    theta = [get_angle(0, 0, x, y) for x, y in zip(xs, ys)]
    theta = [np.radians(x) for x in theta]
    return rs, theta

def get_size(size):
    ''' Convert object diameter into Matplotlib scatter point size '''
    size = np.log10(size)
    # Matplotlib scatter size s = size in points^2, or the area
    size = size**2 # Convert to Matplotlib so diameter is new scaled length
    return(size)

if __name__ == '__main__':
    fig = plt.figure(figsize=(10,10))
    ax = fig.add_subplot(1,1,1, projection="polar")

    min10 = np.log10(2.7e7)
    max10 = np.log10(1.496e+10)
    rs = np.arange(0, 1e11, 1e9)
    rs = [np.log10(max(r, 1e-20)) - min10 for r in rs]
    for t in np.arange(0, 360, 90):
        theta = [np.radians(t)]*len(rs)
        ax.scatter(theta, rs, color='#ffffff', marker=(2, 0, t%180),  
                        lw=0.5, alpha=1, s=20)
        ax.plot([np.radians(t)]*2, [0, max(rs)], color='#ffffff', lw=0.5, alpha=1)

    for body in planets.solar_system:
        xlist = []
        ylist = []
        for i in range(100,100000):
            resList = body.orbit.get_pos_at_date(datetime.now() + timedelta(i))
            xlist.append(resList[0] * 1.496e+8)
            ylist.append(resList[1] * 1.496e+8)

        rs, theta = get_r_theta(xlist, ylist)
        ax.plot(theta, rs, color=body.color, lw=1.5, alpha=0.5, zorder = 10)
        
    ax.set_facecolor("#10112d")
    l = np.arange(np.floor(min10), max10)
    ax.set_rticks(l - min10) 
    ax.set_yticklabels([])
    ax.set_rlim(0, max10 - min10)

    plt.tight_layout()
    plt.subplots_adjust(top=1, bottom=0, right=1, left=0, hspace=0, wspace=0)
    plt.margins(0,0)
    plt.gca().xaxis.set_major_locator(matplotlib.pyplot.NullLocator())
    plt.gca().yaxis.set_major_locator(matplotlib.pyplot.NullLocator())

    plt.show()
    plt.clf()
