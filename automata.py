#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Automata Ceular 
Juego de la Vida y Regla de Difusión
Sistemas Complejos
Barreto Aviles Ezequiel Adrian
"""

import numpy as np
import matplotlib.pyplot as plt 
import matplotlib.animation as animation
import time
import Tkinter
import tkMessageBox
import os


#obtención de datos de la interfaz gráfica
pullData = open("DatoDensidad.txt","r").read()
dataArray = pullData.split(',')

#calulo de los porcentajes
porcentajeNuevo = ""
porcentaje = dataArray[0]
if porcentaje == '5%':
  porcentajeNuevo = porcentaje[0]
else:
  porcentajeNuevo = porcentaje[0:2]
unidad = 1.0
p = float(porcentajeNuevo)/100
pVivas = p
pMuertas = unidad - p

#valores para generar el random
viva = 1#int(dataArray[4]) * int(dataArray[4]) 
muerta = 0
vals = [1,0] #para generar numeros aleatorios entre 0 y 250
contadorTiempo = 0

#obtencion en milisegundos del tiempo 
tiempo = 10 * float(dataArray[2])

#valor del lado del cuadrado
N = int(dataArray[4]) 

#tipo de analizis del atractor
tipoAtractor = int(dataArray[5])

#Borra los datos en el archivo para volver a empezar de cero
restablecerDatos = open("DatosPoblacion.txt", "w")
restablecerDatos.write("")
restablecerDatos.close()

#Borra los datos en el archivo tiempo.txt para volver a empezar de cero
restablecerDatos = open("Tiempo.txt", "w")
restablecerDatos.write("")
restablecerDatos.close()

#Borra los datos en el archivo DatosAtractor
restablecerDatos2 = open("DatosAtractor.txt", "w")
restablecerDatos2.write("")
restablecerDatos2.close()

#poblacion random usando numpy 
#primer argumento es un array, el segundo es es el tamaño del array de salida
#la p es una lista de posibilidades de cada elemento
grid = np.random.choice(vals, N*N, p=[pVivas,pMuertas]).reshape(N, N)

#funcion para la graficacion de celulas
def update(data):
  global grid
  global contadorTiempo
  contadorCelulas = 0 
  newGrid = grid.copy()
  for i in range(N):
    for j in range(N):           
      #Contador de celulas
      if grid[i, j] == viva:
        contadorCelulas += 1

      total = (grid[i, (j-1)%N] + grid[i, (j+1)%N] + grid[(i-1)%N, j] 
        + grid[(i+1)%N, j] + grid[(i-1)%N, (j-1)%N] 
        + grid[(i-1)%N, (j+1)%N] + grid[(i+1)%N, (j-1)%N] 
        + grid[(i+1)%N, (j+1)%N])

      if tipoAtractor == 1:  
        #analisis de tres por tres
        columna1 = str(grid[(i-1)%N,(j-1)%N]) + str(grid[i,(j-1)%N]) + str(grid[(i+1)%N,(j-1)%N])
        columna2 = str(grid[(i-1)%N,j]) + str(grid[i,j]) + str(grid[(i+1)%N,j])
        columna3 = str(grid[(i-1)%N,(j+1)%N]) + str(grid[i,(j+1)%N]) + str(grid[(i+1)%N,(j+1)%N]) 
        matriz3x3 = columna1 + columna2 + columna3
        matriz3x3 = int(matriz3x3,2)
        datosAnalisis = open("DatosAtractor.txt","a")
        datosAnalisis.write(str(matriz3x3)+'\n')
        datosAnalisis.close()

      if tipoAtractor == 2:  
        #analisis de 4 x 4
        columna1 = str(grid[(i-1)%N,(j-1)%N]) + str(grid[i,(j-1)%N]) + str(grid[(i+1)%N,(j-1)%N]) + str(grid[(i+2)%N,(j-1)%N])
        columna2 = str(grid[(i-1)%N,j]) + str(grid[i,j]) + str(grid[(i+1)%N,j]) + str(grid[(i+2)%N,j])
        columna3 = str(grid[(i-1)%N,(j+1)%N]) + str(grid[i,(j+1)%N]) + str(grid[(i+1)%N,(j+1)%N]) + str(grid[(i+2)%N,(j+1)%N])
        columna4 =str(grid[(i-1)%N,(j+2)%N]) + str(grid[i,(j+2)%N]) + str(grid[(i+1)%N,(j+2)%N]) + str(grid[(i+2)%N,(j+2)%N])
        matriz4x4 = columa1 + columna2 + columna3 + columna4 
        matriz4x4 = int(matriz4x4,2)
        datosAnalisis = open("DatosAtractor.txt","a")
        datosAnalisis.write(str(matriz4x4)+'\n')
        datosAnalisis.close()

      if int(dataArray[1]) == 1:  
        #Reglas del juego de la vida (2,3,3,3)
        if grid[i, j]  == viva:
          if (total < 2) or (total > 3):
            newGrid[i, j] = muerta
        else:
          if total == 3:
            newGrid[i, j] = viva
      
      if int(dataArray[1]) == 2:
        #Reglas de difusion R(7,7,2,2)
        if grid[i, j] == viva:
          if total != 7:
            newGrid[i, j] = muerta
        else:
          if total == 2:
            newGrid[i, j] = viva
            


  #Creacion de Archivo y escritura de la poblacion de celulas y tiempo
  arch = open("DatosPoblacion.txt", "a")
  arch.write(str(contadorTiempo)+","+str(contadorCelulas)+'\n')
  arch.close()

  tiempo = open("Tiempo.txt","a")
  tiempo.write(str(contadorTiempo)+'\n')
  tiempo.close()


  contadorTiempo += 1      
  #actulización de datos
  mat.set_data(newGrid)
  grid = newGrid

  #ifs para el número de simulaciones
  if dataArray[3] != 'Indefinido':
    if contadorTiempo == int(dataArray[3]) :
      raw_input("")

  return [mat]

#configurando la animacion
fig, ax = plt.subplots()
mat = ax.matshow(grid)
ani = animation.FuncAnimation(fig, update,interval=tiempo,save_count=10)
plt.show()
