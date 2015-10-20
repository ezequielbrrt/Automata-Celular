#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Modulo para graficar atractores
"""
from numpy import *
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import time
import random

fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)
i = 0

#obtencion de datos del atractor
dataA = open("DatosAtractor.txt","r").read()
datosAtractor = dataA.split('\n')
datosAtractor.remove("")

#obtención de datos de la interfaz gráfica
dataD = open("DatoDensidad.txt","r").read()
datosDensidad = dataD.split(',')

#obtencion de datos de tiempo
tiempo = open("Tiempo.txt","r").read()
tmp = tiempo.split('\n')


#Creacion de constante para el numero de elementos en el array
N = int(datosDensidad[4])
constante = N * N
valores = array(datosAtractor) 

#numero de simulaciones
if datosDensidad[3] == 'Indefinido':
    #para dos simulaicones
    aux = valores[i:constante]
    aux2 = valores[constante:constante*2]
    #para cinco simulaciones
    aux3 = valores[constante*2:constante*3]
    aux4 = valores[constante*3:constante*4]
    aux5 = valores[constante*4:constante*5]
    #para 10 simulaciones
    aux6 = valores[constante*5:constante*6]
    aux7 = valores[constante*6:constante*7]
    aux8 = valores[constante*7:constante*8]
    aux9 = valores[constante*8:constante*9]
    aux10 = valores[constante*9:constante*10]
    aux11 = valores[constante*10:constante*11]

    paso1 = aux == aux2
    paso2 = aux2 == aux3
    paso3 = aux3 == aux4
    paso4 = aux4 == aux5
    paso5 = aux5 == aux6
    paso6 = aux6 == aux7
    paso7 = aux7 == aux8
    paso8 = aux8 == aux9
    paso9 = aux9 == aux10
    paso10 = aux10 == aux11

    print paso9
    print paso10
    def animate(update):
        xar = tmp
        yar = aux11
        ax1.clear()
        ax1.bar(xar,yar, facecolor='#9999ff',label="Poblacion")
        plt.title("Poblacion")
        plt.xlabel("Tiempo Transcurrido")
        plt.ylabel("Atractores")
        plt.grid(True)

    #ani = animation.FuncAnimation(fig , animate, interval=1000)
    #plt.show()

