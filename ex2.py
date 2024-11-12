# make infinite circles, start with a small circle, then draw a bigger circle around it
import turtle
def circle(r):
    while True:
        turtle.circle(r)
        turtle.up()
        turtle.right(90)
        turtle.forward(10)
        turtle.left(90)
        turtle.down()
        r += 10
circle(20)

