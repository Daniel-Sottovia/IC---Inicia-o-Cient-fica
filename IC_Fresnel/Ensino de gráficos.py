import math
import matplotlib.pyplot as plt
import numpy as np

xp_list = []
yp_list = []

raio = 1
theta = np.deg2rad(0)

while True:
    xp = raio*math.cos(theta)
    xp_list.append(xp)
    yp = raio*math.sin(theta)
    yp_list.append(yp)
    if theta >= np.deg2rad(360):
        break
    theta += 0.01

plt.plot(xp_list,yp_list)
plt.show()