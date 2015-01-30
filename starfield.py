#By Luke Taylor
#Uses Python 2.7
#A test of embedding pygame windows in tkinter frames
#A 3D Starfield program. Tested on Mac OS X Yosemite, Windows 7, and Raspbian (Linux)
#Tests were completely successful on Windows and Linux.
#On mac, the pygame window appeared separately from the tkinter window, leaving the tkinter frame blank. 

import pygame
import math
import sys
import platform
import os
from random import randrange
from Tkinter import *


class Simulation:
	def __init__(self, num_stars, max_depth):
		global var
		var = 0.19
		
		global tk
		tk = Tk()
		
		#creates embed frame for pygame window
		embed = Frame(tk, width = 640, height = 480)
		embed.grid(columnspan = (640), rowspan = 480)
		embed.grid(row=0, column=0)
		
		#Creates frame for slider
		buttonwin = Frame(tk, width = 75, height = 500)
		buttonwin.grid(row=1, column=0)
		
		#Tells pygame's SDL window which window ID to use  
		os.environ['SDL_WINDOWID'] = str(embed.winfo_id())
		if platform.system == "Windows":
		    os.environ['SDL_VIDEODRIVER'] = 'windib'
		
		#Creates the slider
		global slider
		slider = Scale(buttonwin, from_=0, to=1, length=640, resolution = .01, label="Speed", orient=HORIZONTAL)
		slider.pack()
		slider.set(0.18)
		
		#Set up pygame's window (inside the tkinter frame)
		pygame.init()
		self.screen = pygame.display.set_mode((640, 480))
		pygame.display.set_caption("3D starfield simulation")
		
		self.clock = pygame.time.Clock()
		self.num_stars = num_stars
		self.max_depth = max_depth
		
		self.init_stars()
	
	def init_stars(self):
		#Create the starfield
		self.stars = []
		for i in range(self.num_stars):
			#A star is represented as a list of [X, Y, Z]
			star = [randrange(-25,25), randrange(-25,25), randrange(1,self.max_depth)]
			self.stars.append(star)
			
	def move_and_draw_stars(self):
		#Move and draw all the stars
		
		#Middle points are half the width and half the height
		origin_x = self.screen.get_width() / 2
		origin_y = self.screen.get_height() / 2
		
		#Decrease the third (Z) component of every star on each frame by 0.19
		for star in self.stars:
			star[2] -= var
			
			#If the star is past the screen (Z <= 0,) reposition it at the max depth (far away) with random x and y coordinates
			if star[2] <= 0:
				star[0] = randrange(-25,25)
				star[1] = randrange(-25,25)
				star[2] = self.max_depth
				
			#Convert 3D coords to 2D by using perspective projection (which I don't pretend to understand)
			'''Divide 128 by the Z value'''
			k = 128.0 / star[2]
			'''2D X value is the x value * that ^ plus the center x point'''
			x = int(star[0] * k + origin_x)
			'''2D Y value is the y value * that ^^ plus the center Y point'''
			y = int(star[1] * k + origin_y)
			
			#Draw the star (If it's on screen), make sure closer Z values are equal to bigger dots using liner interpolation
			if 0 <= x < self.screen.get_width() and 0 <= y < self.screen.get_height():
				size = (1 - float(star[2]) / self.max_depth) * 5
				shade = (1 - float(star[2]) / self.max_depth) * 255
				self.screen.fill((shade,shade,shade),(x,y,size,size))
	
	#The main loop
	def run(self):
		while 1:
			#Lock framerate to 50 FPS
			self.clock.tick(50)
			
			var = slider.get()
			
			#Process all events to reduce lag and prevent error messages when exiting. Also, manage scrolling
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					sys.exit()
				
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_DOWN:
						if var >= .3:                                                                                                                                                         
							global var
							var -= .3
					if event.key == pygame.K_UP:
						global var
						var += .3
			
			self.screen.fill((0,0,0))
			self.move_and_draw_stars()
			pygame.display.flip()
			tk.update()
if __name__ == "__main__":
	Simulation(512, 32).run()
