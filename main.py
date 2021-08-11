import turtle
from credits import drawCredits
from drawChecksum import drawChecksum
from drawCensus import drawCensus
from drawRosetta import drawRosetta
from button_back import drawBackButton

screen = turtle.getscreen()

def drawMainScreen(x,y):
# set environment
	turtle.clearscreen()
	screen.title("Khipu Simulator")
	screen.setup (width=.9, height=.95)
	screen.bgcolor("black")

	#write title
	turtle.hideturtle()
	turtle.penup()
	turtle.speed(0)
	turtle.pen(pencolor="white")
	turtle.sety(200)
	turtle.write("Khipu Simulator", True, align="center", font=("Panibo", 100, "normal"))

	def khipu_1(x,y):
		drawChecksum(0,0)
		drawBackButton(drawMainScreen)
	def khipu_2(x,y):
		drawCensus(0,0)
		drawBackButton(drawMainScreen)
	def khipu_3(x,y):
		drawRosetta(0,0)
		drawBackButton(drawMainScreen)
	def credits(x,y):
		drawCredits(0,0)
		drawBackButton(drawMainScreen)
	def quit(x,y):
		turtle.bye()

	#configure buttons
	button_1 = turtle.Turtle()
	button_1.hideturtle()
	button_1.penup()
	button_1.shapesize(4, 12)
	button_1.sety(60)
	button_1.shape("square")
	button_1.speed(0)
	button_1.pen(pencolor="white", pensize=50, speed=0)
	button_1.fillcolor("white")
	button_1.showturtle()
	button_1.onclick(khipu_1)

	button_2 = turtle.Turtle()
	button_2.hideturtle()
	button_2.penup()
	button_2.shapesize(4, 12)
	button_2.sety(-40)
	button_2.shape("square")
	button_2.speed(0)
	button_2.pen(pencolor="white", pensize=50, speed=0)
	button_2.fillcolor("white")
	button_2.showturtle()
	button_2.onclick(khipu_2)

	button_3 = turtle.Turtle()
	button_3.hideturtle()
	button_3.penup()
	button_3.shapesize(4, 12)
	button_3.sety(-140)
	button_3.shape("square")
	button_3.speed(0)
	button_3.pen(pencolor="white", pensize=50, speed=0)
	button_3.fillcolor("white")
	button_3.showturtle()
	button_3.onclick(khipu_3)

	button_4 = turtle.Turtle()
	button_4.hideturtle()
	button_4.penup()
	button_4.shapesize(4, 12)
	button_4.sety(-240)
	button_4.shape("square")
	button_4.speed(0)
	button_4.pen(pencolor="white", pensize=50, speed=0)
	button_4.fillcolor("white")
	button_4.showturtle()
	button_4.onclick(credits)

	button_5 = turtle.Turtle()
	button_5.hideturtle()
	button_5.penup()
	button_5.shapesize(4, 12)
	button_5.sety(-340)
	button_5.shape("square")
	button_5.speed(0)
	button_5.pen(pencolor="white", pensize=50, speed=0)
	button_5.fillcolor("white")
	button_5.showturtle()
	button_5.onclick(quit)

	button_1_caption = turtle.Turtle()
	button_1_caption.hideturtle()
	button_1_caption.shape("square")
	button_1_caption.shapesize(4, 12)
	button_1_caption.penup()
	button_1_caption.speed(0)
	button_1_caption.pen(pencolor="black", speed=0)
	button_1_caption.sety(45)
	button_1_caption.write("check sums", True, align="center", font=("Panibo", 20, "normal"))

	button_2_caption = turtle.Turtle()
	button_2_caption.hideturtle()
	button_2_caption.penup()
	button_2_caption.speed(0)
	button_2_caption.pen(pencolor="black", speed=0)
	button_2_caption.sety(-55)
	button_2_caption.write("census", True, align="center", font=("Panibo", 20, "normal"))

	button_3_caption = turtle.Turtle()
	button_3_caption.hideturtle()
	button_3_caption.penup()
	button_3_caption.speed(0)
	button_3_caption.pen(pencolor="black", speed=0)
	button_3_caption.sety(-155)
	button_3_caption.write("rosetta", True, align="center", font=("Panibo", 20, "normal"))

	button_4_caption = turtle.Turtle()
	button_4_caption.hideturtle()
	button_4_caption.penup()
	button_4_caption.speed(0)
	button_4_caption.pen(pencolor="black", speed=0)
	button_4_caption.sety(-255)
	button_4_caption.write("credits", True, align="center", font=("Panibo", 20, "normal"))

	button_5_caption = turtle.Turtle()
	button_5_caption.hideturtle()
	button_5_caption.penup()
	button_5_caption.speed(0)
	button_5_caption.pen(pencolor="black", speed=0)
	button_5_caption.sety(-355)
	button_5_caption.write("quit", True, align="center", font=("Panibo", 20, "normal"))

drawMainScreen(0,0)
turtle.mainloop()
