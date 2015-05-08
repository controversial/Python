#Spirograph.py
from math import *
from Tkinter import *
import time
tk = Tk()
canvas = Canvas(tk, width=500, height=500)
canvas.pack()
canvas.configure(scrollregion=(-250, -250, 250, 250))

def rotate(point, angle, center=(0, 0)):
    counterangle = 360 - angle
    while counterangle > 0: counterangle -= 360
    while counterangle < 0: counterangle += 360
    theta = radians(counterangle)
    #Translate point to rotate around center
    translated = point[0]-center[0] , point[1]-center[1]
    #Rotate point
    rotated = (translated[0]*cos(theta)-translated[1]*sin(theta),translated[0]*sin(theta)+translated[1]*cos(theta))
    #Translate point back
    newcoords = (round(rotated[0]+center[0], 1),round(rotated[1]+center[1], 1))
    return newcoords

def create_point(coords, canv=canvas):
    assert len(coords) == 2
    canv.create_line(coords[0], coords[1], coords[0]+1, coords[1]+1)

x, y = 0, 0
lines = []

while 1:
    x += 0.25
    if x > 360:
        x -= 360
        canvas.delete("all")
        time.sleep(1)
    y += 3
    if y > 360: y -= 360

    for line in lines:
        canvas.delete(line)
    lines = []

    point1 = rotate((0,25), x)
    point2 = map(sum,zip(rotate((0, 40), -y), point1))
    create_point(point2)
    lines.append( canvas.create_line(0, 0, point1[0], point1[1]) )
    lines.append( canvas.create_line(point1[0], point1[1], point2[0], point2[1]) )

    tk.update()
