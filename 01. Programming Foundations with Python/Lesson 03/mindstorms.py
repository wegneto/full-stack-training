import turtle

def draw_square(some_turtle):
	for x in range(0, 4):
		some_turtle.forward(100)
		some_turtle.right(90)

def draw_shapes():
	window = turtle.Screen()
	window.bgcolor("red")

	#draw a circle out of squares
	brad = turtle.Turtle()
	brad.shape("turtle")
	brad.color("yellow")
	for i in range (1,37):
		draw_square(brad)
		brad.right(10)

	window.exitonclick()

def draw_rhombus(some_turtle, length, angle):
	for i in range (1,3):
		some_turtle.forward(length)
		some_turtle.left(180-angle)
		some_turtle.forward(length)
		some_turtle.left(angle)

def draw_flower():
	window = turtle.Screen()
	window.bgcolor("red")

	#draw a circle out of squares
	brad = turtle.Turtle()
	brad.shape("turtle")
	brad.color("yellow")
	for i in range (1,73):
		draw_rhombus(brad, 100, 140)
		brad.right(5)

	window.exitonclick()

def draw_triangle():
	window = turtle.Screen()
	window.bgcolor("red")

	#draw a circle out of squares
	triangle = turtle.Turtle()
	triangle.color("yellow")
	triangle.forward(110)
	triangle.left(180-65)
	triangle.forward(140)
	triangle.left(180-50)
	triangle.forward(140)

	window.exitonclick()

#draw_shapes()
#draw_flower()
draw_triangle()