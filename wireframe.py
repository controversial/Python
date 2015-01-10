import sys
import math
import pygame

xrot = 0
yrot = 0

class Point3D:
	def __init__(self, x = 0, y = 0, z = 0):
		self.x = float(x)
		self.y = float(y)
		self.z = float(z)
		
	def rotateX(self, angle):
		# Roatates the point around the X by the given angle in degrees
		rad = angle * math.pi / 180
		cosa = math.cos(rad)
		sina = math.sin(rad)
		y = self.y * cosa - self.z * sina
		z = self.y * sina + self.z * cosa
		return Point3D(self.x, y, z)
	
	def rotateY(self, angle):
		# Rotates the point around the Y by the given angle in degrees
		rad = angle * math.pi / 180
		cosa = math.cos(rad)
		sina = math.sin(rad)
		z = self.z * cosa - self.x * sina
		x = self.z * sina + self.x * cosa
		return Point3D(x, self.y, z)
	
	def rotateZ(self, angle):
		# Rotates the point around the Z by the given angle in degrees
		rad = angle * math.pi / 180
		cosa = math.cos(rad)
		sina = math.sin(rad)
		x = self.x * cosa - self.y * sina
		y = self.x * sina + self.y * cosa
		return Point3D(x, y, self.z)
	
	def project(self, win_width, win_height, fov, viewer_distance):
		#Transforms the 3D point into a 2D projection
		factor = fov / (viewer_distance + self.z)
		x = self.x * factor + win_width / 2
		y = -self.y * factor + win_height / 2
		return Point3D(x, y, 1)
		
class Simulation:
	def __init__(self, win_width = 640, win_height = 480):
		pygame.init()
		
		self.screen = pygame.display.set_mode((win_width, win_height))
		pygame.display.set_caption("Move the mouse to rotate the cube")
		
		self.clock = pygame.time.Clock()
		
		self.vertices = [
            Point3D(-1,1,-1),
            Point3D(1,1,-1),
            Point3D(1,-1,-1),
            Point3D(-1,-1,-1),
            Point3D(-1,1,1),
            Point3D(1,1,1),
            Point3D(1,-1,1),
            Point3D(-1,-1,1)
        ]
		
		self.faces = [(0,1,2,3),(1,5,6,2),(5,4,7,6),(4,0,3,7),(0,4,5,1),(3,2,6,7)]
		
	def run(self):
		while 1:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					sys.exit()
			self.clock.tick(50)
			self.screen.fill((0,0,0))
			
			#Controls Mouse Position
			global xrot
			global yrot
			yvar, xvar = pygame.mouse.get_rel()
			xrot += xvar
			yrot += yvar
			
			#Will hold the transformed vertices
			t = []
			
			for v in self.vertices:
				# Rotate the point around the X axis, then the Y axis, and finally the Z axis
				r = v.rotateX(-xrot / 2).rotateY(-yrot / 2).rotateZ(0)
				
				# Transform the point from 3D to 2D
				p = r.project(self.screen.get_width(), self.screen.get_height(), 256, 4)
				x, y = int(p.x), int(p.y)
				
				# Put the point in the list of transformed vertices
				t.append(p)
			
			for f in self.faces:
				pygame.draw.line(self.screen, (255,255,255), (t[f[0]].x, t[f[0]].y), (t[f[1]].x, t[f[1]].y))
				pygame.draw.line(self.screen, (255,255,255), (t[f[1]].x, t[f[1]].y), (t[f[2]].x, t[f[2]].y))
				pygame.draw.line(self.screen, (255,255,255), (t[f[2]].x, t[f[2]].y), (t[f[3]].x, t[f[3]].y))
				pygame.draw.line(self.screen, (255,255,255), (t[f[3]].x, t[f[3]].y), (t[f[0]].x, t[f[0]].y))
			
			for v in self.vertices:
				# Draw dots on the edges of the cube
				r = v.rotateX(-xrot / 2).rotateY(-yrot / 2).rotateZ(0)
				p = r.project(self.screen.get_width(), self.screen.get_height(), 256, 4)
				x, y = int(p.x), int(p.y)
				pygame.draw.circle(self.screen,(0,255,255),(x,y),4)
				
			pygame.display.flip()
			
if __name__ == "__main__":
	Simulation().run()
