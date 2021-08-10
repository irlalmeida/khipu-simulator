import turtle
turtle.register_shape("src/khipu-sewing.gif")

# set environment
screen = turtle.getscreen()
screen.title("Khipu Simulator")

W = "#EEEEEE"
MB = "#673923"
GG = "#575E4E"
AB = "#A86540"
NB = "#9E671D"
YB = "#BB8B54"

def drawCensus(x,y):

	turtle.clearscreen()
	screen.bgcolor("black")
	turtle.pendown()
	hand = turtle.Turtle()
	hand.pen(pencolor="white", pensize=2, speed=00)
	hand.shape("src/khipu-sewing.gif")

	turtle.hideturtle()
	turtle.penup()
	turtle.speed(0)
	turtle.pen(pencolor=W)
	turtle.sety(200)
	turtle.write("UR011", True, align="center", font=("Panibo", 100, "normal"))

	def makeCircle(angle):
		hand.begin_fill()
		hand.circle(4)
		hand.seth(angle)
		hand.fd(8)
		hand.end_fill()

	def makeKnots(amount, space, angle):
		x = amount
		while (x > 0):
			makeCircle(angle)
			x = x - 1
		hand.fd(space)

#main chord
	hand.circle(200,-50)
	hand.circle(200,100)
	hand.circle(200,-100)

# #fisrt strand
	hand.pen(pencolor=MB, pensize=2, speed=0)
	hand.seth(220)
	hand.fd(25)
	hand.color(MB)
#ten thousands
	hand.fd(50)
# #thousands
	makeKnots(0, 80, 220)
# #hundreds
	makeKnots(0, 80, 220)
# #decimals
	makeKnots(0, 50, 220)
# #unities
	makeKnots(8, 20, 220)
	
	hand.penup()
	hand.seth(0)
	hand.goto(0,0)
	hand.circle(200,-45)
	hand.pendown()
# #second strand
	hand.pen(pencolor=MB, pensize=2, speed=0)
	hand.seth(225)
	hand.fd(25)
	hand.color(MB)
 #ten thousands
	hand.seth(225)
	hand.fd(50)
# #thousands
	makeKnots(0, 70, 225)
# #hundreds
	makeKnots (0, 70, 225)
 #decimals
	makeKnots(5, 50, 225)
# #unities
	makeKnots(2, 20, 225)

	hand.penup()
	hand.seth(0)
	hand.goto(0,0)
	hand.circle(200,-40)
	hand.pendown()

# #third strand
	hand.pen(pencolor=MB, pensize=2, speed=0)
	hand.seth(230)
	hand.fd(25)
	hand.color(MB)
# #ten thousands
	hand.seth(230)
	hand.fd(100)
# #thousands
	makeKnots(0, 100, 230)
# #hundreds
	makeKnots (2, 50, 230)
# #decimals
	makeKnots(8, 50, 230)
# #unities
	makeKnots(1, 20, 230)	

	hand.penup()
	hand.seth(0)
	hand.goto(0,0)
	hand.circle(200,-35)
	hand.pendown()
# #fourth strand
	hand.pen(pencolor=GG, pensize=2, speed=0)
	hand.seth(235)
	hand.fd(15)
	hand.color(GG)
# #ten thousands
	makeKnots(1, 50, 235)
# #thousands
	makeKnots(5, 50, 235)
# #hundreds
	makeKnots(7, 50, 235)
 #decimals
	makeKnots(4, 50, 235)
# #unities
	makeKnots(6, 20, 235)	

	hand.penup()
	hand.seth(0)
	hand.goto(0,0)
	hand.circle(200,-30)
	hand.pendown()

# #fifth strand
	hand.pen(pencolor=W, pensize=2, speed=0)
	hand.seth(240)
	hand.fd(15)
	hand.color(W)
# #ten thousands
	makeKnots(1, 50, 240)
# #thousands
	makeKnots(5, 50, 240)
# #hundreds
	makeKnots(4, 50, 240)
# #decimals
	makeKnots(4, 50, 240)
# #unities
	makeKnots(8, 20, 240)	

	hand.penup()
	hand.seth(0)
	hand.goto(0,0)
	hand.circle(200,-25)
	hand.pendown()

#sixth strand
	hand.pen(pencolor=MB, pensize=2, speed=0)
	hand.seth(245)
	hand.fd(25)
	hand.color(MB)
