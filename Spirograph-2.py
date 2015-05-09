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

def drawSpiral(arms, lenlist, velocitylist):
    assert arms == len(lenlist) == len(velocitylist)
    pointlist = []
    pointlist.append((0, 0))
    angle = 0
    lines = []
    run = 1
    while run:
        angle += 1
        for n in range(arms):
            point = tuple(map(sum,zip(rotate((0, lenlist[n]), angle*velocitylist[n], pointlist[n]))))
            pointlist.append(point)
            print pointlist
        for n in range(len(pointlist)-1):
            lines.append(canvas.create_line(pointlist[n][0], pointlist[n][1], pointlist[n+1][1], pointlist[n+1][1]))
        tk.update()
        for line in lines:
            canvas.delete(line)
        lines = []
        pointlist = []
        pointlist.append((0, 0))

drawSpiral(2, [50, 75], [1, 5])


x, y = 0, 0
lines = []

while 1:

    point1 = rotate((0,25), x)
    point2 = map(sum,zip(rotate((0, 40), -y), point1))
    if x == 0:
        oldpoint2 = point2
    else:
        canvas.create_line(oldpoint2[0], oldpoint2[1], point2[0], point2[1])
    lines.append( canvas.create_line(0, 0, point1[0], point1[1]) )
    lines.append( canvas.create_line(point1[0], point1[1], point2[0], point2[1]) )
    oldpoint2 = point2

    tk.update()

    x += 1
    if x > 360 and y > 360:
        x -= 360
        canvas.delete("all")
        time.sleep(1)
    y += 25
    if y > 360: y -= 360

    for line in lines:
        canvas.delete(line)
    lines = []
    time.sleep(0.025)

