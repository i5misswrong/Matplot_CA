import numpy as np
import matplotlib.pyplot as plt

fig1 = plt.figure()


ax1 = fig1.add_subplot(111)


ax1.plot(4, 'o')


# In the latest release, it is no longer necessary to do anything
# special to share axes across figures:

# ax1.sharex_foreign(ax2)
# ax2.sharex_foreign(ax1)

# ax1.sharey_foreign(ax2)
# ax2.sharey_foreign(ax1)

plt.show()