#ten thousands
	hand.seth(245)
	hand.fd(100)
#thousands
	makeKnots(0, 70, 245)
#hundreds
	makeKnots(1, 50, 245)
#decimals
	makeKnots(6, 50, 245)
#unities
	makeKnots(1, 20, 245)

	hand.penup()
	hand.seth(0)
	hand.goto(0,0)
	hand.circle(200,-20)
	hand.pendown()

#seventh strand
	hand.pen(pencolor=MB, pensize=2, speed=0)
	hand.seth(250)
	hand.fd(25)
	hand.color(MB)
#ten thousands
	hand.seth(250)
	hand.fd(100)
#thousands
	makeKnots(0, 50, 250)
#hundreds
	makeKnots (0, 70, 250)
#decimals
	makeKnots(5, 50, 250)
#unities
	makeKnots(5, 20, 250)

	hand.penup()
	hand.seth(0)
	hand.goto(0,0)
	hand.circle(200,-15)
	hand.pendown()

#eighth strand
	hand.pen(pencolor=AB, pensize=2, speed=0)
	hand.seth(255)
	hand.fd(25)
	hand.color(AB)
 #ten thousands
	hand.seth(255)
	hand.fd(50)
# #thousands
	makeKnots(0, 70, 255)
# #hundreds
	makeKnots (2, 50, 255)
 #decimals
	makeKnots(6, 50, 255)
# #unities
	makeKnots(3, 20, 255)

	hand.penup()
	hand.seth(0)
	hand.goto(0,0)
	hand.circle(200,-10)
	hand.pendown()

#nineth strand
	hand.pen(pencolor=AB, pensize=2, speed=0)
	hand.seth(260)
	hand.fd(15)
	hand.color(AB)
 #ten thousands
	makeKnots(1, 50, 260)
# #thousands
	makeKnots(0, 100, 260)
# #hundreds
	makeKnots (8, 50, 260)
 #decimals
	makeKnots(0, 80, 260)
# #unities
	makeKnots(9, 20, 260)

	hand.penup()
	hand.seth(0)
	hand.goto(0,0)
	hand.circle(200,-5)
	hand.pendown()

#tenth strand
	hand.pen(pencolor=W, pensize=2, speed=0)
	hand.seth(265)
	hand.fd(15)
	hand.color(W)
 #ten thousands
	makeKnots(1, 50, 265)
# #thousands
	makeKnots(1, 90, 265)
# #hundreds
	makeKnots (0, 80, 265)
 #decimals
	makeKnots(5, 50, 265)
# #unities
	makeKnots(6, 20, 265)

	hand.penup()
	hand.seth(0)
	hand.goto(0,0)
	hand.circle(200,0)
	hand.pendown()

#eleventh strand
	hand.pen(pencolor=MB, pensize=2, speed=0)
	hand.seth(270)
	hand.fd(25)
	hand.color(MB)
 #ten thousands
	hand.seth(270)
	hand.fd(50)
# #thousands
	makeKnots(0, 100, 270)
# #hundreds
	makeKnots (2, 50, 270)
 #decimals
	makeKnots(3, 50, 270)
# #unities
	makeKnots(7, 20, 270)

	hand.penup()
	hand.seth(0)
	hand.goto(0,0)
	hand.circle(200,5)
	hand.pendown()

#twelveth strand
	hand.pen(pencolor=MB, pensize=2, speed=0)
	hand.seth(275)
	hand.fd(25)
	hand.color(MB)
 #ten thousands
	hand.seth(275)
	hand.fd(50)
# #thousands
	makeKnots(0, 80, 275)
# #hundreds
	makeKnots (0, 80, 275)
 #decimals
	makeKnots(4, 50, 275)
# #unities
	makeKnots(4, 20, 275)

	hand.penup()
	hand.seth(0)
	hand.goto(0,0)
	hand.circle(200,10)
	hand.pendown()

#thirteenth strand
	hand.pen(pencolor=AB, pensize=2, speed=0)
	hand.seth(280)
	hand.fd(25)
	hand.color(AB)
 #ten thousands
	hand.seth(280)
	hand.fd(50)
# #thousands
	makeKnots(0, 80, 280)
# #hundreds
	makeKnots (2, 50, 280)
 #decimals
	makeKnots(5, 50, 280)
