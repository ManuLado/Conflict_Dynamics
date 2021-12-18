#!/usr/bin/python
# -*- coding: utf-8 -*-
from tkinter import Canvas, Tk
import time
import numpy as np
import math
WIDTH = 500
HEIGHT = 500
FOOD_SIZE = 1

class Food:

	all_food = {}

	def __init__(self, canvas):
		(x1, y1, x2, y2) = self.get_random_coordinates()
		self.canvas = canvas

		self.shape = self.canvas.create_oval(x1, y1, x2, y2, fill='#77ff00',width=0)
		self.food = np.random.randint(100, 1001)

		Food.all_food[self.shape] = self

	def get_random_coordinates(self):
		x1 = np.random.randint(0, WIDTH/2 - FOOD_SIZE)+WIDTH/4
		y1 = np.random.randint(0, HEIGHT/2 - FOOD_SIZE)+HEIGHT/4
		x2 = x1 + FOOD_SIZE
		y2 = y1 + FOOD_SIZE

		return (x1, y1, x2, y2)