import numpy as np
from matplotlib import pyplot as plt
from matplotlib import animation

fig = plt.figure()
data = np.random.random((5, 5))
# data=[[1,2,1],[3,4,5]]
# print(data)
im = plt.imshow(data, cmap='gray')

# animation function.  This is called sequentially
def animate(i):
    data = np.random.random((5,5))
    im.set_array(data)
    print(data)
    return [im]

anim = animation.FuncAnimation(fig, animate, frames=200, interval=1000, blit=True)
plt.show()
