import turtle
turtle.register_shape("includes/khipu-sewing.gif")

# set environment
screen = turtle.getscreen()
screen.title("Khipu Simulator")

#color hashes
W = "#EEEEEE"
MB = "#673923"
GG = "#575E4E"
AB = "#A86540"
NB = "#9E671D"
YB = "#BB8B54"

def drawRosetta(x,y):

	turtle.clearscreen()
	screen.bgcolor("black")
	turtle.pendown()
	hand = turtle.Turtle()
	hand.pen(pencolor=W, pensize=2, speed=0)
	hand.shape("includes/khipu-sewing.gif")

	turtle.hideturtle()
	turtle.penup()
	turtle.speed(0)
	turtle.pen(pencolor=W)
	turtle.sety(200)
	turtle.write("UR88", True, align="center", font=("Panibo", 100, "normal"))
	turtle.setx(0)
	turtle.sety(175)
	turtle.write("chords 1 to 21 ", True, align="center", font=("Panibo", 30, "normal"))

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

##FIRST STRAND
	hand.pen(pencolor=AB, pensize=2, speed=0)
	hand.seth(220)
	hand.fd(25)
	hand.color(AB)
#ten thousands
	hand.fd(50)
# #thousands
	makeKnots(0, 80, 220)
# #hundreds
	makeKnots(0, 80, 220)
# #decimals
	makeKnots(0, 80, 220)
# #unities
	makeKnots(9, 20, 220)
	
	hand.penup()
	hand.seth(0)
	hand.goto(0,0)
	hand.circle(200,-45)
	hand.pendown()
# #SECOND STRAND
	hand.pen(pencolor=NB, pensize=2, speed=0)
	hand.seth(225)
	hand.fd(25)
	hand.color(NB)
 #ten thousands
	hand.seth(225)
	hand.fd(50)
# #thousands
	makeKnots(0, 100, 225)
# #hundreds
	makeKnots(0, 70, 225)
 #decimals
	makeKnots(7, 50, 225)
# #unities
	makeKnots(1, 20, 225)

	hand.penup()
	hand.seth(0)
	hand.goto(0,0)
	hand.circle(200,-40)
	hand.pendown()

# #THIRD STRAND
	hand.pen(pencolor=AB, pensize=2, speed=0)
	hand.seth(230)
	hand.fd(25)
	hand.color(AB)
# #ten thousands
	hand.seth(230)
	hand.fd(100)
# #thousands
	makeKnots(0, 100, 230)
# #hundreds
	makeKnots(0, 70, 230)
# #decimals
	makeKnots(3, 50, 230)
# #unities
	makeKnots(3, 20, 230)	

	hand.penup()
	hand.seth(0)
	hand.goto(0,0)
	hand.circle(200,-35)
	hand.pendown()
# #FOURTH STRAND
	hand.pen(pencolor=AB, pensize=2, speed=0)
	hand.seth(235)
	hand.fd(25)
	hand.color(AB)
# #ten thousands
	hand.seth(235)
	hand.fd(100)
# #thousands
	makeKnots(0, 100, 235)
# #hundreds
	makeKnots(1, 60, 235)
 #decimals
	makeKnots(5, 50, 235)
# #unities
	makeKnots(9, 20, 235)	

	hand.penup()
	hand.seth(0)
	hand.goto(0,0)
	hand.circle(200,-30)
	hand.pendown()

# #FIFTH STRAND
	hand.pen(pencolor=AB, pensize=2, speed=0)
	hand.seth(240)
	hand.fd(25)
	hand.color(AB)
# #ten thousands
	hand.seth(240)
	hand.fd(100)
# #thousands
	makeKnots(0, 100, 240)
# #hundreds
	makeKnots(0, 70, 240)
# #decimals
	makeKnots(1, 50, 240)
# #unities
	makeKnots(0, 70, 240)	

	hand.penup()
	hand.seth(0)
	hand.goto(0,0)
	hand.circle(200,-25)
	hand.pendown()

#SIXTH strand
	hand.pen(pencolor=AB, pensize=2, speed=0)
	hand.seth(245)
	hand.fd(25)
	hand.color(AB)
#ten thousands
	hand.seth(245)
	hand.fd(100)
#thousands
	makeKnots(0, 100, 245)
#hundreds
	makeKnots(0, 70, 245)
#decimals
	makeKnots(1, 50, 245)
