#!/usr/bin/python
# -*- coding: utf-8 -*-
from tkinter import Canvas, Tk
import time
import numpy as np
from individual import Individual



from food import Food
import math

WIDTH = 500
HEIGHT = 500
FOOD_RATE = 1023
INDIVIDUAL_QNT = 120

ANCHOPUERTA=30
BARRERA=50
B_FASE=0
numero_inicial=80

def create_food(canvas):
	quantity = math.ceil((np.random.randint(30, 101)/100) * INDIVIDUAL_QNT)
	for i in range(quantity):
		Food(canvas)

master = Tk()
canvas = Canvas(master, width=WIDTH, height=HEIGHT,background= "#1f1a0b")

#canvas.create_text(100,10,fill="red",text="number")

canvas.create_line(0, BARRERA+B_FASE, WIDTH/2-ANCHOPUERTA, BARRERA+B_FASE,fill='white',width=3)
canvas.create_line(WIDTH/2+ANCHOPUERTA, BARRERA+B_FASE, WIDTH, BARRERA+B_FASE,fill='white',width=3)

canvas.create_line(0, HEIGHT-BARRERA, WIDTH/2-ANCHOPUERTA, HEIGHT-BARRERA,fill='white',width=3)
canvas.create_line(WIDTH/2+ANCHOPUERTA, HEIGHT-BARRERA, WIDTH, HEIGHT-BARRERA,fill='white',width=3)

master.title('Simulation')
canvas.pack()

# Creating individuals


#red_array=[]
#blue_array=[]


Nazules=numero_inicial
Nrojos=numero_inicial

#blue_array.append(Nazules)
#red_array.append(Nrojos)


for i in range(numero_inicial):
	Individual(canvas,'#d54332',0, BARRERA+B_FASE,'rojo')
	Individual(canvas,'#1f7ed3', HEIGHT-BARRERA, HEIGHT+B_FASE,'azul')

canvas.create_text(20,100,fill="red",font=("Purisa", 22),text=Nrojos,tag="redtext_tag")
canvas.create_text(20,380,fill="blue",font=("Purisa", 22),text=Nazules,tag="bluetext_tag")
# Creating food
create_food(canvas)
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D

# Main loop
while True:
	Individual.current_generation += 1
	

	for ind in list(Individual.all_individuals.values()):
		ind.step()
		
		
	if Individual.current_generation % FOOD_RATE == 0 and len(Food.all_food) < 1.5 * INDIVIDUAL_QNT:
		#create_food(canvas)
		pass #activar si el recurso es renovable


	master.update()
	time.sleep(0.005)


	if len(Food.all_food) == 0 or len(Individual.all_individuals) ==0  or Individual.current_generation==5000:
		print('End of simulation')
		from individual import tension_array
		from individual import asesinatos_array
		from individual import tension_place
		from individual import asesinatos_place
		from individual import tiempo
		from individual import blue_array
		from individual import red_array
		from individual import comida_array

		fig, axs = plt.subplots(2)
		axs[1].plot(tiempo,tension_array,label='tension')
		axs[1].plot(tiempo,asesinatos_array,label='asesinatos')
		axs[1].legend()
		axs[1].set_ylabel('Casos cumulativos')

		axs[0].plot(tiempo,blue_array[1::], color='blue',label='Bando azul')
		axs[0].plot(tiempo,comida_array, color='lawngreen',label='Recursos')
		axs[0].plot(tiempo,red_array[1::], color='red',label='Bando rojo')
		axs[0].set_ylabel("Poblacion")
		axs[0].legend()

		plt.xlabel('Tiempo de simulacion')
		fig.suptitle('Barrera = {}+{}'.format(BARRERA,B_FASE))
		plt.savefig('PopRun1_Barrera_ {}+{}'.format(BARRERA,B_FASE))
		plt.show()


		plt.scatter(0,0,color='white')
		plt.scatter(WIDTH,HEIGHT,color='white')

		


		plt.plot([0,WIDTH/2-ANCHOPUERTA], [BARRERA+B_FASE,BARRERA+B_FASE],'--',color='Black')
		plt.plot([WIDTH/2+ANCHOPUERTA,WIDTH], [BARRERA+B_FASE,BARRERA+B_FASE],'--',color='Black')

		plt.plot([0,WIDTH/2-ANCHOPUERTA], [HEIGHT-BARRERA,HEIGHT-BARRERA],'--',color='Black')
		plt.plot([WIDTH/2+ANCHOPUERTA,WIDTH], [HEIGHT-BARRERA,HEIGHT-BARRERA],'--',color='Black')

		legend_elements = [Line2D([0], [0], linestyle='None',marker='o', color='Orange',alpha=0.5, label='Tension') , Line2D([0], [0], linestyle='None', marker='x',color='red', label='Asesinatos')]
		plt.legend(handles=legend_elements)

		for data_tension in tension_place:
		#print(data)
			x,y,w,z = data_tension
			plt.scatter(x,y,color='Orange',alpha=0.5)

		for data_asesinatos in asesinatos_place:
			x,y,w,z = data_asesinatos
			plt.scatter(x,y,marker='x',color='red',alpha=1)

		plt.title("Puntos de tension y asesinatos")

		plt.savefig('SpotRun1_Barrera_ {}+{}'.format(BARRERA,B_FASE))
		plt.show()

		break

master.mainloop()