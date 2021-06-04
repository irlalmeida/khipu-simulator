import turtle

turtle.register_shape("src/quipu-sewing.gif")

# set environment
screen = turtle.getscreen()
screen.bgcolor("black")

#write title
turtle.hideturtle()
turtle.penup()
turtle.pen(pencolor="white")
turtle.goto(0, 300)
turtle.write("Quipu Simulator", True, align="center", font=("Panibo", 50, "normal"))

#user input
#first_strand_color = screen.textinput("Select Product", "What product are you accounting for?")
first_strand_color = "red"

# configure pen
turtle.pendown()
hand = turtle.Turtle()
hand.pen(pencolor="white", pensize=2, speed=10)
hand.shape("src/quipu-sewing.gif")

#drawing
hand.circle(100,-90)
hand.circle(100,180)
hand.circle(100,-145)
hand.pen(pencolor=first_strand_color, pensize=2, speed=1)
hand.goto(-130, -5)
hand.color(first_strand_color)
hand.begin_fill()
hand.circle(4)
hand.rt(80)
hand.fd(4)
hand.circle(4)
hand.end_fill()
hand.fd(50)

hand.penup()

#second_strand_color = screen.textinput("Select Product", "What product are you accounting for?")

turtle.getscreen()._root.mainloop()

