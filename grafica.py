#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Modulo para graficar densidades de poblacion 
"""

import matplotlib.pyplot as plt
import matplotlib.animation as animation
import time
import random

fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)

def animate(update):
    pullData = open("DatosPoblacion.txt","r").read()
    dataArray = pullData.split('\n')
    xar = []
    yar = []
    for eachLine in dataArray:
        if len(eachLine)>1:
            x,y = eachLine.split(',')
            xar.append(int(x))
            yar.append(int(y))
    ax1.clear()
    ax1.bar(xar,yar, facecolor='#9999ff',label="Poblacion")
    plt.title("Poblacion")
    plt.xlabel("Tiempo Transcurrido")
    plt.ylabel("Numero de Celulas")
    plt.grid(True)

ani = animation.FuncAnimation(fig , animate, interval=1000)
plt.show()

