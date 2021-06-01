import turtle
turtle.register_shape("quipu-sewing.gif")

# set environment
screen = turtle.getscreen()
screen.bgcolor("black")

# configure pen
hand = turtle.Turtle()
#hand.hideturtle()
hand.pen(pencolor="white", pensize=2, speed=1)
hand.shape("quipu-sewing.gif")

#drawing
hand.circle(100,-90)
hand.circle(100,180)
hand.circle(100,-145)
hand.pen(pencolor="red", pensize=2, speed=1)
hand.goto(-140, -10)


#t.right(90)
#t.forward(100)
#t.left(90)
#t.backward(200)
#t.circle(200)

#turtle.getscreen()._root.mainloop()