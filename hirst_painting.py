import turtle
import random

# Function to generate a list of random colors
def generate_random_colors(num_colors):
    colors = []
    for _ in range(num_colors):
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        colors.append((r, g, b))
    return colors

# Set up the turtle screen
def setup_screen():
    screen = turtle.Screen()
    screen.setup(width=800, height=800)
    screen.bgcolor("white")
    return screen

# Draw a dot at a given position with a specific color
def draw_dot(x, y, color):
    turtle.penup()
    turtle.goto(x, y)
    turtle.dot(20, color)
    turtle.pendown()

# Main function to create the painting
def create_hirst_painting(colors, grid_size, dot_size):
    turtle.speed('fastest')
    turtle.hideturtle()
    turtle.bgcolor("white")
    
    x_start = -grid_size * dot_size / 2
    y_start = -grid_size * dot_size / 2
    for row in range(grid_size):
        for col in range(grid_size):
            x = x_start + col * dot_size
            y = y_start + row * dot_size
            color = random.choice(colors)
            draw_dot(x, y, color)

# Generate random colors
num_colors = 10
colors = generate_random_colors(num_colors)

# Set up the turtle screen and draw the painting
screen = setup_screen()
create_hirst_painting(colors, grid_size=5, dot_size=50)

# Keep the window open until clicked
screen.exitonclick()

