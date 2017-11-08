import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from matplotlib.pyplot import imsave
import numpy as np
import random

principle='0110110'

class group:
    def __init__(self,length):
        self.cells=[]
        for i in range(length):
            self.cells.append(random.choice((1,0)))
    def __repr__(self):
        return  str(self.cells)
    def b_to_d(self,list_3):
        return list_3[2]+2*list_3[1]+4*list_3[0]
    def set_cell(self,i,val):
        self.cells[i]=val
    def next_gen(self,principle):
        new_grouop=group(len(self.cells))
        state=[None,None,None]
        for i in range(len(self.cells)):
            state[0]=int(self.cells[i-1])
            state[1]=int(self.cells[i])
            if i==len(self.cells)-1:
                state[2]=int(self.cells[0])
            else:
                state[2]=int(self.cells[i+1])
            new_grouop.set_cell(i,20)

        return new_grouop

img=[]
A=group(256)
for i in range(256):
    img_item=[]
    for jtem in A.cells:
        if jtem==0:
            jtem=1
        else:
            jtem=0
        img_item.append([jtem,jtem,jtem])
    img.append(img_item)
    B=A.next_gen(principle)
    A=B
img_item=[]
for jtem in A.cells:
    if jtem==0:
        jtem=1
    else:
        jtem=0
    img_item.append([jtem,jtem,jtem])
img.append(img_item)
img=np.array(img,dtype="float32")
imgplot=plt.imshow(img)
plt.show()
