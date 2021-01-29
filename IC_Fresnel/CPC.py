import math
import matplotlib.pyplot as plt
import numpy as np

def espelhar_graf(xp,yp):
    dx = abs(xp)
    xp2 = abs(xp_list[0]) + dx
    xp_list_espelhada.append(xp2)
    yp_list_espelhada.append(yp)

alpha_list = []
xp_list = []
xp_list_espelhada = []
yp_list = []
yp_list_espelhada = []

rt = 0.035
rg = 0.0625
thetaa = np.deg2rad(50)
#thetaa = 50*math.pi/180
n1 = abs(pow((rg/rt), 2)-1)
n2 = rt/rg
beta = math.sqrt(n1) - math.acos(n2)
thetamax = (math.atan(-104/-215)) + np.deg2rad(180)

# for AB

thetao = math.acos(rt/rg)
while True:
    alpha0 = rt*(thetao + beta)
    print(alpha0)
    xp = alpha0*math.cos(thetao) - rt*math.sin(thetao)
    xp_list.append(xp)
    yp = alpha0*math.sin(thetao) + rt*math.cos(thetao)
    yp_list.append(yp)
    thetao += 0.01
    if thetao >= (np.deg2rad(90) + thetaa):
        xp_list.pop()
        yp_list.pop()
        break
    espelhar_graf(xp,yp)

#For BC

thetao = (np.deg2rad(90) + thetaa)
while True:
    alpha0 = rt*(thetao + thetaa + (math.pi/2) + (2*beta) - math.cos(thetao - thetaa)) / (1 + math.sin(thetao - thetaa))
    print(alpha0)
    xp = alpha0 * math.cos(thetao) - rt * math.sin(thetao)
    xp_list.append(xp)
    yp = alpha0 * math.sin(thetao) + rt * math.cos(thetao)
    yp_list.append(yp)
    thetao += 0.01
    if thetao >= (thetamax):
        xp_list.pop()
        yp_list.pop()
        break
    espelhar_graf(xp,yp)

cx = []  # Circunferência do envelope de vidro.
cy = []
omega = np.deg2rad(0)
while True:
    x = rg*math.cos(omega)
    cx.append(x)
    y = rg*math.sin(omega) - 0.02
    cy.append(y)
    omega += 0.01
    if omega >= np.deg2rad(360):
        break

abx = []  # Circunferência do tubo evacuado.
aby = []
omega = np.deg2rad(0)
while True:
    x = rt*math.cos(omega)
    abx.append(x)
    y = rt*math.sin(omega) - 0.02
    aby.append(y)
    omega += 0.01
    if omega >= np.deg2rad(360):
        break

plt.plot(xp_list,yp_list)
plt.plot(xp_list_espelhada,yp_list_espelhada,color = 'r')
plt.plot(cx,cy)
plt.plot(abx,aby)
plt.show()

