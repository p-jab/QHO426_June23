import matplotlib.pyplot as plt
import matplotlib.animation as a
import numpy as np

fig, ax = plt.subplots(1,1)

def animate(f):
    ax.set_xlim(0,720)
    ax.set_ylim(-1,1)
    x = np.arange(0, f)
    x_rad = x*np.pi/180
    y = np.sin(x_rad)
    ax.plot(x,y)

def run():
    margaret = a.FuncAnimation(fig, animate, frames=720, interval=10)
    plt.show()
run()