# #unities
	makeKnots(8, 20, 280)

	hand.penup()
	hand.seth(0)
	hand.goto(0,0)
	hand.circle(200,15)
	hand.pendown()

#fourteenth strand
	hand.pen(pencolor=GG, pensize=2, speed=0)
	hand.seth(285)
	hand.fd(15)
	hand.color(GG)
 #ten thousands
	makeKnots(1, 70, 285)
# #thousands
	makeKnots(1, 70, 285)
# #hundreds
	makeKnots (5, 70, 285)
 #decimals
	makeKnots(3, 50, 285)
# #unities
	makeKnots(2, 20, 285)

	hand.penup()
	hand.seth(0)
	hand.goto(0,0)
	hand.circle(200,20)
	hand.pendown()

#fifteenth strand
	hand.pen(pencolor=W, pensize=2, speed=0)
	hand.seth(290)
	hand.fd(25)
	hand.color(W)
 #ten thousands
	hand.seth(290)
	hand.fd(50)
# #thousands
	makeKnots(9, 20, 290)
# #hundreds
	makeKnots (5, 50, 290)
 #decimals
	makeKnots(4, 50, 290)
# #unities
	makeKnots(7, 20, 290)

	hand.penup()
	hand.seth(0)
	hand.goto(0,0)
	hand.circle(200,0)
	hand.circle(200,25)
	hand.pendown()

#sixteenth strand
	hand.pen(pencolor=MB, pensize=2, speed=0)
	hand.seth(295)
	hand.fd(25)
	hand.color(MB)
 #ten thousands
	hand.seth(295)
	hand.fd(50)
# #thousands
	makeKnots(0, 50, 295)
# #hundreds
	makeKnots (2, 50, 295)
 #decimals
	makeKnots(5, 50, 295)
# #unities
	makeKnots(3, 20, 295)

	hand.penup()
	hand.seth(0)
	hand.goto(0,0)
	hand.circle(200,0)
	hand.circle(200,30)
	hand.pendown()

#SEVENTEENTH STRAND
	hand.pen(pencolor=MB, pensize=2, speed=0)
	hand.seth(300)
	hand.fd(25)
	hand.color(MB)
 #ten thousands
	hand.seth(300)
	hand.fd(50)
# #thousands
	makeKnots(0, 70, 300)
# #hundreds
	makeKnots (0, 70, 300)
 #decimals
	makeKnots(3, 50, 300)
# #unities
	makeKnots(3, 20, 300)

	hand.penup()
	hand.seth(0)
	hand.goto(0,0)
	hand.circle(200,0)
	hand.circle(200,35)
	hand.pendown()

#EIGHTEENTH STRAND
	hand.pen(pencolor=AB, pensize=2, speed=0)
	hand.seth(305)
	hand.fd(25)
	hand.color(AB)
 #ten thousands
	hand.seth(305)
	hand.fd(50)
# #thousands
	makeKnots(0, 70, 305)
# #hundreds
	makeKnots (2, 70, 305)
 #decimals
	makeKnots(3, 70, 305)
# #unities
	makeKnots(6, 20, 305)

	hand.penup()
	hand.seth(0)
	hand.goto(0,0)
	hand.circle(200,0)
	hand.circle(200,40)
	hand.pendown()

#NINETEENTH STRAND
	hand.pen(pencolor=AB, pensize=2, speed=0)
	hand.seth(310)
	hand.fd(25)
	hand.color(AB)
 #ten thousands
	hand.seth(310)
	hand.fd(50)
# #thousands
	makeKnots(8, 50, 310)
# #hundreds
	makeKnots (7, 50, 310)
 #decimals
	makeKnots(6, 50, 310)
# #unities
	makeKnots(4, 20, 310)

	hand.penup()
	hand.seth(0)
	hand.goto(0,0)
	hand.circle(200,0)
	hand.circle(200,45)
	hand.pendown()

#TWENTIETH STRAND
	hand.pen(pencolor=W, pensize=2, speed=0)
	hand.seth(315)
	hand.fd(25)
	hand.color(W)
 #ten thousands
	hand.seth(315)
	hand.fd(50)
# #thousands
	makeKnots(8, 50, 315)
# #hundreds
	makeKnots (5, 50, 315)
 #decimals
	makeKnots(9, 50, 315)
# #unities
	makeKnots(2, 20, 315)
