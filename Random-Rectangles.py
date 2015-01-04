from Tkinter import *
import random

tk = Tk()

canvas = Canvas(tk, width=400, height=400)
canvas.grid(row=0,column=1)

Option = StringVar()
Option.set("None")
menu = OptionMenu(tk, Option,"None", "Colored Outlines", "Colored Fills")
menu.grid(row=1,column=1)

colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']

slider = Scale(tk, from_=0, to=1000, label="Rectangles", resolution=50,length=400)
slider.grid(row=0,column=2)
slider.set(100)

def random_rectangle(width, height):
	x1 = random.randrange(width)
	y1 = random.randrange(height)
	x2 = x1 + random.randrange(width)
	y2 = y1 + random.randrange(height)
	canvas.create_rectangle(x1, y1, x2, y2)
	
def random_outline_rectangle(width, height):
	x1 = random.randrange(width)
	y1 = random.randrange(height)
	x2 = x1 + random.randrange(width)
	y2 = y1 + random.randrange(height)
	color = random.choice(colors)
	canvas.create_rectangle(x1, y1, x2, y2, outline=color)
	
def random_color_rectangle(width, height):
	x1 = random.randrange(width)
	y1 = random.randrange(height)
	x2 = x1 + random.randrange(width)
	y2 = y1 + random.randrange(height)
	color = random.choice(colors)
	canvas.create_rectangle(x1, y1, x2, y2, fill=color, outline=color  )

def Generate():
	count = slider.get()
	global option
	canvas.delete("all")
	if Option.get() == "None":
		for x in range(0,count):
			random_rectangle(400, 400)
	elif Option.get() == "Colored Outlines":
		for x in range(0,count):
			random_outline_rectangle(400,400)
	elif Option.get() == "Colored Fills":
		for x in range(0,count):
			random_color_rectangle(400,400)
			
button = button = Button(tk, text="Generate", command=Generate)
button.grid(row=1,column=2)

tk.mainloop()

