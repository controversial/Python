#Spirograph.py
from math import *
from Tkinter import *
import time

tk = Tk()

canvas = Canvas(tk, width=500, height=500)
canvas.pack(side=LEFT)
canvas.configure(scrollregion=(-250, -250, 250, 250))

frame = Frame(tk, bd=2, relief=GROOVE)
frame.pack(side=LEFT)


label1 = Label(frame, text="Angular Velocities")
label1.grid(row=0, column=0, columnspan=2)

scale1 = Scale(frame, from_=10, to=-10, resolution=0, label="1")
scale1.grid(row=1, column=0)

scale2 = Scale(frame, from_=10, to=-10, resolution=0, label="2")
scale2.grid(row=1, column=1)

spacer = LabelFrame(frame, height=20)
spacer.grid(row=2, column=0)

label2 = Label(frame, text="Arm Lengths")
label2.grid(row=3, column=0, columnspan=2)

scale3 = Scale(frame, from_=10, to=-10, resolution=0, label="1")
scale3.grid(row=4, column=0)

scale4 = Scale(frame, from_=10, to=-10, resolution=0, label="2")
scale4.grid(row=4, column=1)


def create_point(coords, canv=canvas):
    assert len(coords) == 2
    canv.create_line(coords[0], coords[1], coords[0]+1, coords[1]+1)

def create_line(coords1, coords2, canv=canvas):
    line = canvas.create_line(coords1[0], coords1[1], coords2[1], coords2[1])
    return line

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

def createSpiral(armOne, armTwo):

    x, y = 0, 0
    len1, step1 = armOne
    len2, step2 = armTwo
    lines = []
    previousPositions = []

    while step1 > 10 or step2 > 10:
        step1 /= 2
        step2 /= 2


    run = 1
    iteration = 1
    inarow = 0
    while run:
        scale1.set(step1)
        scale2.set(step2)
        iteration += 1

        point1 = rotate((0,len1), x)
        point2 = map(sum,zip(rotate((0, len2), y), point1))

        #Detection of whether pattern is repeating itself
        if point2 not in previousPositions:
            previousPositions.append(point2)
            inarow = 0
        else:
            inarow += 1

        if inarow > 5:
            print "Pattern is detected to be repeating itself"
            run = 0


        if x == 0:
            oldpoint2 = point2
        else:
            canvas.create_line(oldpoint2[0], oldpoint2[1], point2[0], point2[1])
        lines.append( canvas.create_line(0, 0, point1[0], point1[1], fill="#5CE6E6", width=3.0) )
        lines.append( canvas.create_line(point1[0], point1[1], point2[0], point2[1], fill="#5CE6E6", width=3.0) )
        oldpoint2 = point2

        tk.update()

        x += step1
        if x > 360: x -= 360
        y += step2
        if y > 360: y -= 360

        for line in lines:
            canvas.delete(line)
        lines = []
        time.sleep(0.005)
    print "Done!"
    time.sleep(5)



createSpiral((50, 5), (50, 8.8))
