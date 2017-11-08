import matplotlib.pyplot as plt
import numpy as np

class BasicLayer():
    def __init__(self,initSize=10,initColor='black',xlim=[0,100],ylim=[0,62.5]):
        self.fig=plt.figure(figsize=(initSize,initSize),facecolor=initColor)
        self.ax=self.fig.add_axes([0,0,1,1],frameon=False)
        self.ax.set_xlim(xlim)
        self.ax.set_ylim(ylim)
        self.ax.set_xticks([])
        self.ax.set_yticks([])
        self.time_text=self.ax.text(0,0.85,'',transform=self.ax.transAxes,color='orange')
    def getLayer(self):
        return self.fig
    def gerScatLayer(self):
        return self.ax

class RoadPlot():
    def __init__(self,rX,rY,roadbox,plotLayer):
        self.rX=rX;
        self.rY=62.5*rY/100.0

        self.road=roadbox[0]
        self.width=1+self.road.get_road_lanes()*2
        self.roadbox=roadbox
        self.plotLayer=plotLayer
        self.scat=self.plotLayer.scatter([0],[0],s=1)

        
