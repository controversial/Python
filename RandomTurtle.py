import turtle
import random
turtle.setup(500,500)
randy = turtle.Pen()	
while True:
	forward = random.randint(-100, 100)
	randy.forward(forward)
	turn = random.randint(-360, 360)
	directions = ["right", "left"]
	direction = random.choice(directions)
	if direction == "right":
		randy.right(turn)
	elif direction == "left":
		randy.left(turn)
	posx = randy.xcor()
	posy = randy.ycor()
	if posx >= 250 or posx <= -250 or posy >= 250 or posy <= -250:
		randy.goto(0, 0)
