import math
import matplotlib.pyplot as plt

xp_list = []
yp_list = []
zp_list = []
cx = 1.1
cy = 0
x = 0
y = 0

while True:
    z = 0.5 * (cx * math.pow(x, 2) + cy * math.pow(y, 2))
    zp_list.append(z)
    xp_list.append(x)
    xp =+0.1
    yp =+0.1
    if x or y == 1:
        zp_list.pop()
        xp_list.pop()
        break

plt.plot(xp_list,zp_list)
plt.show()
