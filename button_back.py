import turtle

def drawBackButton(handleClick):

	screen = turtle.getscreen()
	screen.title("Khipu Simulator")
	screen.setup (width=.9, height=.95)
	screen.bgcolor("black")

	back_button = turtle.Turtle()
	back_button.hideturtle()
	back_button.penup()
	back_button.shapesize(3, 8)
	back_button.setx(800)
	back_button.sety(-400)
	back_button.shape("square")
	back_button.speed(0)
	back_button.pen(pencolor="white", pensize=50, speed=0)
	back_button.fillcolor("white")
	back_button.showturtle()
	back_button.onclick(handleClick)

	back_button_caption = turtle.Turtle()
	back_button_caption.hideturtle()
	back_button_caption.penup()
	back_button_caption.speed(0)
	back_button_caption.pen(pencolor="black", speed=0)
	back_button_caption.setx(800)
	back_button_caption.sety(-415)
	back_button_caption.write("back", True, align="center", font=("Panibo", 20, "normal"))
