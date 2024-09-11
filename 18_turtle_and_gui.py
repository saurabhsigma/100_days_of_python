# turtle is a module in python, draw graphics onto the screen
from turtle import Turtle, Screen
import random
# or :- from turtle import * 


timmy = Turtle()

# to change the shape of the turtle
timmy.shape("turtle") 
# timmy.pensize(2)
timmy.speed("fastest")

# to change the color of the turtle
timmy.color("red")

list_of_colors = ["green yellow", "dodger blue" , "red", "magenta", "lime green"]
list_of_angles = [0, 90, 180, 270, 360]


def make_a_sqaure():
    timmy.forward(100)
    timmy.right(90)
    timmy.forward(100)
    timmy.right(90)
    timmy.forward(100)
    timmy.right(90)
    timmy.forward(100)
    timmy.right(90)

def dashed_line():
    for _ in range(15):
        timmy.forward(10)
        timmy.color("white")
        timmy.forward(10)
        timmy.color("red")

def dashed_line_using_pen():
    for _ in range(15):
        timmy.forward(10)
        timmy.penup()
        timmy.forward(10)
        timmy.pendown()

def draw_triangle():
    for _ in range(3):
        timmy.forward(100)
        timmy.right(120)
        

# draw_triangle()
def draw_square():
    for _ in range(4):
        timmy.forward(100)
        timmy.right(90)

def draw_pentagon():
    for _ in range(5):
        timmy.forward(100)
        timmy.right(72)

def draw_hexagon():
    for _ in range(6):
        timmy.forward(100)
        timmy.right(60)
    
def draw_heptagon():
    for _ in range(7):
        timmy.forward(100)
        timmy.right(51.43)

def draw_octagon():
    for _ in range(8):
        timmy.forward(100)
        timmy.right(45)

def draw_nonagon():
    for _ in range(9):
        timmy.forward(100)
        timmy.right(40)

def draw_decagon():
    for _ in range(10):
        timmy.forward(100)
        timmy.right(36)

# draw_triangle()
# draw_square()
# draw_pentagon()
# draw_hexagon()
# draw_heptagon()
# draw_octagon()
# draw_nonagon()
# draw_decagon()
# print(random.choice(list_of_angles))

def random_walk():
    for _ in range(100):
        timmy.forward(20)
        timmy.right(random.choice(list_of_angles))
        timmy.color(random.choice(list_of_colors))
        timmy.forward(20)

# random_walk()


def draw_circle():
    for i in range(100):
        timmy.circle(100)
        current_heading = timmy.heading()
        timmy.setheading(current_heading+10)
        timmy.color(random.choice(list_of_colors))
        # timmy.forward(10)
        # timmy.left(1)


draw_circle()

# timmy.circle(50)


# dashed_line_using_pen()
# make_a_sqaure()
# timmy.forward(100)
# dashed_line()


# setting the screen to show
screen = Screen()

# setting the exit on click, so that when we click
#  on the screen then only it exits the game window, not before that
screen.exitonclick()