#unities
	makeKnots(9, 20, 245)

	hand.penup()
	hand.seth(0)
	hand.goto(0,0)
	hand.circle(200,-20)
	hand.pendown()

# SEVENTH STRAND
	hand.pen(pencolor=AB, pensize=2, speed=0)
	hand.seth(250)
	hand.fd(25)
	hand.color(AB)
#ten thousands
	hand.seth(250)
	hand.fd(100)
#thousands
	makeKnots(0, 80, 250)
#hundreds
	makeKnots(0, 80, 250)
#decimals
	makeKnots(0, 80, 250)
#unities
	makeKnots(9, 20, 250)

	hand.penup()
	hand.seth(0)
	hand.goto(0,0)
	hand.circle(200,-15)
	hand.pendown()

#EIGHTH STRAND
	hand.pen(pencolor=AB, pensize=2, speed=0)
	hand.seth(255)
	hand.fd(15)
	hand.color(AB)

	hand.penup()
	hand.seth(0)
	hand.goto(0,0)
	hand.circle(200,-10)
	hand.pendown()

#NINETH STRAND
	hand.pen(pencolor=AB, pensize=2, speed=0)
	hand.seth(260)
	hand.fd(25)
	hand.color(AB)
 #ten thousands
	hand.seth(260)
	hand.fd(50)
# #thousands
	makeKnots(0, 100, 260)
# #hundreds
	makeKnots(0, 70, 260)
 #decimals
	makeKnots(2, 50, 260)
# #unities
	makeKnots(5, 20, 260)

	hand.penup()
	hand.seth(0)
	hand.goto(0,0)
	hand.circle(200,-5)
	hand.pendown()

#TENTH STRAND
	hand.pen(pencolor=MB, pensize=2, speed=0)
	hand.seth(265)
	hand.fd(25)
	hand.color(MB)
 #ten thousands
	hand.seth(265)
	hand.fd(50)
# #thousands
	makeKnots(0, 100, 265)
# #hundreds
	makeKnots (1, 50, 265)
 #decimals
	makeKnots(6, 50, 265)
# #unities
	makeKnots(4, 20, 265)

	hand.penup()
	hand.seth(0)
	hand.goto(0,0)
	hand.circle(200,0)
	hand.pendown()

#ELEVENTH STRAND
	hand.pen(pencolor=MB, pensize=2, speed=0)
	hand.seth(270)
	hand.fd(25)
	hand.color(MB)
 #ten thousands
	hand.seth(270)
	hand.fd(50)
# #thousands
	makeKnots(0, 80, 270)
# #hundreds
	makeKnots (0, 80, 270)
 #decimals
	makeKnots(2, 50, 270)
# #unities
	makeKnots(0, 50, 270)

	hand.penup()
	hand.seth(0)
	hand.goto(0,0)
	hand.circle(200,5)
	hand.pendown()

#TWELVETH STRAND
	hand.pen(pencolor=AB, pensize=2, speed=0)
	hand.seth(275)
	hand.fd(25)
	hand.color(AB)
 #ten thousands
	hand.seth(275)
	hand.fd(50)
# #thousands
	makeKnots(0, 70, 275)
# #hundreds
	makeKnots (0, 70, 275)
 #decimals
	makeKnots(1, 70, 275)
# #unities
	makeKnots(8, 20, 275)

	hand.penup()
	hand.seth(0)
	hand.goto(0,0)
	hand.circle(200,10)
	hand.pendown()

#THIRTEENTH STRAND
	hand.pen(pencolor=YB, pensize=2, speed=0)
	hand.seth(280)
	hand.fd(25)
	hand.color(YB)
 #ten thousands
	hand.seth(280)
	hand.fd(50)
# #thousands
	makeKnots(0, 80, 280)
# #hundreds
	makeKnots (0, 80, 280)
 #decimals
	makeKnots(0, 80, 280)
# #unities
	makeKnots(9, 20, 280)

	hand.penup()
	hand.seth(0)
	hand.goto(0,0)
	hand.circle(200,15)
	hand.pendown()

#FOURTEENTH STRAND
	hand.pen(pencolor=YB, pensize=2, speed=0)
	hand.seth(285)
	hand.fd(25)
	hand.color(YB)
 #ten thousands
	hand.seth(285)
	hand.fd(50)
# #thousands
	makeKnots(0, 70, 285)
# #hundreds
	makeKnots (0, 70, 285)
 #decimals
	makeKnots(6, 50, 285)
