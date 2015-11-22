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


i = 0

contador = 0

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

restablecerDatos = open("DatosGrafica.txt", "w")
restablecerDatos.write("")
restablecerDatos.close()



#Creacion de constante para el numero de elementos en el array
N = int(datosDensidad[4])
constante = N * N
valores = datosAtractor 

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


for x in xrange(1,100):
    if aux[x] == aux2[x] :
        pass#print "Encontre recursion en el paso 1" + "id " + str(x+1)
    if aux2[x] == aux3[x] :
        pass #print "Encontre recursion en el paso 2" + "id " + str(x+1)
    if aux3[x] == aux4[x] :
        valoresID.append(str(x))
    if aux4[x] == aux5[x] :
        valoresID.append(str(x))
    if aux5[x] == aux6[x] :
        valoresID.append(str(x))
    if aux6[x] == aux7[x] :
        valoresID.append(str(x))
    if aux7[x] == aux8[x] :
        valoresID.append(str(x))
    if aux8[x] == aux9[x] :
        valoresID.append(str(x))
    if aux9[x] == aux10[x] :
        valoresID.append(str(x))
print valoresID

fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)
for i in range(0,len(valoresID)-1):
    contadorCeros = 0
    fila1 = ""
    fila1 = (aux[int(valoresID[i])]+","+aux2[int(valoresID[i])]+","
        +aux3[int(valoresID[i])]+","+aux4[int(valoresID[i])]+","+aux5[int(valoresID[i])]
        +","+aux6[int(valoresID[i])]+","+aux7[int(valoresID[i])]+","+aux8[int(valoresID[i])]
        +","+aux9[int(valoresID[i])]+","+aux10[int(valoresID[i])])
    for i in fila1:
        if i == "0":
            contadorCeros += 1
    if contadorCeros > 1:
        pass
    else:
        datos = open("DatosGrafica.txt","a")
        datos.write(str(fila1)+'\n')
        datos.close()
 

def animate(update):
    global contador
    pullData = open("DatosGrafica.txt","r").read()
    dataArray = pullData.split('\n')
    dataArray.remove("")
    xar = [1,2,3,4,5,6,7,8,9,10]
    yar = []
        
    y = dataArray[contador].split(',')
    for i in y:
        yar.append(i)
    ax1.plot(xar,yar)
    plt.title("Atractores")
    plt.xlabel("Tiempo Transcurrido")
    plt.ylabel("Numero de Celulas")
    plt.grid(True)
    contador += 1

ani = animation.FuncAnimation(fig , animate, interval=10)
plt.show()



