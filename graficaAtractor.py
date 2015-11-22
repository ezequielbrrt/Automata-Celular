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

#obtención de datos de Densidades
dataD = open("DatoDensidad.txt","r").read()
datosDensidad = dataD.split(',')

#obtencion de datos de tiempo
tiempo = open("Tiempo.txt","r").read()
tmp = tiempo.split('\n')


#Creacion de constante para el numero de elementos en el array
N = int(datosDensidad[4])
constante = N * N
valores = array(datosAtractor) 

aux = valores[i:constante]
aux2 = valores[constante:constante*2]
aux3 = valores[constante*2:constante*3]
aux4 = valores[constante*3:constante*4]
aux5 = valores[constante*4:constante*5]
aux6 = valores[constante*5:constante*6]
aux7 = valores[constante*6:constante*7]
aux8 = valores[constante*7:constante*8]
aux9 = valores[constante*8:constante*9]
aux10 = valores[constante*9:constante*10]

valoresID = []
especial = 0

for x in xrange(0,100):
    if aux[x] == aux2[x] :
        if aux2[x] != 0:
            print "Encontre recursion en el paso 1" + "id " + str(x+1)
    if aux2[x] == aux3[x] :
        if aux2[x] != 0:
            print "Encontre recursion en el paso 2" + "id " + str(x+1)
    if aux3[x] == aux4[x] :
        if aux2[x] != 0:
            print "Encontre recursion en el paso 3" + "id " + str(x+1)
            valoresID.append(str(x+1))
    if aux4[x] == aux5[x] :
        if aux2[x] != 0:
            print "Encontre recursion en el paso 4" + "id " + str(x+1)
            valoresID.append(str(x+1))
    if aux5[x] == aux6[x] :
        if aux2[x] != 0:
            print "Encontre recursion en el paso 5" + "id " + str(x+1)
            valoresID.append(str(x+1))
    if aux6[x] == aux7[x] :
        if aux2[x] != 0:
            print "Encontre recursion en el paso 6" + "id " + str(x+1)
            valoresID.append(str(x+1))
    if aux7[x] == aux8[x] :
        if aux2[x] != 0:
            print "Encontre recursion en el paso 7" + "id " + str(x+1)
            valoresID.append(str(x+1))
    if aux8[x] == aux9[x] :
        if aux2[x] != 0:
            print "Encontre recursion en el paso 8" + "id " + str(x+1)
            valoresID.append(str(x+1))
    if aux9[x] == aux10[x] :
        if aux2[x] != 0:
            print "Encontre recursion en el paso 9" + "id " + str(x+1)
            valoresID.append(str(x+1))

print valoresID
for i in valoresID:
    print i

fila1 = [aux[3]+","+aux2[3]+","+aux3[3]+","+aux4[3]+","+aux5[3]+","
+aux6[3]+","+aux7[3]+","+aux8[3]+","+aux9[3]+","+aux10[3]]

print 
print fila1

