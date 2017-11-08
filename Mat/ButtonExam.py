import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, Button, RadioButtons
plt.figure(figsize=(12,8))

# 绘制第一个图
plt.subplot(1, 1, 1)
plt.plot([0, 1], [0, 1])
# 绘制第二个图
# plt.subplot(2, 1, 2)
# plt.plot([0, 1], [0, 1])


resetax = plt.axes([0.8, 0.025, 0.1, 0.04])
button = Button(resetax, 'Reset',  hovercolor='0.5')
def reset(event):
    plt.close()
button.on_clicked(reset)
plt.show()