# #unities
	makeKnots(5, 20, 285)

	hand.penup()
	hand.seth(0)
	hand.goto(0,0)
	hand.circle(200,20)
	hand.pendown()

#FIFTEENTH STRAND
	hand.pen(pencolor=YB, pensize=2, speed=0)
	hand.seth(290)
	hand.fd(25)
	hand.color(YB)
 #ten thousands
	hand.seth(290)
	hand.fd(50)
# #thousands
	makeKnots(0, 70, 290)
# #hundreds
	makeKnots (0, 70, 290)
 #decimals
	makeKnots(3, 50, 290)
# #unities
	makeKnots(9, 20, 290)

	hand.penup()
	hand.seth(0)
	hand.goto(0,0)
	hand.circle(200,0)
	hand.circle(200,25)
	hand.pendown()

#SIXTEENTH STRAND
	hand.pen(pencolor=W, pensize=2, speed=0)
	hand.seth(295)
	hand.fd(25)
	hand.color(W)
 #ten thousands
	hand.seth(295)
	hand.fd(50)
# #thousands
	makeKnots(0, 70, 295)
# #hundreds
	makeKnots (1, 50, 295)
 #decimals
	makeKnots(7, 50, 295)
# #unities
	makeKnots(7, 20, 295)

	hand.penup()
	hand.seth(0)
	hand.goto(0,0)
	hand.circle(200,0)
	hand.circle(200,30)
	hand.pendown()

#SEVENTEENTH STRAND
	hand.pen(pencolor=W, pensize=2, speed=0)
	hand.seth(300)
	hand.fd(25)
	hand.color(W)
 #ten thousands
	hand.seth(300)
	hand.fd(50)
# #thousands
	makeKnots(0, 70, 300)
# #hundreds
	makeKnots (0, 70, 300)
 #decimals
	makeKnots(2, 50, 300)
# #unities
	makeKnots(4, 20, 300)

	hand.penup()
	hand.seth(0)
	hand.goto(0,0)
	hand.circle(200,0)
	hand.circle(200,35)
	hand.pendown()

#EIGHTEENTH STRAND
	hand.pen(pencolor=W, pensize=2, speed=0)
	hand.seth(305)
	hand.fd(25)
	hand.color(W)
 #ten thousands
	hand.seth(305)
	hand.fd(50)
# #thousands
	makeKnots(0, 70, 305)
# #hundreds
	makeKnots (0, 70, 305)
 #decimals
	makeKnots(1, 70, 305)
# #unities
	makeKnots(7, 20, 305)

	hand.penup()
	hand.seth(0)
	hand.goto(0,0)
	hand.circle(200,0)
	hand.circle(200,40)
	hand.pendown()

#NINETEENTH STRAND
	hand.pen(pencolor=GG, pensize=2, speed=0)
	hand.seth(310)
	hand.fd(25)
	hand.color(GG)
 #ten thousands
	hand.seth(310)
	hand.fd(50)
# #thousands
	makeKnots(0, 80, 310)
# #hundreds
	makeKnots (0, 80, 310)
 #decimals
	makeKnots(0, 80, 310)
# #unities
	makeKnots(9, 20, 310)

	hand.penup()
	hand.seth(0)
	hand.goto(0,0)
	hand.circle(200,0)
	hand.circle(200,45)
	hand.pendown()

#TWENTIETH STRAND
	hand.pen(pencolor=GG, pensize=2, speed=0)
	hand.seth(315)
	hand.fd(25)
	hand.color(GG)
 #ten thousands
	hand.seth(315)
	hand.fd(50)
# #thousands
	makeKnots(0, 80, 315)
# #hundreds
	makeKnots (0, 80, 315)
 #decimals
	makeKnots(3, 50, 315)
# #unities
	makeKnots(8, 20, 315)

	hand.penup()
	hand.seth(0)
	hand.goto(0,0)
	hand.circle(200,0)
	hand.circle(200,50)
	hand.pendown()

#TWENTY FIRST STRAND
	hand.pen(pencolor=GG, pensize=2, speed=0)
	hand.seth(320)
	hand.fd(25)
	hand.color(GG)
 #ten thousands
	hand.seth(320)
	hand.fd(50)
# #thousands
	makeKnots(0, 80, 320)
# #hundreds
	makeKnots (0, 80, 320)
 #decimals
	makeKnots(0, 80, 320)
# #unities
	makeKnots(9, 20, 320)

	hand.hideturtle()