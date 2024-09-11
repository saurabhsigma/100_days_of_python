# from turtle import *
# import turtle

# screen = turtle.Screen()
# screen.setup(width=600, height=600)
# screen.bgcolor("white")

# # Create a turtle named "pen"
# pen = turtle.Turtle()

# # Make the turtle move forward by 100 units
# pen.forward(100)

# # Make the turtle turn left by 100 degrees
# pen.left(100)


# # Make the turtle move forward again by 100 units to see the result of the turn
# pen.forward(100)

# # Hide the turtle and finish
# pen.hideturtle()

# # Keep the window open until clicked
# screen.exitonclick()

import turtle
from turtle import Turtle, Screen
import random

timmy = Turtle()

timmy.shape("turtle")
timmy.speed("slowest")
timmy.color("red")


for i in range(4):
    timmy.forward(100)
    timmy.left(90)





screen = Screen()

screen.exitonclick()