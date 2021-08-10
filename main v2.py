import turtle

turtle.register_shape("src/khipu-sewing.gif")

hand = turtle.Turtle()

def makeCircle(angle):
	hand.begin_fill()
	hand.circle(4)
	hand.seth(angle)
	hand.fd(8)
	hand.end_fill()

def makeKnots(amount, space, angle):
	while (amount > 0):
		makeCircle(angle)
		amount = amount - 1
	hand.fd(space)

def drawChecksum(x,y):
## configure pen
	turtle.pendown()
	hand = turtle.Turtle()
	hand.pen(pencolor="white", pensize=2, speed=10)
	hand.shape("src/khipu-sewing.gif")

#main chord
	hand.circle(200,-50)
	hand.circle(200,100)
	hand.circle(200,-100)

# #fisrt strand
	hand.pen(pencolor="brown", pensize=2, speed=1)
	hand.seth(220)
	hand.fd(25)
	hand.color("brown")
#ten thousands
	hand.fd(50)
# #thousands
	makeKnots(3, 50, 220)
# #hundreds
	makeKnots(3, 50, 220)
# #decimals
	makeKnots(1, 50, 220)
# #unities
	makeKnots(7, 20, 220)
	
	hand.penup()
	hand.seth(0)
	hand.goto(0,0)
	hand.circle(200,-45)
	hand.pendown()
# #second strand
	hand.pen(pencolor="brown", pensize=2, speed=1)
	hand.seth(225)
	hand.fd(25)
	hand.color("brown")
 #ten thousands
	hand.seth(225)
	hand.fd(50)
# #thousands
	makeKnots(0, 70, 225)
# #hundreds
	makeKnots (0, 70, 225)
 #decimals
	makeKnots(4, 50, 225)
# #unities
	makeKnots(7, 20, 225)

	hand.penup()
	hand.seth(0)
	hand.goto(0,0)
	hand.circle(200,-40)
	hand.pendown()

# #third strand
	hand.pen(pencolor="brown", pensize=2, speed=1)
	hand.seth(230)
	hand.fd(25)
	hand.color("brown")
# #ten thousands
	hand.seth(230)
	hand.fd(100)
# #thousands
	makeKnots(0, 100, 230)
# #hundreds
	makeKnots (1, 50, 230)
# #decimals
	makeKnots(1, 50, 230)
# #unities
	makeKnots(4, 20, 230)	

	hand.penup()
	hand.seth(0)
	hand.goto(0,0)
	hand.circle(200,-35)
	hand.pendown()
# #fourth strand
	hand.pen(pencolor="brown", pensize=2, speed=1)
	hand.seth(235)
	hand.fd(25)
	hand.color("brown")
# #ten thousands
	hand.seth(235)
	hand.fd(100)
# #thousands
	makeKnots(0, 50, 235)
# #hundreds
	makeKnots (4, 50, 235)
 #decimals
	makeKnots(9, 50, 235)
# #unities
	makeKnots(8, 20, 235)	

	hand.penup()
	hand.seth(0)
	hand.goto(0,0)
	hand.circle(200,-30)
	hand.pendown()

# #fifth strand
	hand.pen(pencolor="brown", pensize=2, speed=1)
	hand.seth(240)
	hand.fd(25)
	hand.color("brown")
# #ten thousands
	hand.seth(240)
	hand.fd(100)
# #thousands
	makeKnots(0, 50, 240)
# #hundreds
	makeKnots (3, 50, 240)
# #decimals
	makeKnots(7, 50, 240)
# #unities
	makeKnots(0, 70, 240)	

	hand.penup()
	hand.seth(0)
	hand.goto(0,0)
	hand.circle(200,-25)
	hand.pendown()

#sixth strand
	hand.pen(pencolor="brown", pensize=2, speed=1)
	hand.seth(245)
	hand.fd(25)
	hand.color("brown")
#ten thousands
	hand.seth(245)
	hand.fd(100)
#thousands
	makeKnots(2, 50, 245)
#hundreds
	makeKnots (2, 50, 245)
#decimals
	makeKnots(8, 50, 245)
#unities
	makeKnots(7, 20, 245)

	hand.penup()
	hand.seth(0)
	hand.goto(0,0)
	hand.circle(200,-20)
	hand.pendown()

#seventh strand
	hand.pen(pencolor="white", pensize=2, speed=1)
	hand.seth(250)
	hand.fd(25)
	hand.color("white")
#ten thousands
	hand.seth(250)
	hand.fd(100)
#thousands
	makeKnots(2, 50, 250)
#hundreds
	makeKnots (0, 70, 250)
#decimals
	makeKnots(8, 50, 250)
#unities
	makeKnots(9, 20, 250)

	hand.penup()
	hand.seth(0)
	hand.goto(0,0)
	hand.circle(200,-15)
	hand.pendown()

#eighth strand
	hand.pen(pencolor="white", pensize=2, speed=1)
	hand.seth(255)
	hand.fd(25)
	hand.color("white")
 #ten thousands
	hand.seth(255)
	hand.fd(50)
# #thousands
	makeKnots(0, 70, 255)
