#!/usr/bin/python
# -*- coding: utf-8 -*-
from food import Food
from tkinter import Canvas, Tk
import time
import numpy as np
import random

WIDTH = 500
HEIGHT = 500
IND_SIZE = 5
START_GEN = 200
VIEW_RADIUS = 200

ANCHOPUERTA=30
BARRERA=50

numero_inicial=80
Nazules=numero_inicial
Nrojos=numero_inicial
t=0
tiempo=[]
red_array=[]
blue_array=[]
tension_array=[]
tension=0
asesinatos=0


asesinatos_array=[]
tension_place=[]
asesinatos_place=[]


blue_array.append(Nazules)
red_array.append(Nrojos)

comida_array=[]

enemy_coordinates=[]

class Individual:

	all_individuals = {}
	current_generation = 0

	def __init__(self, canvas,color,ymin,ymax,ID):
		self.flag = ID
		(x1, y1, x2, y2) = self.get_random_coordinates(ymin,ymax)
		self.canvas = canvas
		self.shape = self.canvas.create_oval(x1, y1, x2, y2, fill=color,width=0,tag=ID)

		self.xspeed = 1
		self.yspeed = 1

		self.on_course = False
		self.food_position_x = 0
		self.food_position_y = 0

		self.food = 0
		self.max_hunger = np.random.randint(500, 1001)

		self.randomly_change_direction(low=-1, high=1, chance=100)

		
		
		Individual.all_individuals[self.shape] = self



	def get_random_coordinates(self,ymin,ymax):

		x1 = np.random.randint(0, WIDTH - IND_SIZE)
		y1 = np.random.randint(ymin, ymax - IND_SIZE)
		x2 = x1 + IND_SIZE
		y2 = y1 + IND_SIZE

		return (x1, y1, x2, y2)

	def step(self):
		global t
		global tiempo
		global comida_array
		t+=1
		tiempo.append(t)
		tension_array.append(tension)
		asesinatos_array.append(asesinatos)


		blue_array.append(Nazules)
		red_array.append(Nrojos)

		comida_array.append(len(Food.all_food))

		if self.is_dead() or self.kill():

			return

		self.reached_border()
		self.canvas.move(self.shape, self.xspeed, self.yspeed)

		focus_group = self.decide_next_action()

		self.eat()
		if self.food == 0:
			self.randomly_change_direction(low=-1, high=1, chance=2)
			self.on_course = False
		
		self.reached_food()

		self.food += 1
		
		if not self.on_course:
			self.move_to(focus_group)
		
		if not self.on_course:
			self.randomly_change_direction(low=-1, high=1, chance=2)

	def reached_food(self):
		(x1, y1, x2, y2) = self.canvas.coords(self.shape)
		
		if x1 == self.food_position_x and y1 == self.food_position_y:
			self.randomly_change_direction(low=-1, high=1, chance=2)
			self.on_course = False
	
	def decide_next_action(self):
		if self.food > 200:	
			#return Food.all_food
			pass
		else:
			return None
	
	def move_to(self, group):
		if group == None:
			self.randomly_change_direction(low=-1, high=1, chance=2)
			self.on_course = False
			return

		(x1, y1, x2, y2) = self.canvas.coords(self.shape)

		x1 -= VIEW_RADIUS
		y1 -= VIEW_RADIUS
		x2 += VIEW_RADIUS
		y2 += VIEW_RADIUS

		currently_seeing = self.canvas.find_overlapping(x1, y1, x2, y2)
		currently_seeing = [obj for obj in currently_seeing if obj in group]

		if len(currently_seeing) == 0:
			self.randomly_change_direction(low=-1, high=1, chance=2)
			self.on_course = False
			return

		target = currently_seeing[0]

		targ_x1, targ_y1, targ_x2, targ_y2 = self.canvas.coords(target)
		
		self.xspeed = ((targ_x1 + targ_x2)/2 - x1)/100
		self.yspeed = ((targ_y1 + targ_y2)/2 - y1)/100

		self.food_position_x = (targ_x1 + targ_x2)/2 
		self.food_position_y = (targ_y1 + targ_y2)/2

		self.on_course = True

	def is_dead(self):
		if self.food >= self.max_hunger:
			self.canvas.delete(self.shape)
			try:
				del Individual.all_individuals[self.shape]
				#print(self.shape)
			except KeyError:
				pass
			self.contador('died')
		return self.shape not in Individual.all_individuals



	def reached_border(self):
		pos = self.canvas.coords(self.shape)

		if pos[3] >= HEIGHT or pos[1] <= 0:
			self.yspeed = -self.yspeed

		if pos[2] >= WIDTH or pos[0] <= 0:
			self.xspeed = -self.xspeed
		
		if (pos[3]==BARRERA+IND_SIZE or pos[3]==BARRERA-IND_SIZE) or (pos[3]==HEIGHT-(BARRERA+IND_SIZE) or pos[3]==HEIGHT-(BARRERA-IND_SIZE)):
			if pos[2] <=WIDTH/2-ANCHOPUERTA or pos[2] >=WIDTH/2+ANCHOPUERTA:
				self.yspeed = -self.yspeed


	def reached_noman_zone(self):
		
		pos = self.canvas.coords(self.shape)
		if (pos[3]>BARRERA+IND_SIZE) and (pos[3]<HEIGHT-(BARRERA+IND_SIZE)):
			r=random.randint(0,2)  #1/3 de probabilidad de morir
			if True:
				self.canvas.delete(self.shape)
				try:
					del Individual.all_individuals[self.shape]
					

				except KeyError:
					pass
				self.contador('died')

			return self.shape not in Individual.all_individuals
			print('died in nomans zone')



		

	def contador(self,status):
		
		global Nrojos
		global Nazules
		global red_array
		global blue_array

		if self.flag=='rojo':
			self.canvas.delete("redtext_tag")

			if status=='reproduced':
				Nrojos+=1
			if status=='died':
				Nrojos+=-1

			self.canvas.create_text(20,100,fill="red",font=("Purisa", 22),text=Nrojos,tag="redtext_tag")
			#red_array.append(Nrojos)

		if self.flag=='azul':
			self.canvas.delete("bluetext_tag")
			if status=='reproduced':
				Nazules+=1
			if status=='died':
				Nazules+=-1
			self.canvas.create_text(20,380,fill="blue",font=("Purisa", 22),text=Nazules,tag="bluetext_tag")

			#blue_array.append(Nazules)
		

	def eat(self):
		currently_overlapping = self.detect_resource_collision(Food.all_food)
		
		if len(currently_overlapping) == 0:
			return

		for food in currently_overlapping:
			self.canvas.delete(food)

			#se reproduce al comer

			se_reproduce = True#np.random.choice([True, False])
			if se_reproduce == True:

				if self.flag=='rojo':
					Individual(self.canvas,'#d54332',0, BARRERA,'rojo')
					self.contador('reproduced')
					

				if self.flag=='azul':
					Individual(self.canvas,'#1f7ed3', HEIGHT-BARRERA, HEIGHT,'azul')
					
					self.contador('reproduced')
					
			else:
				pass

			try:
				del Food.all_food[food]
			except KeyError:
				pass

		self.food = 0
		
	def kill(self):
		global tension_array
		global tension_place
		global asesinatos_place
		global asesinatos_array
		global tension
		global asesinatos

		currently_overlapping = self.detect_resource_collision(Individual.all_individuals)
		
		if len(currently_overlapping) == 0:
			return

		if self.flag=='rojo':
			self.enemy_flag='azul'

		if self.flag=='azul':
			self.enemy_flag='rojo'

		for enemy in currently_overlapping:
			#print(Individual.all_individuals[enemy].flag,self.flag)


			if Individual.all_individuals[enemy].flag != self.flag:
				print('encuentro==TENSION')
				tension += 1 
				tension_place.append(self.canvas.coords(self.shape))
		

				r=random.randint(0,1) #eleccion de matar o no
				if r==0:
					asesinatos+=1
					

					self.canvas.delete(enemy)
					try:
						del Individual.all_individuals[enemy]
					#print(self.shape)
					except KeyError:
						pass
					self.contador('died')
					print('----deleted:')
					asesinatos_place.append(self.canvas.coords(self.shape))
				return enemy not in Individual.all_individuals

				if r==1:
					pass
			else:
				#tension=0
				pass


	def detect_resource_collision(self, group):
		(x1, y1, x2, y2) = self.canvas.coords(self.shape)
		currently_overlapping = self.canvas.find_overlapping(x1, y1, x2, y2)

		currently_overlapping = [ind for ind in currently_overlapping if ind in group]

		return currently_overlapping

	def randomly_change_direction(self, low, high, chance):
		if np.random.randint(0, 101) > 100 - chance:
			self.xspeed = np.random.randint(low, high + 1)
		if np.random.randint(0, 101) > 100 - chance:	
			self.yspeed = np.random.randint(low, high + 1)