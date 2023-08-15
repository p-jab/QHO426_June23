import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator

fig, axs = plt.subplots(3,2)
x = range(5, 10)
y = range(20, 40, 4)
axs[0, 0].plot(x,y, "ro-")
axs[0,0].set_xlim(0, 10)
axs[0,0].set_ylim(0,40)
axs[0,0].tick_params(which = "both", width = 2)
axs[0,0].tick_params(which = "major", length = 6, color = "g")
axs[0,0].tick_params(which = "minor", length = 4, color = "b")

axs[0,0].yaxis.set_minor_locator(MultipleLocator(5))
axs[0,0].yaxis.set_major_locator(MultipleLocator(10))
axs[0,0].xaxis.set_major_locator(MultipleLocator(2))
axs[0,0].xaxis.set_minor_locator(MultipleLocator(0.5))

axs[2,1].plot(y, x, "y^--")
axs[1,1].bar(x,y,color="g")

plt.tight_layout()
plt.show()