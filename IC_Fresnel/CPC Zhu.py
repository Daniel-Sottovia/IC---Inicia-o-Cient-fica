import math
import matplotlib.pyplot as plt
import numpy as np

def espelhar_graf(xp,yp):
    dx = -(xp)
    xp2 = (xp_list[0]) + dx
    xp_list_espelhada.append(xp2)
    zp_list_espelhada.append(zp)

xp_list = []
xp_list_espelhada = []
zp_list = []
zp_list_espelhada = []

raio = 0.035    # Radius of the absorber
g = 0.025       # Distance from the absorber to the CPC end
phi = np.deg2rad(63/2)
n1 = math.sqrt(2*raio*g + pow(g, 2))



# AB

thetao = math.acos(raio /(raio + g))
theta = thetao
while True:
    funI = math.sqrt(2*raio*g + pow(g, 2)) + raio*(theta - thetao)
    xp = raio*math.sin(theta) - funI*math.cos(theta)
    xp_list.append(xp)
    zp = theta*math.cos(theta) + funI*math.sin(theta)
    zp_list.append(zp)
    theta += 0.01
    if theta >= (np.deg2rad(90) + phi):
        xp_list.pop()
        zp_list.pop()
        break
    espelhar_graf(xp, zp)

# BC

thetao = math.acos(raio /(raio + g))
theta = np.deg2rad(90) + phi
while True:
    funI = (2*(math.sqrt(2*raio*g + pow(g,2)) - raio*thetao) + raio*(np.deg2rad(90) + phi + theta - math.cos(theta - phi))) / (1 + math.sin(theta - phi))
    xp = raio * math.sin(theta) - funI * math.cos(theta)
    print(xp)
    xp_list.append(xp)
    zp = theta * math.cos(theta) + funI * math.sin(theta)
    print(zp)
    zp_list.append(zp)
    theta += 0.01
    if theta >= np.deg2rad(150):
        xp_list.pop()
        zp_list.pop()
        break
    espelhar_graf(xp, zp)

plt.plot(xp_list,zp_list)
plt.plot(xp_list_espelhada,zp_list_espelhada,color = 'r')
plt.show()

