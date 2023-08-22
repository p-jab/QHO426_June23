import matplotlib.pyplot as plt
import matplotlib.animation as a
import numpy as np

fig, ax = plt.subplots()

def animate(f):
    #ax.cla()
    ax.set_xlim(0,720)
    ax.set_ylim(-1,1)
    x_deg = np.arange(0, 720)
    x_rad = x_deg/180*np.pi
    y = np.sin(x_rad - f/20)
    ax.plot(x_deg, y, "o")

def run():
    larry = a.FuncAnimation(fig, animate, frames=720, interval=100)
    plt.show()
run()