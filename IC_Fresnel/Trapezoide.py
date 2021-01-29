import math
import matplotlib.pyplot as plt
import numpy as np

xp_list = []
yp_list = []

rw = 0.1 # Secondary-aperture width
ha = 0.05 # Secondary-reflector height
thetatc = np.deg2rad(30) # Inclination of the side section of the secondary shape


x = -rw
while True:
    xp_list.append(x)
    y = x * math.tan(thetatc)
    yp_list.append(y)
    x += 0.01
    if x >= (-ha/math.tan(thetatc)):
        xp_list.pop()
        yp_list.pop()
        break

x = ( -ha / math.tan(thetatc))
while True:
    x += 0.01
    xp_list.append(x)
    yp_list.append(ha)
    if x >= (ha/math.tan(thetatc)):
        xp_list.pop()
        yp_list.pop()
        break

x = ha/math.tan(thetatc)
while True:
    xp_list.append(x)
    y = (rw - x) * math.tan(thetatc)
    yp_list.append(y)
    x += 0.01
    if x >= rw:
        xp_list.pop()
        yp_list.pop()
        break

plt.plot(xp_list,yp_list)
plt.show()