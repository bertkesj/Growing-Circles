#!/usr/bin/python


import matplotlib.animation as animation
from scipy.spatial import distance
import matplotlib.pyplot as plt
import numpy as np

def xy(r,phi,c):
  return r*np.cos(phi) + c[0], r*np.sin(phi) + c[1]


plt.show()



n_circ = 1
tick = 0
def update(curr):

    global tick
    global n_circ
    ax1.clear()
    phis=np.arange(0,2*np.pi,0.01)
    r =1
    c = (0,0)
    ax1.plot( *xy(r,phis,c), c='r',ls='-')
    

    rsub1 = distance.euclidean(xy(r,0*2*np.pi/n_circ,c), xy(r,1*2*np.pi/n_circ,c))/2
    rsub = tick*rsub1/100
    if curr % 100 == 0:
        for i in range(n_circ):
            c1 = xy(r,i*2*np.pi/n_circ,c)
            ax1.plot( *xy(rsub,phis,c1), c='y',ls='-')
        ax1.text(-1.5,1.5, "N = %s" % (n_circ))
        ax1.text(-1.5,1.4, "radius = %.2f" % (rsub))
        ax1.text(-1.5,1.3, "pi/arcsin(radius) = %.2f" % (np.pi/np.arcsin(rsub)))
        ax1.axis([-1.25,1.25,-1.25,1.25])
        plt.pause(3)
        n_circ = n_circ + 1
        tick = 0
    
    else:    
        for i in range(n_circ):
            c1 = xy(r,i*2*np.pi/n_circ,c)
            ax1.plot( *xy(rsub,phis,c1), c='b',ls='-')
        ax1.text(-1.5,1.5, "N = %d" % (n_circ))
        ax1.text(-1.5,1.4, "radius = %.2f" % (rsub))
        ax1.text(-1.5,1.3, "pi/arcsin(radius) = %.2f" % (np.pi/np.arcsin(rsub)))
        ax1.axis([-1.25,1.25,-1.25,1.25])
        tick = tick + 1
    
fig = plt.figure()
ax1 = fig.add_subplot(1,1,1,aspect="equal")
a = animation.FuncAnimation(fig, update, interval=50)
plt.show()