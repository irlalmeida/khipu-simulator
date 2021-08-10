import turtle
from khipus import drawChecksum

# set environment
screen = turtle.getscreen()
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

#configure buttons
button_1 = turtle.Turtle()
button_1.penup()
button_1.shapesize(4, 12)
button_1.sety(60)
button_1.shape("square")
button_1.speed(0)
button_1_pos = (0.00,60.00)
button_1.onclick(khipu_1)
button_2 = turtle.Turtle()
button_2.shapesize(4, 12)
button_2.sety(-40)
button_2.shape("square")
button_2.speed(0)
button_2_pos = button_2.pos()
button_3 = turtle.Turtle()
button_3.shapesize(4, 12)
button_3.sety(-140)
button_3.shape("square")
button_3.speed(0)
button_3_pos = button_3.pos()
button_4 = turtle.Turtle()
button_4.shapesize(4, 12)
button_4.sety(-240)
button_4.shape("square")
button_4.speed(0)
button_4_pos = button_4.pos()
button_1.pen(pencolor="white", pensize=50)
button_1.fillcolor("white")
button_2.pen(pencolor="white", pensize=50)
button_2.fillcolor("white")
button_3.pen(pencolor="white", pensize=50)
button_3.fillcolor("white")
button_4.pen(pencolor="white", pensize=50)
button_4.fillcolor("white")
button_1_caption = turtle.Turtle()
button_1_caption.hideturtle()
button_1_caption.penup()
button_1_caption.speed(0)
button_1_caption.pen(pencolor="black")
button_1_caption.sety(45)
button_1_caption.write("check sums", True, align="center", font=("Panibo", 20, "normal"))
button_2_caption = turtle.Turtle()
button_2_caption.hideturtle()
button_2_caption.penup()
button_2_caption.speed(0)
button_2_caption.pen(pencolor="black")
button_2_caption.sety(-55)
button_2_caption.write("census", True, align="center", font=("Panibo", 20, "normal"))
button_3_caption = turtle.Turtle()
button_3_caption.hideturtle()
button_3_caption.penup()
button_3_caption.speed(0)
button_3_caption.pen(pencolor="black")
button_3_caption.sety(-155)
button_3_caption.write("storage", True, align="center", font=("Panibo", 20, "normal"))
button_4_caption = turtle.Turtle()
button_4_caption.hideturtle()
button_4_caption.penup()
button_4_caption.speed(0)
button_4_caption.pen(pencolor="black")
button_4_caption.sety(-255)
button_4_caption.write("credits", True, align="center", font=("Panibo", 20, "normal"))
screen.mainloop()
