import turtle

star = turtle.Turtle()

step = 1

while(True):
	star.forward(step)
	star.right(144)
	step = step + 3

turtle.done()