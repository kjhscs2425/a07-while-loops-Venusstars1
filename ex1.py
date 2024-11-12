# Use turtle graphics to make an infinite spiral
import turtle
def infinite_spiral (x):
    while x>=0:
        turtle.forward(x)
        turtle.left(90)
        x = x +10
infinite_spiral(5)