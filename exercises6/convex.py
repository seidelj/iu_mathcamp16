import numpy as np
import matplotlib.pyplot as plt

def convex(x,y):
    xlist = []
    ylist = []
    for lam in np.arange(0,1,.001):
        xlist.append(x * float(lam))
        ylist.append(y * ( float(1)-lam))

    return ylist, xlist

coords = convex(100,100)
plt.plot(coords[0], coords[1])

plt.show()
