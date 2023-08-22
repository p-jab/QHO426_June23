import matplotlib.animation as a
import matplotlib.pyplot as plt
import random

fig, ax = plt.subplots(1,1)

def animate(f):
    ax.cla()
    ax.set_xlim(0,10)
    ax.set_ylim(0,10)
    colours = ["r", "b", "g", "y"]
    colour = colours[random.randint(0,3)]
    ax.plot(f, f, colour+"o") # y=x

def run():
    karen = a.FuncAnimation(fig, animate, frames = 10, interval=500)
    plt.show()



run()