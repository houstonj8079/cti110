# Jordan Houston-Taylor
# P4LAB1 Assignment
# April 7, 2024
# This assignment will help me test how to write programs with loops.

import turtle

# Set up the screen
wn = turtle.Screen()
wn.title("Square and Triangle")
wn.setup(width=500, height=500)
wn.bgcolor("white")

# Create a turtle
pen = turtle.Turtle()

# Function to draw a square
def draw_square():
    for _ in range(4):
        pen.forward(100)
        pen.right(90)

# Function to draw a triangle
def draw_triangle():
    for _ in range(3):
        pen.forward(100)
        pen.right(120)

# Move to starting position for the square
pen.penup()
pen.goto(-150,0)
pen.pendown()

# Draw the square
pen.color("orange")
draw_square()

# Move to starting position for the triangle
pen.penup()
pen.goto(-150, 0)
pen.pendown()

# Draw the triangle
pen.color("green")
draw_triangle()


# Set up the screen
wn = turtle.Screen()
wn.title("Drawing the letter J and H")
wn.setup(width=500, height=500)
wn.bgcolor("white")

# Create a turtle
pen = turtle.Turtle()

# Function to draw the letter J
def draw_J():
    pen.penup()
    pen.goto(-50, 100)
    pen.pendown()
    pen.setheading(270)
    pen.circle(50, 180)
    pen.forward(100)
    pen.pendown()

def draw_H():
    pen.penup()
    pen.goto(70, 100)
    pen.pendown()
    pen.setheading(270)
    pen.forward(200)
    pen.penup()
    pen.goto(50, 0)
    pen.pendown()
    pen.setheading(0)
    pen.forward(100)
    pen.penup()
    pen.goto(150, 100)
    pen.pendown()
    pen.setheading(270)
    pen.forward(100)
    pen.forward(100)

# Draw the letter J AND H
pen.color("blue")
draw_J()
draw_H()

# Hide the turtle
pen.hideturtle()

# Keep the window open
wn.mainloop()