# #hundreds
	makeKnots (0, 70, 255)
 #decimals
	makeKnots(4, 50, 255)
# #unities
	makeKnots(7, 20, 255)

	hand.penup()
	hand.seth(0)
	hand.goto(0,0)
	hand.circle(200,-10)
	hand.pendown()

#nineth strand
	hand.pen(pencolor="white", pensize=2, speed=1)
	hand.seth(260)
	hand.fd(25)
	hand.color("white")
 #ten thousands
	hand.seth(260)
	hand.fd(50)
# #thousands
	makeKnots(0, 70, 260)
# #hundreds
	makeKnots (2, 50, 260)
 #decimals
	makeKnots(0, 100, 260)
# #unities
	makeKnots(3, 20, 260)

	hand.penup()
	hand.seth(0)
	hand.goto(0,0)
	hand.circle(200,-5)
	hand.pendown()

#tenth strand
	hand.pen(pencolor="white", pensize=2, speed=1)
	hand.seth(265)
	hand.fd(25)
	hand.color("white")
 #ten thousands
	hand.seth(265)
	hand.fd(50)
# #thousands
	makeKnots(0, 100, 265)
# #hundreds
	makeKnots (2, 50, 265)
 #decimals
	makeKnots(5, 50, 265)
# #unities
	makeKnots(7, 20, 265)

	hand.penup()
	hand.seth(0)
	hand.goto(0,0)
	hand.circle(200,0)
	hand.pendown()

#eleventh strand
	hand.pen(pencolor="white", pensize=2, speed=1)
	hand.seth(270)
	hand.fd(25)
	hand.color("white")
 #ten thousands
	hand.seth(270)
	hand.fd(50)
# #thousands
	makeKnots(0, 100, 270)
# #hundreds
	makeKnots (3, 50, 270)
 #decimals
	makeKnots(1, 50, 270)
# #unities
	makeKnots(2, 20, 270)

	hand.penup()
	hand.seth(0)
	hand.goto(0,0)
	hand.circle(200,5)
	hand.pendown()

#twelveth strand
	hand.pen(pencolor="white", pensize=2, speed=1)
	hand.seth(275)
	hand.fd(25)
	hand.color("white")
 #ten thousands
	hand.seth(275)
	hand.fd(50)
# #thousands
	makeKnots(1, 50, 275)
# #hundreds
	makeKnots (2, 50, 275)
 #decimals
	makeKnots(7, 50, 275)
# #unities
	makeKnots(1, 20, 275)

	hand.penup()
	hand.seth(0)
	hand.goto(0,0)
	hand.circle(200,10)
	hand.pendown()

#thirteenth strand
	hand.pen(pencolor="grey", pensize=2, speed=1)
	hand.seth(280)
	hand.fd(25)
	hand.color("grey")
 #ten thousands
	hand.seth(280)
	hand.fd(50)
# #thousands
	makeKnots(1, 50, 280)
# #hundreds
	makeKnots (8, 50, 280)
 #decimals
	makeKnots(4, 50, 280)
# #unities
	makeKnots(2, 20, 280)

	hand.penup()
	hand.seth(0)
	hand.goto(0,0)
	hand.circle(200,15)
	hand.pendown()

#fourteenth strand
	hand.pen(pencolor="grey", pensize=2, speed=1)
	hand.seth(285)
	hand.fd(25)
	hand.color("grey")
 #ten thousands
	hand.seth(285)
	hand.fd(50)
# #thousands
	makeKnots(0, 70, 285)
# #hundreds
	makeKnots (0, 70, 285)
 #decimals
	makeKnots(4, 50, 285)
# #unities
	makeKnots(7, 20, 285)

	hand.penup()
	hand.seth(0)
	hand.goto(0,0)
	hand.circle(200,20)
	hand.pendown()

#fifteenth strand
	hand.pen(pencolor="grey", pensize=2, speed=1)
	hand.seth(290)
	hand.fd(25)
	hand.color("grey")
 #ten thousands
	hand.seth(290)
	hand.fd(50)
# #thousands
	makeKnots(0, 100, 290)
# #hundreds
	makeKnots (3, 50, 290)
 #decimals
	makeKnots(5, 50, 290)
# #unities
	makeKnots(3, 20, 290)

	hand.penup()
	hand.seth(0)
	hand.goto(0,0)
	hand.circle(200,0)
	hand.circle(200,25)
	hand.pendown()

#sixteenth strand
	hand.pen(pencolor="grey", pensize=2, speed=1)
	hand.seth(295)
	hand.fd(25)
	hand.color("grey")
 #ten thousands
	hand.seth(295)
	hand.fd(50)
# #thousands
	makeKnots(6, 50, 295)
# #hundreds
	makeKnots (1, 50, 295)
 #decimals
	makeKnots(7, 50, 295)
# #unities
	makeKnots(4, 20, 295)

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

#configure buttons
button_1 = turtle.Turtle()
button_1.penup()
button_1.shapesize(4, 12)
button_1.sety(60)
button_1.shape("square")
button_1.speed(0)
button_1_pos = (0.00,60.00)
button_1.onclick(drawChecksum(0,0))

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

turtle.getscreen()._root.mainloop()