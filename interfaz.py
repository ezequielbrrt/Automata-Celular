#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Moduló de la interfaz gráfica que manda a llamar a los demás
archivos  
"""

from Tkinter import *
import tkMessageBox
import subprocess

def simularAutomata():
	if var.get() == 1 or var.get() == 2:
		poblacion.configure(state='normal')
		atractor.configure(state='normal')
		reinicio.configure(state='normal')
		simulacion.configure(state='disabled')
		datoPoblacion = variable.get()
		datoDensidad = open("DatoDensidad.txt","w")
		datoDensidad.write(str(datoPoblacion)+","
			+str(var.get())+","
			+str(variableTiempo.get())+","
			+(variableSimulacion.get())+","
			+v.get()+","
			+str(varAtractor.get()))
		datoDensidad.close()
		programaAutomata = subprocess.Popen([sys.executable, 'automata.py'])
	else:
		tkMessageBox.showerror("Error", "Selecciona una opción \n de automata")
		
def graficarPoblacion():
	poblacion.configure(state='disabled')
	programa = subprocess.Popen([sys.executable, 'grafica.py'])
	 
def graficarAtractor():
	atractor.configure(state='disabled')
	programa = subprocess.Popen([sys.executable, 'graficaAtractor.py'])

def reiniciar():
	poblacion.configure(state='disabled')
	atractor.configure(state='disabled')
	reinicio.configure(state='disabled')
	simulacion.configure(state='normal')
	tkMessageBox.showwarning("Advertencia", "Cerrar ventanas antes de simular otro automata")


root = Tk()
variable = StringVar(root)
variableTiempo = StringVar(root)
variableSimulacion = StringVar(root)
var  = IntVar()
v = StringVar()
varAtractor = IntVar()
#Opciones de las densidades de poblacion
opciones = [
	   "5%",
	   "10%",
	   "25%",
	   "50%",
	   "70%",
	   "80%",
	   "95%"
]
opcionesTiempo = [
	"0.1",
	"0.5",
	"1",
	"2"
]
opcionesSimulacion = [
	"Indefinido",
	"2",
	"5",
	"10"
]

#Boton de Reinicio
reinicio = Button(root, text="Reiniciar", command=reiniciar,state='disabled')
reinicio.grid(row=0,column=2)

#Radiobutton para la seleccion del tipo de automata
Label(root, text="Automata Celular").grid(row=0,column=1)
Radiobutton(root, text="Juego de la Vida", var=var, value=1 ).grid(row=1,column=0)
Radiobutton(root, text="Regla de Difusion", var=var, value=2).grid(row=2,column=0)

#Menu de opciones para las densidades de poblacion
Label(root,text="Niveles de densidad de Poblacion.").grid(row=3,column=1)
variable.set(opciones[3]) 
w = apply(OptionMenu, (root, variable) + tuple(opciones)).grid(row=4,column=1)

#opciones de Atractor
Label(root, text="Analisís de Atractor:").grid(row=6,column=0)
Radiobutton(root, text="3x3", var=varAtractor, value=1 ).grid(row=7,column=0)
Radiobutton(root, text="4x4", var=varAtractor, value=2 ).grid(row=8,column=0)

#tamaño del cuadrado del automata
Label(root,text="Tamaño de la simulación:").grid(row=5,column=1)
E1 = Entry(root,textvariable=v).grid(row=6,column=1)
v.set("50")
Label(root,text=v.get()+" x "+v.get()+" Cuadros").grid(row=6,column=2)

#Tiempo de rapidez de la simulación
Label(root,text="Rapidéz de Simulación").grid(row=7,column=1)
variableTiempo.set(opcionesTiempo[2]) 
w = apply(OptionMenu, (root, variableTiempo) + tuple(opcionesTiempo)).grid(row=8,column=1)
Label(root,text="Segundos").grid(row=8,column=2)

#Número de simulaciones
Label(root,text="Número de Simuaciones").grid(row=9,column=1)
variableSimulacion.set(opcionesSimulacion[2]) 
w = apply(OptionMenu, (root, variableSimulacion) + tuple(opcionesSimulacion)).grid(row=10,column=1)
Label(root,text="Simulaciones").grid(row=10,column=2)

#Botones para simular y graficar
poblacion = Button(root, text="Graficar Población", command=graficarPoblacion,state='disabled',relief=GROOVE)
simulacion = Button(root, text="Simular Automata", command=simularAutomata)
atractor = Button(root, text="Graficar Atractor", command=graficarAtractor,state='disabled')

poblacion.grid(row=11,column=0)
simulacion.grid(row=11,column=1)
atractor.grid(row=11,column=2)
mainloop()