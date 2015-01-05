import turtle
import random  
turtle.setup(500,500)
randy = turtle.Pen()
while True:
	randy.forward(random.randint(-100, 100))
	randy.setheading(random.randint(-360, 360))
	if randy.xcor() >= 250 or randy.xcor() <= -250 or randy.ycor() >= 250 or randy.ycor() <= -250:
		randy.goto(0, 0)
